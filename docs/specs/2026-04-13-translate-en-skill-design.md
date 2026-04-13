# Translate-EN Claude Code Skill Design

## Overview

A Claude Code skill for high-quality Arabic/Persian-to-English translation of Baha'i sacred texts, producing translations in the elevated register characteristic of Shoghi Effendi's authorized translations. The skill employs a Lead Translator orchestrating a 6-member specialist review team across two review rounds, mirroring the architecture of the existing Persian translation skill.

This skill is the primary translation interface for in-depth, high-quality work. A standalone CLI tool (`translate.py`) provides a quick-draft option using a simpler two-pass pipeline.

All project files will live in a new Git repository at `~/work/translation/translate-tool`.

**Note:** The earlier CLI tool spec (`2026-04-12-translate-tool-design.md`) references `translate.py` in the autoagent project root. This spec supersedes that: all project files move to `~/work/translation/translate-tool`. The CLI tool spec will be updated during implementation.

## Section 1: Skill Structure

The skill lives at `~/.claude/skills/translate-en/SKILL.md` with a companion `GLOSSARY.csv`.

- **SKILL.md**: Contains the Lead Translator system prompt (adapted from the proven exp50 prompt), the 7-phase workflow, reviewer mandates, conflict resolution rules, and glossary reference.
- **GLOSSARY.csv**: Mandatory terminology mapping (44 terms). Symlinked from the main repo to avoid duplication.

The standalone CLI tool (`translate.py`) remains available for quick drafts. The skill and CLI tool share the same glossary and core translation guidance but differ in review depth:

| Aspect | CLI (`translate.py`) | Skill (`translate-en`) |
|--------|---------------------|----------------------|
| Review depth | 1 LLM verify pass | 2 rounds of 6-reviewer team |
| Latency | ~10-30 seconds | ~2-5 minutes |
| Use case | Quick drafts, iteration | Final-quality translations |
| Invocation | `translate FILE` | `/translate-en FILE` in Claude Code |

## Section 2: Lead Translator Role & Workflow

The Lead Translator is the orchestrating agent, using the exp50 system prompt as its foundation. It follows a 7-phase workflow mirroring the Persian translation skill:

### Phase 1: Preparation
- Read the source file (`.txt` or `.docx`)
- Identify source language (Arabic or Persian)
- Count paragraphs
- Load glossary terms
- For Arabic: expect terse, commanding style; translate with short, powerful sentences
- For Persian: expect flowing prose; translate with semicolon-linked balanced clauses, maintaining density

### Phase 2: Initial Draft
- Translate the complete text using the exp50 system prompt guidance
- Temperature 0.3 (experimentally validated as optimal)
- Trust first instinct for word choices (exp6 finding: over-revision degrades quality)
- Output paragraph count must match source paragraph count

### Phase 3: First Team Review
- Dispatch all 6 reviewers in parallel via Claude Code Agent tool (hub-and-spoke, not mesh)
- Reviewers use the same model as the Lead Translator (inherited from Claude Code session)
- Each reviewer receives: source text, draft translation, their specific mandate (defined inline in SKILL.md)
- Each reviewer returns: specific line-level feedback within their domain only

### Phase 4: First Synthesis
- Lead Translator reads all 6 reviews
- Applies conflict resolution priority to adjudicate disagreements
- Produces revised translation incorporating accepted feedback
- Documents which feedback was accepted/rejected and why

### Phase 5: Second Team Review
- Dispatch all 6 reviewers again with the revised translation
- Reviewers check whether their previous concerns were addressed
- Reviewers may raise new issues visible only after revision

### Phase 6: Final Synthesis
- Lead Translator performs final integration
- Verifies: paragraph count matches, all pronouns are thee/thou/thy/thine, glossary terms correct
- Programmatic paragraph count fix as safety net (rarely fires)

### Phase 7: Delivery
- Write the final translation to the output file
- Report completion with brief quality notes

## Section 3: Six Reviewer Mandates

All 6 reviewers are retained from the Persian skill architecture, with mandates adapted for Arabic/Persian-to-English translation:

### 1. Diction & Grammar (`diction-grammar`)
- Word precision: is each English word the best match for the source?
- Archaic form consistency: thee/thou/thy/thine throughout, correct verb conjugations (hath, doth, shalt, canst, mayest, wilt, behooveth)
- Tense and mood accuracy
- No modern English intrusions

### 2. Beauty & Eloquence (`beauty-eloquence`)
- Literary quality: does it read as elevated sacred literature?
- Latinate formality and King James resonance
- Rhetorical power: parallelism, rhythm, cadence
- Sentence architecture: subordinate clauses, semicolons as rhythmic pivots, participle phrases
- Avoids overwrought or purple prose (the "too ornate" failure mode)

### 3. Clarity & Accessibility (`clarity-accessibility`)
- Elevated but comprehensible: a thoughtful reader should follow the meaning
- Catches over-expansion (the most critical failure mode per experiments)
- Flags unnecessarily complex constructions
- Ensures interpretive additions clarify rather than obscure

### 4. Shoghi Effendi Conventions (`se-conventions`)
- Glossary term compliance: all 44 mandatory terms used correctly
- Transliteration accuracy (Baha'i diacriticals)
- Known phrasings: where SE translated the same passage, match his choices
- Structural patterns: SE's characteristic concision, his compression techniques

### 5. Back-Translator (`back-translator`)
- Back-translates the English into the source language (Arabic or Persian)
- Compares back-translation against original source
- Flags semantic drift: meaning lost, added, or distorted
- This is the primary semantic fidelity check

### 6. Oral & Spiritual Quality (`oral-spiritual`)
- Read-aloud fluidity: does it flow when spoken?
- Spiritual potency: does it convey the weight and authority of sacred scripture?
- Cadence and rhythm at the sentence and paragraph level
- Cumulative impact: does the whole passage build appropriately?

### Conflict Resolution Priority

When reviewers disagree, the Lead Translator resolves using this hierarchy:

1. **Meaning fidelity** (back-translator concerns override all)
2. **Terminology** (glossary compliance is non-negotiable)
3. **Grammar** (correctness over style)
4. **Oral/spiritual quality** (sacred literature must read well aloud)
5. **Register/style** (Shoghi Effendi's elevated register)
6. **Clarity** (comprehensibility — ranked below oral/spiritual because the clarity reviewer's over-expansion concerns are addressed structurally via the concision rules in the system prompt; in conflict resolution, oral quality of sacred text takes precedence over simplification)
7. **Aesthetic preferences** (lowest priority — subjective beauty calls yield to all above)

## Section 4: Repository Structure

A new Git repository at `~/work/translation/translate-tool`:

```
translate-tool/
├── translate.py              # Standalone CLI tool (quick drafts)
├── pyproject.toml            # Dependencies: openai, python-docx
├── tests/
│   └── test_translate.py     # Unit and integration tests
├── glossary.csv              # Mandatory terminology (shared by CLI + skill)
├── docs/
│   └── specs/                # Design specs
│       └── 2026-04-12-translate-tool-design.md
│       └── 2026-04-13-translate-en-skill-design.md
└── program.md                # Translation optimization directive
```

The Claude Code skill lives outside this repo:

```
~/.claude/skills/translate-en/
├── SKILL.md                  # Skill definition
└── GLOSSARY.csv              # Symlink → ~/work/translation/translate-tool/glossary.csv
```

Key decisions:
- **Single-source glossary**: Lives in the repo, symlinked into the skill directory.
- **`~/src/scripts/translate`** wrapper updated to point to `~/work/translation/translate-tool`.
- **No autoagent dependency**: The new repo is fully self-contained. `agent.py` and the Harbor benchmark remain in autoagent.
- **Skill can invoke translate.py** for the quick-draft path; orchestrates via Claude Code's TeamCreate/Agent tools for the full team review path.

## Section 5: Error Handling & Edge Cases

### CLI tool (`translate.py`)
Already implemented and tested:
- Missing/empty input: exit with error message
- Unsupported file type: exit with error message
- LLM call failure: exit with error message (no retries)
- Empty translation: exit with error message
- Verification failure: skip verification, use raw translation

### Claude Code skill (`translate-en`)
- **Reviewer disagreement**: Lead Translator uses conflict resolution priority. No voting — the Lead decides.
- **Very short input** (< 1 sentence): Skip team review, translate directly. Overhead of 6 reviewers not justified for a single phrase.
- **Very long input** (> ~2000 source-text words): Lead Translator segments into natural sections (chapter breaks, paragraph groups), translates each segment with full team review, then assembles. The 2000-word threshold is a guideline; the Lead uses judgment based on natural section boundaries.
- **Reviewer returns no feedback**: Treated as approval — no changes needed from that reviewer's perspective.
- **LLM endpoint down**: Skill reports the error clearly. No silent fallback.
- **Mixed language input** (Arabic + Persian in same document): Lead Translator identifies language per section, adjusts style guidance accordingly (terse for Arabic, flowing for Persian).

## Key Design Decisions (Experiment-Backed)

| Decision | Rationale | Source |
|----------|-----------|--------|
| Two review rounds, not one | First round catches issues, second verifies fixes and catches emergent problems | Persian skill architecture |
| Hub-and-spoke, not mesh | Reviewers don't need to coordinate; Lead synthesizes | Reduces complexity, faster parallel dispatch |
| Temperature 0.3 for translation | 0.2 too conservative, 0.35 too random | exp16, exp27 |
| Trust first instinct | Over-revision degrades quality | exp6 |
| Embedded glossary is load-bearing | Improves stylistic quality even beyond terminology scoring | exp18 |
| Concision as primary style rule | SE's translations are shorter than most; LLMs tend to over-expand | exp6-50 |
| Style calibration examples | Concrete good/bad examples anchor quality better than abstract rules | exp17 |
| 6 reviewers retained | User preference; each covers a distinct quality dimension | Persian skill precedent |
| Conflict resolution hierarchy | Meaning fidelity > terminology > grammar > oral > style > clarity > aesthetics | Principled prioritization |
