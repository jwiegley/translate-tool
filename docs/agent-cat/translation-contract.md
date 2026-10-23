# Native English translation contract

## Authority and evidence

This contract derives from the current translate-tool worktree at revision
`bffdb7ba3e5db603ea1390fee555354c1d45d642`. It governs the replacement of the minimal
`translate-en` workflow in agent-workflows, not a revision of that workflow's
abbreviated interpretation of another translation direction.

The current thorough procedure is `skill/SKILL.md`, supported by
`docs/specs/2026-04-13-translate-en-skill-design.md`. The standalone `translate.py`
and its earlier design specify a quick-draft interface. They supply developed
translation guidance and experiment conclusions, but their two-call execution
shape does not replace the thorough procedure.

The local Git history starts with the standalone tool and then introduces the
shared glossary and review skill. It contains no raw exp6–exp50 trajectories,
benchmark scores, or experimental corpus. References to those experiments below
are attributed design-record conclusions, not independently reproduced results.
`program.md` is an earlier benchmark-optimization directive. Its quality dimensions
remain relevant, while its Harbor adapter, Docker commands, fixed endpoint/output
path, benchmark-reference access, and indefinite experiment loop do not govern
this production workflow. `RESUME.md` is an existing deployment handoff and remains
unchanged.

## Requirements and implementation allocation

The implementation column identifies the owning layer. Entries describe required
behavior, not completed verification. Completion evidence belongs beside the
corresponding tests and acceptance results.

| ID | Requirement and authoritative source | Classification | Implementation and evidence required |
| --- | --- | --- | --- |
| T01 | Register, vocabulary, grammar, sentence architecture, interpretive restraint, and separate Arabic/Persian treatment (`translate.py:SYSTEM_PROMPT`, skill register sections) | Developed prompt guidance | Versioned workflow prompt assets, consumed by draft and synthesis stages. Tests check inclusion and reviewer access. |
| T02 | Concision, first-instinct choices, good/ornate/literal calibration, and glossary anchoring (CLI design, experiment decision table) | Experiment conclusions reported by the design record | Preserve guidance and calibration text without unsupported numerical claims. Reviews justify necessary changes rather than paraphrasing satisfactory text. |
| T03 | Draft temperature 0.3, mechanical verification temperature 0.0, and selected model (CLI and both specifications) | Reported experimental configuration | Use existing symbolic routing and supported generation options. Document actual settings and unsupported adapter controls. Never imply a prose instruction configures temperature. |
| T04 | Source reading, language identification, paragraph count, and relevant terminology brief (skill phase 1) | Current thorough procedure | Deterministic preparation helper plus explicit model preparation stage. Relevant terms retain glossary notes and source locations. Full glossary remains available to the conventions reviewer. |
| T05 | Initial complete translation, one output paragraph per source paragraph, no commentary inside translation (skill phase 2) | Current thorough procedure | Calibrated draft with stable source-unit identifiers and an explicitly validated response shape. |
| T06 | Diction/grammar, beauty/eloquence, clarity/accessibility, conventions/terminology, back-translation fidelity, oral/spiritual review (skill phase 3 and reviewer mandates) | Current thorough procedure | Six named native text-panel seats. Preserve all responses, locations, proposed changes, reasons, ratings, and explicit no-issue findings. Tests inspect actual prompts and data flow. |
| T07 | Independent reverse translation followed by comparison with the source (back-translator mandate) | Current thorough procedure | A separate back-translation call receives only the English candidate and language metadata. The subsequent fidelity review receives the original and that back-translation. Do not rely on asking a model to ignore source text already in its prompt. |
| T08 | First synthesis, second complete review round, final synthesis (skill phases 4–6) | Current thorough procedure | Two explicit review/synthesis rounds, including a second back-translation. Round two receives previous concerns and their disposition. Early approval does not omit round two. |
| T09 | Meaning > terminology > grammar > oral/spiritual quality > register > clarity > aesthetic preference (skill conflict hierarchy) | Current thorough procedure | One priority definition shared by both syntheses and quality notes. Preserve acceptance/rejection rationale as internal run evidence. A verdict-monoid fold is not a substitute for transmitting all review findings. |
| T10 | Paragraph, pronoun, and terminology verification (skill phase 6) | Current thorough procedure | Deterministic validation against source identifiers and applicable glossary requirements, followed by bounded targeted repair and revalidation. Successful verification does not establish semantic equivalence. |
| T11 | TXT, DOCX, and multiline pasted text (CLI input contract and confirmed goal) | Existing inputs plus requested Pi delivery | Supported workflow inputs with explicit file-versus-text selection, UTF-8 validation, empty/missing/unsupported/unreadable refusal, and no source overwrite. DOCX extraction must not silently omit unsupported content. |
| T12 | Phrase exception, natural-boundary segmentation around 2,000 source words, ordered assembly, mixed languages (skill edge cases) | Current thorough procedure | Explicit short-input path and notice. Every normal segment receives the full review process. Source paragraph identity survives sentence-level subdivisions and reassembly. Document finite runtime limits and refuse excess before model calls. |
| T13 | Saved final translation, Pi-visible result, brief separate notes, inspectable intermediates (skill phase 7 and important notes) | Current delivery contract plus native integration | Exclusive output creation, deterministic assembly, native typed text result, and normal run-store artifacts. Translation text excludes reviews, back-translations, headers, and quality notes. |
| T14 | Clear model failure and no silent fallback (skill edge cases) | Current reliability requirement | Existing native routing and recovery, with no workflow-supplied fallback ladder. Missing/invalid responses and exhausted repair prevent verified-success delivery. Cancellation retains native run semantics. |
| T15 | Catalogue, help, package assets, installation, and real Pi invocation (confirmed goal) | Integration requirement | Registry and package updates in the local agent-workflows clone. Preserve `translate` and `translate-es`. Verify the installed catalogue and approved file/text runs through the existing Pi integration, without redesigning `/wf`. |

## Reconciliations

### Review depth and revision restraint

The CLI design says that broad revision degraded first-instinct choices. The later
skill design explicitly distinguishes the thorough, two-round process from that
quick-draft interface. The workflow therefore retains both review rounds while
requiring each accepted change to address a concrete defect. Aesthetic alternatives
alone do not justify rewriting an accurate, concise phrase. Mechanical verification
preserves an already valid candidate unchanged.

### Glossary applicability

`glossary.csv` contains **43 data records**, despite several historical references
to 44. The CSV, including its notes, is authoritative. No missing forty-fourth term
is invented. The proper-name condition for باب and the divine-name condition for
حق are meaningful restrictions, not permission for substring replacement. Arabic
vocalization and Persian/Arabic letter variants require normalization for matching
without changing the stored source. Terminology review must also detect relevant
forms that deterministic matching cannot resolve.

The entry `وجود,being/existence` specifies alternative renderings rather than an
English phrase containing a slash. Both permitted words remain explicit. Ordinary
sentence capitalization does not license synonym substitution, and diacritics on
proper names remain significant. Packaged glossary assets must retain provenance
and an automated comparison with this CSV.

### Source coverage and paragraph alignment

The CLI's merge-shortest/split-longest fallback checks paragraph count, not source
alignment. The confirmed contract requires both coverage and alignment. The new
workflow retains stable source-unit identities and rejects missing, duplicated,
reordered, or empty units. It does not rearrange unrelated paragraphs merely to
make a count pass. Counts and identifiers are mechanical evidence of structural
coverage, while actual meaning coverage remains a linguistic review obligation.

### Empty reviews and incomplete results

An explicit, valid reviewer response reporting no issues is approval. A missing,
empty, malformed, or failed response is not approval. This distinguishes the
skill's “no feedback” shorthand from a transport failure. Likewise, the CLI's
fallback to an unverified draft is not a verified workflow success. Unresolved
critical findings and exhausted repair remain visible, prevent clean final
publication, and preserve diagnostic artifacts for inspection.

### Calibration and benchmark material

Preserve the supplied good, ornate, and literal examples as calibration, but remove
incorrect word-count assertions and claims about words absent from the quoted
example. Concision is a stylistic objective, not a cross-language word-count
acceptance formula. Meaning may require additional English words. Do not use the
calibration passage as a blind live-quality test, and do not supply held-out
reference translations to a translator being evaluated against them.

### Runtime composition

Use native model questions, named text panels, function calls, bounded revisions,
and typed results. Deterministic helpers may read documents, normalize and validate
structured responses, segment source text, and assemble artifacts. They do not
invoke models or run a hidden orchestration engine. If the authoring surface cannot
compose a needed native operation, correct that shared surface in the local
agent-cat clone with its owning tests rather than delegating orchestration to a
prompt.

## Isolation and verification baseline

`source-baseline.json` records original revisions, working-tree states, and diff
hashes. Both local clones use branch `translation-workflow` and contain committed
source HEAD, not uncommitted changes from the originals. In particular, the original
agent-cat `flake.lock` modification and `.worktrees/` directory remain untouched.
Builds and generated project state belong in these local clones.

The original non-integration suite passes: seven tests, one live integration test
deselected. Those tests cover basic reading and paragraph-count repair, not the
new workflow's quality, reviewer completeness, or failure semantics. Native
workflow tests and approved live acceptance evidence are additional requirements.
