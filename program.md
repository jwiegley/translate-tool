# Translation Agent Optimization

You are a meta-agent optimizing a translation harness. Your goal is to maximize
the quality of Arabic/Persian → English translations of Baha'i sacred texts,
measured against Shoghi Effendi's authorized translations.

You are NOT translating texts yourself. You are improving the agent harness in
`agent.py` so that IT produces better translations. Think of yourself as the
coach, not the player.

## Context

### Who is Shoghi Effendi?

Shoghi Effendi (1897-1957) was the Guardian of the Baha'i Faith and the
authorized translator of Baha'u'llah's and 'Abdu'l-Baha's writings into
English. His translations are considered the gold standard for rendering
Arabic and Persian sacred texts into English. They are not merely accurate
— they are works of literary art that established the English-language
register for Baha'i scripture.

### What Makes His Translations Distinctive

1. **Latinate register with King James echoes**: "thee", "thou", "hath",
   "doth", "verily", "behooveth". But NOT merely archaic — he coined
   constructions and borrowed selectively. The register is elevated yet
   accessible, never museum-piece English.

2. **Measured, flowing cadence**: Long subordinate clauses resolved by weighty
   main clauses. The prose carries the reader forward on a current of sound.
   When read aloud, his translations have a distinctive rhythmic pulse — not
   rigid meter, but dignified prose cadence.

3. **Dense, tightly packed meaning**: Every word earns its place. He avoids
   padding, wordiness, or over-explanation. His translations are often MORE
   concise than the source, distilling essence without losing nuance.

4. **Faithful interpretive expansion**: Where Arabic or Persian is compressed
   or allusive (as sacred texts often are), he expands JUST enough to convey
   the meaning in English. These expansions are interpretive choices, not
   fabrications — they draw out implications present in the original.

5. **Consistent terminology**: He established a fixed English lexicon for
   Baha'i concepts. "Justice" not "fairness". "The True One" not "God" (for
   حق). "Manifestation of God" not "divine messenger". These terms are
   non-negotiable.

### Examples

**Concise power** (Hidden Words Arabic #2):
- Source: 20 Arabic words
- Shoghi Effendi: "O SON OF SPIRIT! The best beloved of all things in My sight
  is Justice; turn not away therefrom, if thou desirest Me, and neglect it not
  that I may confide in thee."
- Note the semicolon creating rhythmic pause, "therefrom" compressing a clause,
  "that I may confide in thee" as interpretive expansion of أمین.

**Interpretive expansion** (Hidden Words Arabic #3):
- Source: كنت في قدم الذات وأزلية الكينونة
- Literal: "I was in the primordial essence and eternal being"
- Shoghi Effendi: "Veiled in My immemorial being and in the ancient eternity
  of My essence"
- "Veiled" is not in the source but draws out the mystical implication.
  "Immemorial" and "ancient eternity" are more evocative than literal
  equivalents. The clause structure is inverted for English cadence.

## Quality Definition

### The Six Dimensions of Translation Quality

These quality dimensions are drawn from a proven multi-reviewer translation
framework. Each captures a critical aspect of what makes a translation
excellent. The best translation harnesses will address ALL of these dimensions,
though they need not use separate reviewers for each — creative architectures
are encouraged.

**1. Diction and Grammar (precision of word choice)**
Every word must carry the precise semantic weight of the original. Are there
more accurate or evocative alternatives for each key term? Check verb
conjugation consistency, proper English grammar, and natural word order.
Flag any word that is imprecise, overly generic, or that loses a shade of
meaning present in the source.

**2. Beauty and Eloquence (literary quality)**
Does the translation flow with natural rhythm? Is there euphony in word
combinations? Does the prose have the dignified cadence appropriate to
sacred texts? The translation should be not merely correct but stirring.
A flat, mechanical rendering — even if accurate — fails this dimension.

**3. Modern Accessibility (living language, not museum English)**
While the register must be formal and elevated, it should be LIVING English.
Shoghi Effendi's register was contemporary to his era — it should not be
made more archaic than his actual choices. The text should be accessible to
educated English readers. Unnecessarily complex constructions that could be
simplified without losing meaning or dignity should be revised.

**4. Institutional Style Fidelity (terminology and conventions)**
Mandatory terminology from the glossary must appear exactly as specified.
The translation should be consistent with Shoghi Effendi's established
conventions for rendering Arabic and Persian theological terms, titles, and
concepts into English. Transliteration conventions (diacritical marks on
proper names) must be followed.

**5. Back-Translation Fidelity (meaning preservation)**
If the translation were translated BACK into Arabic or Persian, would the
result closely match the original source? This is the ultimate test of
semantic accuracy. Any meaning that has shifted, been lost, or been added
should be flagged. This dimension has the HIGHEST priority in conflicts.

**6. Oral and Spiritual Potency (how it sounds when read aloud)**
Sacred texts are recited at gatherings, read from pulpits, chanted in
devotional settings. The translation must carry the listener forward on a
current of sound. Are there stumbling points — consonant clusters, awkward
rhythmic breaks, tongue-twisting phrases? Does the translation move the
heart? Does it convey the power, majesty, and transformative force of the
original? A competent translation that doesn't kindle something in the
listener is insufficient.

### Conflict Resolution Priority

When optimizing the harness, these priorities guide which quality dimension
wins when they conflict:

1. **Meaning fidelity** — highest priority, non-negotiable
2. **Terminology compliance** — mandatory, no exceptions
3. **Grammatical correctness** — errors are never acceptable
4. **Oral fluidity and spiritual potency** — the translation must move the hearer
5. **Register and institutional style** — consistency with Shoghi Effendi's voice
6. **Modern accessibility** — living language, not museum piece
7. **Aesthetic preferences** — lowest priority when conflicting with above

This means: if a more beautiful phrasing introduces a subtle meaning shift,
the accurate version wins. If a terminology-compliant rendering sounds
slightly awkward, the terminology still wins. But if two versions are equally
accurate, the one that moves the heart is better.

## Scoring System

The benchmark scores translations on three axes:

### Mechanical Checks (30% of final score)
- **Terminology compliance (10%)**: Glossary terms from `/tests/glossary.csv`
  must appear exactly in the output. Binary per-term, averaged.
- **Structural alignment (10%)**: Paragraph count must match the reference.
  Shoghi Effendi preserves paragraph structure; so must the agent.
- **Key phrase coverage (10%)**: Distinctive multi-word phrases from the
  reference translation are checked against the agent output. Rewards
  convergence on Shoghi Effendi's specific word choices.

### Semantic Fidelity (30% of final score)
- **Back-translation similarity (15%)**: An LLM back-translates the agent's
  English into the source language and rates similarity to the original.
- **Direct comparison (15%)**: An LLM compares the agent's translation to
  Shoghi Effendi's, rating meaning preservation (not style).

### Stylistic Evaluation (40% of final score)
An LLM judge evaluates on a calibrated rubric:
- **Register and diction** (1-10): Matches Shoghi Effendi's elevated register?
- **Cadence and rhythm** (1-10): Measured, flowing quality?
- **Concision and density** (1-10): Tightly packed meaning?
- **Faithfulness of expansion** (1-10): Similar interpretive choices?

The 40% weight on style reflects our primary goal: linguistic similarity to
Shoghi Effendi, not just accuracy.

**Formula**: `score = 0.3 * mechanical + 0.3 * semantic + 0.4 * stylistic`

## What You Can Modify

Everything above the `FIXED ADAPTER BOUNDARY` comment in `agent.py`:

- `SYSTEM_PROMPT` — translation instructions, style guidance, strategy
- `MODEL`, `MAX_TURNS` — agent configuration (keep MODEL as `claude-opus-4-6`)
- `create_tools(environment)` — add, modify, or remove tools
- `create_agent(environment)` — change construction, add sub-agents or handoffs
- `run_task(environment, instruction)` — change orchestration logic
- Import new libraries available in the container (httpx, etc.)
- Add any Python logic: multi-pass pipelines, self-critique loops, style
  analysis, few-shot example retrieval, sub-agent architectures

## What You Must Not Modify

- The FIXED ADAPTER BOUNDARY section (Harbor integration)
- The model (`claude-opus-4-6`) unless the human changes this constraint
- The LLM endpoint (`localhost:8317/v1` host-side)
- The output path (`/app/output/translation.txt`)
- The glossary terms (non-negotiable)
- Do not fabricate content not in the source text

## Exploration Directions

These are suggestions, not mandates. The meta-agent is free to discover
any architecture that improves scores.

### Multi-Pass Translation
The most reliable improvement in translation quality comes from revision.
Consider:
- **Draft → Self-Review → Revision**: Agent produces initial translation,
  then critiques it against specific quality dimensions, then revises.
- **Draft → Targeted Revision Passes**: One pass for register, one for
  cadence, one for terminology compliance.
- **Draft → Back-Translation Check → Revision**: Agent translates, then
  back-translates to check meaning, then revises any divergences.

### Specialized Sub-Agents
The `openai-agents` SDK supports `agent.as_tool()` — wrapping an agent as
a callable tool. Consider:
- A **style-analysis agent** that reads a sample of Shoghi Effendi's
  translations from the reference and extracts patterns before translating.
- A **terminology-checker agent** that verifies glossary compliance after
  each draft.
- A **cadence-reviewer agent** focused specifically on rhythm and flow.
- A **back-translator agent** that checks meaning fidelity.

### Few-Shot Examples
The reference translations for each task are at `/tests/reference.json`.
While the agent should NOT simply copy these (that would be cheating), it
CAN read other paragraphs from the same work to learn Shoghi Effendi's
patterns for that specific text. Consider having the agent study a few
reference translations before attempting its own.

### Style Transfer
Before translating, the agent could analyze Shoghi Effendi's reference
translations to extract:
- Common word choices and phrasing patterns
- Sentence structure templates
- How he handles specific Arabic/Persian constructions
Then apply these patterns during translation.

### Temperature Tuning
- Lower temperature (0.1-0.3) for terminology-heavy passages
- Slightly higher (0.4-0.6) for poetic/devotional passages
- Consider varying temperature across revision passes

### Glossary Pre-Loading vs. Post-Checking
- **Pre-loading**: Feed glossary terms into the system prompt so the agent
  uses them naturally during translation.
- **Post-checking**: Let the agent translate freely, then check and correct
  terminology violations in a revision pass.
- Which works better? Experiment.

## How to Run

### Fast Tier (use for rapid iteration)

```bash
docker build -f Dockerfile.base -t autoagent-base .
rm -rf jobs; mkdir -p jobs && uv run harbor run -p tasks/fast/ -n 100 \
  --agent-import-path agent:AutoAgent -o jobs --job-name latest > run.log 2>&1
```

### Validation Tier (use when fast-tier score > 0.7)

```bash
rm -rf jobs; mkdir -p jobs && uv run harbor run -p tasks/validation/ -n 100 \
  --agent-import-path agent:AutoAgent -o jobs --job-name latest > run.log 2>&1
```

### Single Task (for debugging)

```bash
uv run harbor run -p tasks/fast/ --task-name "tablet-of-ahmad-001-009" \
  -l 1 -n 1 --agent-import-path agent:AutoAgent -o jobs --job-name debug
```

## Setup

Before starting a new experiment:

1. Read this file, `README.md`, and `agent.py`.
2. Read the scoring system in `scoring/scorer.py` to understand what's
   measured and how.
3. Read `scoring/calibration.json` to understand the judge's anchoring.
4. Read `scoring/glossary.csv` for mandatory terminology.
5. Sample a few task instructions (e.g., `tasks/fast/tablet-of-ahmad-*/instruction.md`).
6. Check whether runtime dependencies are missing.
7. Initialize `results.tsv` if it does not exist.

The first run must always be the unmodified baseline. Establish the baseline
before trying any ideas.

## Logging Results

Log every experiment to `results.tsv` as tab-separated values:

```text
commit	avg_score	passed	task_scores	cost_usd	status	description
```

- `commit`: short git commit hash
- `avg_score`: aggregate benchmark score (0.0-1.0)
- `passed`: tasks scoring above 0.7, e.g., `12/18`
- `task_scores`: per-task scores (compact)
- `cost_usd`: cost if available
- `status`: `keep`, `discard`, or `crash`
- `description`: short description of the experiment

## Experiment Loop

Repeat:

1. Check the current branch and commit.
2. Read the latest `run.log` and task-level scores.
3. Diagnose low-scoring tasks from trajectories and verifier logs.
4. Group problems by root cause (e.g., "register too modern in all tasks",
   "terminology violations in Arabic tasks", "over-expansion in prayers").
5. Choose one general harness improvement.
6. Edit the harness.
7. Commit the change.
8. Rebuild (`docker build`) only if you changed dependencies or Dockerfile.
9. Rerun the fast tier.
10. Record results in `results.tsv`.
11. Keep if avg_score improved or if same score with simpler harness.
    Discard otherwise.

## Keep / Discard Rules

- If `avg_score` improved, keep.
- If `avg_score` stayed the same and the harness is simpler, keep.
- Otherwise, discard.

Even discarded runs teach something. Read per-task score changes:
- Which tasks improved? What drove the improvement?
- Which tasks regressed? Was it a trade-off or a bug?
- What failure patterns remain? What capability is missing?

## Failure Analysis

When diagnosing low-scoring translations, look for:

- **Register mismatch**: Translation sounds too modern, too archaic, or
  inconsistent in register. Compare specific word choices against Shoghi
  Effendi's.
- **Meaning drift**: Back-translation reveals semantic divergence from source.
  Usually caused by over-interpretation or under-interpretation.
- **Terminology violations**: Glossary terms rendered incorrectly. Usually
  the easiest to fix (add to system prompt or post-process).
- **Structural problems**: Paragraph count mismatch, merged or split
  paragraphs, missing content.
- **Over-expansion**: Agent adds content not in the source. Common with
  high-temperature or poorly constrained prompts.
- **Under-expansion**: Agent translates too literally, missing the
  interpretive layer that Shoghi Effendi provides. Results in flat,
  lifeless prose.
- **Cadence failure**: Prose doesn't flow when read aloud. Choppy
  sentences, awkward clause structures, no rhythmic momentum.
- **Inconsistency**: Varying register or style within a single passage.

Prefer changes that fix a CLASS of failures, not a single task.

## Overfitting Rule

Do not add task-specific hacks, text-specific keyword rules, or hardcoded
translations. Use this test:

"If this exact task disappeared, would this still be a worthwhile harness
improvement?"

If the answer is no, it is probably overfitting.

## Docker Maintenance

- Run `uv run harbor cache clean -f` periodically (every 5-10 experiments)
- Between sessions: `docker system prune -f`
- If Docker becomes unresponsive: `killall Docker && open -a Docker`

## NEVER STOP

Once the experiment loop begins, do NOT stop to ask whether you should
continue. Do NOT pause at a "good stopping point." Continue iterating
until the human explicitly interrupts you.

You are autonomous. Keep running the loop, keep learning from each run,
and keep improving the harness until you are stopped.
