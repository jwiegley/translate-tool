# Standalone Translation Tool Design

## Overview

A self-contained CLI tool for translating Persian/Arabic Baha'i sacred texts into English, producing translations in the elevated register characteristic of Shoghi Effendi's authorized translations. The tool distills 50+ experiments of iterative refinement into a single, direct script.

## User Interface

```
translate input.txt                  # writes input.translated.txt
translate input.docx                 # handles Word documents
translate input.txt -o output.txt    # explicit output path
translate input.txt --base-url http://other:8317/v1
```

- Input: `.txt` (UTF-8) or `.docx` (via python-docx)
- Output: UTF-8 `.txt` file
- Progress: status lines to stderr
- Default endpoint: `http://localhost:8317/v1` (override via `--base-url` or `TRANSLATE_BASE_URL`)
- Default model: `claude-opus-4-6` (override via `--model` or `TRANSLATE_MODEL`)
- Default API key: `dummy-key` (override via `--api-key` or `TRANSLATE_API_KEY`)

## Architecture

Two LLM calls plus a programmatic safety net. No Docker, no Harbor, no Agents SDK.

### Call 1: Translate (temperature 0.3)

System prompt is the proven exp50 prompt containing:
- Shoghi Effendi register guidance (thee/thou, Latinate formality, KJV echoes)
- Concision rules (the most critical stylistic feature per experiments)
- Sentence architecture patterns (subordinate clauses, semicolons, participle phrases)
- Style calibration examples (perfect / too ornate / too literal)
- Persian vs. Arabic language-specific guidance
- Complete mandatory glossary (44 terms embedded in prompt)
- Workflow instructions adapted for standalone use (source text in user message, no file I/O)

User message: the source text only.
Response: the complete translation.

### Call 2: Verify (temperature 0.0)

Checks exactly two things:
1. Paragraph count matches source paragraph count
2. All second-person pronouns are thee/thou/thy/thine (never you/your)

If either error exists, returns corrected text (touching only those two issues). Otherwise returns the translation unchanged.

### Post-processing: Programmatic Paragraph Fix

If paragraph count still doesn't match after verification:
- Too many paragraphs: merge shortest adjacent pairs
- Too few paragraphs: split longest at sentence boundaries

Safety net that rarely fires.

## Key Design Decisions (Experiment-Backed)

| Decision | Rationale | Experiment |
|----------|-----------|------------|
| Two calls, not one | Self-check in single pass is unreliable | exp11-14 |
| Temperature 0.3 for translation | 0.2 too conservative, 0.35 too random | exp16, exp27 |
| Temperature 0.0 for verification | Deterministic structural checks | exp23-25 |
| No revision pass | First-instinct word choices are best; over-revision degrades quality | exp6 |
| Embedded glossary in prompt | Acts as terminology anchor improving stylistic quality even beyond scoring | exp18 |
| Concision as primary style rule | Shoghi Effendi's translations are shorter than most; agents tend to over-expand | exp6-50 |
| Style calibration examples | Concrete good/bad/ugly examples anchor quality better than abstract rules | exp17 |

## File Structure

Single file: `translate.py` in the translate-tool repository root (`~/work/translation/translate-tool/`). The `~/src/scripts/translate` wrapper calls it via `uv run python translate.py "$@"`.

Everything is embedded in the script (system prompt, glossary, calibration examples). No runtime dependency on `scoring/`, `tasks/`, or any benchmark infrastructure.

## Dependencies

- `openai` (available via existing `openai-agents` dependency)
- `python-docx` (already in pyproject.toml)

No new dependencies.

## Error Handling

- Missing/empty input, unsupported file type: exit with error message
- LLM call failure: print error and exit (no retries)
- Empty translation returned: exit with error message
- Verification call failure: skip verification, use raw translation

## What Changes

- `translate.py`: completely rewritten (current version builds Harbor tasks)
- `~/src/scripts/translate`: unchanged (already calls `uv run python translate.py "$@"`)
- `agent.py`: unchanged (continues serving the benchmark harness)

## System Prompt

The system prompt is extracted from agent.py's `SYSTEM_PROMPT` constant (lines 52-212) with one adaptation: the workflow section is simplified to remove file I/O instructions (no `read_file`, no `write_file`, no `/task/instruction.md`). The source text arrives in the user message and the translation is returned directly as the response.

The workflow section becomes:
1. Identify the source language (Arabic or Persian) and count paragraphs
2. Translate the complete text, matching Shoghi Effendi's register
3. Output paragraph count must exactly match source paragraph count
4. Output only the translation, no notes or commentary
