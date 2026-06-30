---
name: paper-to-audio-summary
description: 'Convert a scientific paper into a 15-minute entertaining and informative summary optimized for audio. Use when you need a spoken-only, audience-aware overview of a paper for audio narration.'
---

# Paper to Audio Summary

## When to Use
- You are turning a scientific paper into a narrated audio segment.
- You want a summary that is engaging, accurate, and tailored for an expert audience.
- The output will be read aloud directly, so it must sound natural when spoken.

## Goal
Create a 15-minute audio script that explains the paper clearly and vividly for a listener with a strong background in histopathology machine learning who wants to learn more about cancer immunobiology.

## Output Format — Critical
- Return the narration script and nothing else.
- Do not include any preamble, notes, headers, labels, or commentary before or after the script.
- Do not include stage directions, section labels, or any text that would not be spoken aloud by the narrator.
- The very first word of your response must be the first spoken word of the script.
- The very last word of your response must be the last spoken word of the script.

## Core Requirements
- Open by stating the full title of the paper exactly as it appears, followed immediately by introducing the authors.
- Introduce the first author and the corresponding author by name, mention their institutional affiliations, and briefly note what kind of lab or research group they come from.
- If the first author and corresponding author are the same person, say so.
- Write only text that is meant to be spoken.
- Keep the tone entertaining, informative, and conversational.
- Make the piece feel like a strong audio narration, not a written paper summary.
- Aim for roughly 15 minutes of listening time, which is usually about 1800 to 2200 words.

## Audience and Voice
- Assume the listener is technically sophisticated and already comfortable with machine learning concepts.
- They want depth, not oversimplification.
- Use a confident, lively, story-driven narration style.
- Explain advanced ideas clearly without becoming dry or overly academic.

## Content Priorities
1. Start with the paper title and authors.
2. Introduce the central question or problem the paper is addressing.
3. Explain the biological context in a way that helps the listener understand why the work matters.
4. If the paper discusses immune cell subtypes, spend extra time explaining what those cells do in the immune system and why they matter.
5. If the paper uses machine learning models, translate them into simple language while still allowing room for technical detail.
6. End by explaining the broader significance of the work and why it matters for cancer immunobiology.

## Structure for the Script
Use this sequence unless the paper strongly suggests a different flow:

1. Opening hook
   - State the full paper title exactly as written.
   - Introduce the first author and corresponding author by name, their affiliations, and what kind of research group they represent.
   - Briefly frame the topic and why it matters.

2. The biological problem
   - Explain the scientific question in plain but precise terms.
   - Give enough background that the listener can follow without needing the paper itself.

3. What the paper actually did
   - Describe the main methods, datasets, or experimental design.
   - If relevant, explain the machine learning approach in accessible language.
   - Keep the explanation focused on what the model was trying to learn and why.

4. Key findings
   - Summarize the main results in a way that feels vivid and memorable.
   - Highlight any surprising or important observations.

5. Immune biology emphasis
   - When immune cells are involved, explain their roles clearly.
   - Emphasize how these cells shape inflammation, tumor control, immune evasion, or tissue remodeling.
   - Help the listener understand the biology, not just the model output.

6. Why the work matters
   - Close with the bigger picture.
   - Explain what the paper adds to the field and what might come next.

## Style Rules
- Write in full sentences and natural spoken rhythm.
- Prefer conversational phrasing over formal academic wording.
- Avoid bullet points, citations, or dense reference formatting.
- Avoid stage directions like “pause” or “laughs.”
- Do not include text that would only make sense on a page.
- Keep the language vivid enough to be entertaining while remaining precise.

## Technical Explanation Rules
- If a machine learning model is described, explain it in simple terms first.
- Then add enough technical detail for an expert audience to appreciate the approach.
- For example, explain whether the model is classifying, predicting, embedding, clustering, or estimating a biological signal.
- If the model is a neural network, transformer, graph model, or survival model, briefly explain what that means in practical terms.

## Quality Check
Before finishing, confirm that:
- The response contains only the spoken script — no headers, labels, preamble, or closing notes.
- The full paper title appears first, stated exactly as written.
- The first author and corresponding author are both introduced by name with their affiliations.
- The script is written as spoken text only.
- The tone is entertaining and informative.
- The audience is treated as technically capable but curious.
- Immune cell roles are explained clearly when relevant.
- Machine learning methods are translated into understandable language.
- The script feels like it could be read aloud for a full 15-minute segment.
