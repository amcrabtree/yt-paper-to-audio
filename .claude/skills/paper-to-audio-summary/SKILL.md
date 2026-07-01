---
name: paper-to-audio-summary
description: >
  Converts text extracted from a scientific paper into a polished, spoken-word-only audio script
  optimized for ~15 minutes of narration. Use this skill whenever the user provides paper text (or a
  PDF, abstract, or extracted content) and asks for a script, audio summary, narrated summary,
  podcast-style breakdown, or spoken version of a paper. Also trigger when the user says things like
  "turn this paper into audio", "write a script for this paper", "make this paper listenable", or
  "summarize this for a podcast". The audience is a researcher with strong ML and histopathology
  expertise who wants to build intuition in cancer immunobiology. Output is ONLY spoken words — no
  stage directions, no section headers, no bracketed notes. The narrator opens with the paper's full
  title and introduces the authors.
---

# Paper-to-Audio Script

Convert a scientific paper into a ~15-minute engaging, informative spoken-word audio script.

## Core Constraints

- **Output is spoken words only.** No headers, no stage directions, no "[pause]", no bracketed notes, no markdown formatting. Every character in the output will be read aloud by a narrator.
- **Target length**: ~2,000–2,400 words (roughly 15 minutes at a natural narration pace of ~140 wpm).
- **Opening line**: Always begin with: `"Today's paper is called..."` followed by the full title, then introduce the first author, corresponding author (if different), and their affiliations.
- **No jargon without grounding**: Technical terms are fine but must be grounded in plain language on first use.

## Audience Profile

The listener has:
- Strong ML background: familiar with CNNs, transformers, attention mechanisms, training pipelines, evaluation metrics, weakly supervised learning, etc. Go deep on models — don't oversimplify.
- Strong histopathology background: comfortable with H&E, IHC, tissue morphology, spatial concepts.
- **Building expertise in cancer immunobiology.** This is the gap to fill. Prioritize:
  - What each immune cell type *does* in the immune system before explaining its role in the paper
  - Why the tumor microenvironment (TME) matters conceptually
  - What the biological findings *mean*, not just what they are

## Script Structure

Follow this arc. Do not label sections — just flow naturally between them.

### 1. Hook (30–60 seconds)
Open with the title and authors, then immediately establish *why this paper matters*. What problem does it solve? What was unknown or broken before? Make it feel consequential.

### 2. Biological Context (2–3 minutes)
Lay the groundwork any listener needs before the paper makes sense. Cover:
- The disease or biological system studied
- Key immune cell types involved — for **each cell type**, briefly explain its canonical role in the immune system (e.g., "CD8+ T cells, also called cytotoxic T cells, are the immune system's assassins — they're trained to recognize and kill cells that display foreign or abnormal proteins on their surface") before explaining its role in the paper
- The tumor microenvironment if relevant: explain it as a complex ecosystem where cancer cells, immune cells, and stromal cells are in constant negotiation

### 3. The Research Question (1 minute)
State clearly what the authors set out to learn or build. One crisp question or hypothesis.

### 4. Methods (3–4 minutes)
Walk through what was done: cohorts, data, experimental design, and any computational models. For **ML models**:
- Name the architecture and explain how it works at an intuitive level (e.g., "a multiple-instance learning model treats each patient's slide as a bag of tiles, and learns which tiles are most predictive of the outcome — without ever being told which region matters")
- Mention key design choices: loss functions, supervision strategy, input modalities
- Explain evaluation strategy: what metrics, what baselines, what held-out sets

### 5. Results (3–4 minutes)
Walk through the key findings in order of importance. Use concrete numbers when they're compelling ("improved AUC from 0.71 to 0.84"). Translate statistical language into plain meaning. If the paper has multiple experiments, prioritize the ones that most directly answer the research question.

### 6. Biological Meaning (2 minutes)
Step back from the numbers. What do these results tell us about biology? If immune subtypes are involved, explain what it *means* that a certain cell type was enriched, depleted, or predictive. Connect results to known biology where possible.

### 7. Limitations and Open Questions (1 minute)
Be honest about what the paper doesn't prove. What cohorts might not generalize? What's still unknown? What's the next logical experiment?

### 8. Takeaway (30–60 seconds)
End with a memorable synthesis. What should the listener carry with them? What does this paper change about how we think about the problem?

## Tone and Style

- **Conversational but precise**: like a knowledgeable friend explaining a paper over coffee, not a textbook being read aloud
- **Active voice**: prefer "the model learned to..." over "it was found that..."
- **Analogies welcome**: use them to build intuition, especially for immunobiology concepts the audience is still developing
- **No fluff**: skip filler phrases like "This is a fascinating paper..." — just get into it
- **Transitions**: use spoken transitions between topics ("With that context in mind...", "Now here's where things get interesting...", "So what did they actually find?")

## Special Handling

**Immune cell types**: Every named immune cell gets a one-sentence role description on first mention. Examples:
- Macrophages: "macrophages are the immune system's janitors and sentinels — they engulf debris and dead cells, but also coordinate inflammation and can either attack tumors or be co-opted to protect them"
- Tregs: "regulatory T cells, or Tregs, act as the immune system's brakes — they suppress other immune cells to prevent autoimmunity, but in tumors, they often end up suppressing the very cells that should be attacking the cancer"
- NK cells: "natural killer cells are innate immune sentinels that don't need prior training to recognize and destroy abnormal cells — they're a first line of defense before the adaptive immune system has time to respond"

**ML models**: Explain architecture, training supervision, and key design decisions. Use analogies. Assume the listener can handle precision — e.g., "they used a transformer encoder to generate patch-level embeddings, then aggregated across the slide using attention-based pooling, which lets the model highlight the patches it found most informative."

**Missing information**: If the extracted text is incomplete (e.g., methods are truncated, author affiliations are missing), write around it naturally without calling attention to the gap. Do not say "the paper doesn't mention..." — just omit that element.

## Output Format

Begin the script immediately — no preamble, no explanation, no metadata. Just the spoken words.

Start with: `Today's paper is called...`

End with a natural closing sentence. No sign-off, no "thanks for listening."