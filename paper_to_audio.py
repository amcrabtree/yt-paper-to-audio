#!/usr/bin/env python
"""CLI to convert a scientific paper PDF into a spoken-word audio summary."""

import argparse
import io
import os
import re
import warnings
from pathlib import Path

warnings.filterwarnings(
    "ignore",
    message=r"`torch\.nn\.utils\.weight_norm` is deprecated",
    category=FutureWarning,
)

import litellm
import numpy as np
import soundfile as sf
from dotenv import load_dotenv
from pydub import AudioSegment
from pypdf import PdfReader
from tqdm.auto import tqdm

PROJECT_ROOT = Path(__file__).parent

DEFAULT_MODEL = os.environ.get("MODEL", "anthropic/claude-sonnet-4-6")
DEFAULT_SKILL_FILE = PROJECT_ROOT / ".claude/skills/paper-to-audio-summary/SKILL.md"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_VOICE = "af_heart"
DEFAULT_SPEED = 1.0


def parse_args():
    parser = argparse.ArgumentParser(description="Convert a scientific paper PDF into a spoken-word audio summary.")
    parser.add_argument("pdf_path", type=str, help="Path to the paper's PDF file.")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="LLM model to use (litellm format).")
    parser.add_argument("--output-dir", type=str, default=str(DEFAULT_OUTPUT_DIR), help="Base output directory.")
    parser.add_argument("--skill-file", type=str, default=str(DEFAULT_SKILL_FILE), help="Path to the skill instructions file.")
    parser.add_argument("--voice", type=str, default=DEFAULT_VOICE, help="Kokoro voice to use.")
    parser.add_argument("--speed", type=float, default=DEFAULT_SPEED, help="Speech speed.")

    return parser.parse_args()


def check_environment_variables():
    api_keys = ["ANTHROPIC_API_KEY", "OPENAI_API_KEY"]
    missing_vars = [var for var in api_keys if var not in os.environ]
    if len(missing_vars) == len(api_keys):
        raise EnvironmentError(f"Must have one of the required environment variables: {', '.join(api_keys)}")


def convert_pdf_to_text(pdf_path: str, output_file: str = None) -> str:
    reader = PdfReader(pdf_path)

    text = ""
    for _, page in enumerate(reader.pages):
        text += page.extract_text()

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as f:
            f.write(text)

    return text


def make_user_input(paper_txt: str, skill_file: str) -> str:
    with open(skill_file, "r") as f:
        skill_content = f.read()

    return f"Skill Instructions:\n{skill_content}\n\nPaper Text: {paper_txt}"


def get_llm_response(
    prompt: str,
    model: str,
    temperature: float = 0.0,
    max_tokens: int = 5000,
) -> str:
    response = litellm.completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def convert_text_to_speech(text: str, voice: str, speed: float, output_file: str = None) -> np.ndarray:
    from kokoro import KPipeline

    pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

    audio_chunks = []
    for sentence in tqdm(sentences, desc="Synthesizing audio", unit="sentence"):
        for _, _, audio in pipeline(sentence, voice=voice, speed=speed):
            audio_chunks.append(audio)

    full_audio = np.concatenate(audio_chunks)

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "wb") as f:
            f.write(full_audio.tobytes())

    return full_audio


def audio_to_mp3(audio_data, sample_rate=24000) -> bytes:
    wav_buffer = io.BytesIO()
    sf.write(wav_buffer, audio_data, sample_rate, format="WAV")
    wav_buffer.seek(0)
    segment = AudioSegment.from_wav(wav_buffer)
    mp3_buffer = io.BytesIO()
    segment.export(mp3_buffer, format="mp3", bitrate="192k")
    mp3_buffer.seek(0)
    return mp3_buffer.getvalue()


def main():
    args = parse_args()
    
    load_dotenv()
    check_environment_variables()

    pdf_path = Path(args.pdf_path)
    output_dir = Path(args.output_dir) / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    paper_txt_file = output_dir / f"{pdf_path.stem}.txt"
    paper_text = convert_pdf_to_text(str(pdf_path), str(paper_txt_file))
    print(f"Saved {paper_txt_file}")

    user_input = make_user_input(paper_text, args.skill_file)

    print(f"Using model: {args.model}")
    response_text = get_llm_response(user_input, model=args.model)

    response_file = output_dir / f"{pdf_path.stem}_summary.txt"
    with open(response_file, "w") as f:
        f.write(response_text)
    print(f"Saved {response_file}")

    full_audio = convert_text_to_speech(response_text, voice=args.voice, speed=args.speed)

    mp3_bytes = audio_to_mp3(full_audio)
    summary_audio_file_mp3 = output_dir / f"{pdf_path.stem}_summary.mp3"
    with open(summary_audio_file_mp3, "wb") as f:
        f.write(mp3_bytes)
    print(f"Saved {summary_audio_file_mp3}")


if __name__ == "__main__":
    main()
