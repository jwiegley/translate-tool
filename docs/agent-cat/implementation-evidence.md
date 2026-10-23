# Implementation evidence

The requirements in `translation-contract.md` are implemented in the local
agent-workflows and agent-cat clones. This record distinguishes implemented and
checked behavior from live linguistic acceptance, which remains unfinished.
The Nix package is built, checked, installed, and discovered by the restarted Pi.

## Local implementation revisions

The local `agent-cat` branch contains these independent changes:

- `ae0c9f0`: exact documented CLI refusal diagnostics.
- `61ce8e7`: standalone captured audit package builds.
- `ac0472b`: current manager audit mutation anchors.
- `239c684`: typed workflow amendment composition, regression tests, and manual.

The local `agent-workflows` implementation is `54ca322`. All 21 changed workflow
files were compared byte-for-byte with the package-tested Nix source before
committing. The installed package therefore contains the committed workflow and
helper implementation. The documented local runtime override remains required
until the dependency revision is published. No changes were pushed.

Runtime issue closure and live acceptance remain pending. These commits preserve
that status rather than treating a local commit as completion evidence.

## Requirement-to-code map

| Requirements | Implementation | Executable evidence |
| --- | --- | --- |
| T01–T02: developed register, calibration, concision, and revision restraint | `agent-workflows/assets/translate-en/`, reproduced by `tools/sync-translate-en.py`. The helper inserts the calibrated register into drafting and synthesis. Synthesis rejects changes to units without accepted findings. | Source regeneration check, packaged-asset hashes, mandate/calibration tests, and unaccepted-revision refusal tests. |
| T03: model and sampling configuration | Three dedicated symbolic profiles, `translate-en`, `translate-en-back`, and `translate-en-verify`, without authored fallback chains. Configuration requirements are documented in `agent-workflows/doc/translate-en.md`. | Catalogue pin checks pass. Actual live model identity and supported sampling settings still require acceptance evidence. |
| T04–T05: preparation and initial draft | `Workflows.TranslateEn.prepareFn`, `draftFn`, and the helper's `prepare`, `section`, `check_brief`, and `candidate_units`. Conditional glossary applicability is per source unit. | Native TXT and pasted-text flows, mixed-language tests, total terminology-application checks, ordered unit validation, and rejection of untranslated Arabic/Persian in an English candidate. |
| T06–T09: all specialist reviews, independent back-translation, both rounds, and conflict priority | `reviewFn`, both back-translation functions, both synthesis functions, and `reviewedSectionFn`. Native text panels retain every review. The helper enforces response schemas, round transitions, issue accounting, and accepted-revision scope. | Native traces contain twelve reviewer consultations and two back-translations per normal section. Prompt tests check all six mandates and the shared priority. Missing reviews fail without publication. |
| T10: mechanical validation and bounded repair | `mechanical_errors`, `repair_options`, and `apply_repairs`. The verifier selects only enumerated local pronoun replacements. Remaining glossary or critical issues fail rather than allowing free paraphrase. | Pronoun/contraction repair, unauthorized/duplicate edit, unchanged-valid-text, unresolved-critical, and exhausted-verification tests. |
| T11–T12: files, pasted text, mixed language, long documents, and phrase exception | `read_source`, `partition`, `may_be_phrase`, and native first-section plus bounded remaining-section composition. The public `amendWith` helper exposes existing typed RHS amendment composition. | UTF-8/BOM, TXT, DOCX body/table order, unsupported DOCX refusal, mixed paragraphs, long-source assembly, native multi-section iteration, and native phrase-path tests. |
| T13: final artifacts and Pi-visible result | The helper's `append`, `final_text`, `quality_notes`, and `publish`, followed by native typed `answer`. The publication effect atomically creates a link to a complete private bundle. | Saved text/manifest/notes checks, private modes, existing-destination refusal, injected write failure, root replacement, and symlink-root refusal. |
| T14: honest failure and cancellation | Native routing and execution, context-isolation gate, strict helper failure exits, bounded section processing, and publication only after validation. | Native unavailable-model, empty-review, unauthorized-repair, shared-context, and cancellation tests all fail without final artifacts. |
| T15: packaging and Pi integration | Registry replacement, Nix helper wrappers, declared source assets, help, guide, cookbook, and dedicated translation gate. Other translation directions remain registered through their original implementation. | All 75 workflow rows, cookbook, and packaged-helper checks pass. The installed runner advertises file/text inputs and a typed result. Restarted Pi discovers the new workflow. Approved real runs remain pending. |

## Checks completed

- Original translate-tool baseline: seven tests passed, one live test deselected.
- Translation helper suite: **36 tests passed**.
- Native translation flow: passed with actual deterministic helpers and fixture
  model answers. It covers file, pasted, mixed, long, and phrase paths, complete
  source assembly, nineteen model calls per normal section, three for a phrase,
  both review rounds, source-hidden reverse prompts, artifacts, failures, and
  cancellation.
- Workflow regression gate: **75 rows, zero failures**. It includes the original
  unrelated workflows and their help examples.
- Cookbook: **75 regions**, regeneration byte-identical after the update.
- Runtime documentation: source excerpts, 270-item coverage/index, prose, CLI
  examples, 140 exported children, and 112 exported-class instances passed.
- Frozen conformance: **tier0 193 passed**, **tier1 30 passed**.
- Direct runtime policy probe, including the new amendment test, passed.

The final production package includes the untranslated-source and synthesis-scope
guards and passed its package gate. It was installed with `nix profile add`:

`/nix/store/v4hqn841pz3dbqwfns4gkn7qmsl0yl1k-agent-workflows`

The `agent-workflows` user-profile entry roots that package. Its wrapper hash and
installed descriptor are recorded in the local evidence. No Home Manager switch
or original `~/src` change was made.

## Runtime gate correction

The complete runtime policy gate initially stopped at the restore-interruption
audit with `actual currentReview boundary was not reached`. Its build log showed
that Cabal selected the enclosing checkout's project instead of the captured,
instrumented package. The local test harness now creates and records a standalone
`cabal.project` in that captured package. The real restore-interruption audit then
passed at both `-N1` and `-N8`. No manager production behavior was changed.

A later commands check retained an obsolete empty-stderr assertion, despite the
documented exact operator notices. The test now permits only those expected
bytes at the appropriate refusals. Frozen JSON, exit mapping, credential secrecy,
lease and lost-reply checks remain. The commands gate passed at N1 and N8.

The next policy attempt found stale mutation anchors after existing production
refactors. Five test modes now target the shared decision guards, scoped ticket
constructor, and tagged ingestion refusal. Preparation succeeds for all 46 audit
modes. All five repaired modes then passed compiled checks at both N1 and N8.
The full policy gate reached the artifact checks, where inherited Pi environment
variables violated an intentional isolation assertion. A subsequent isolated run
found that Nix's temporary path included the macOS `/tmp` symlink, which private
configuration reads correctly reject. The current run clears `AGENT_CAT_*` and
canonicalizes `TMPDIR` inside only its test subprocess. Neither the isolation
assertion nor the no-symlink security check was weakened. The focused artifact
gate subsequently passed its N1/N8 checks and real history-observation audits.
The complete policy gate is still running.

## Pending acceptance

The full runtime policy gate remains an owned background job, recorded in
`.pi/translation-evidence/background-jobs.json` as `policy-v5`. Inspect its exit
marker and log before claiming the complete runtime gate passed. No paid or live
translation has been launched.

Runner configuration was subsequently lost from a restarted Pi process, producing
`No AGENT_CAT_RUNNER is configured`. Passing `AGENT_CAT_RUNNERS` explicitly through
`agent-deck session restart --env` restored discovery of `wf:translate-en`. The
installed descriptor confirms file/command-tail and text/stdin inputs, all three
routing profiles, and a typed text result. No shell or Home Manager configuration
was rewritten. Catalogue discovery does not establish successful `/wf` execution.

Source-only acceptance fixtures are ready under
`.pi/translation-evidence/acceptance/`, with primary-source URLs, normalized hashes,
and extraction notes. No English reference was fetched or supplied to them.
Required live acceptance is the Arabic DOCX file and the multiline Persian literal,
approved through the normal Pi launch mechanism, with inspected artifacts and
actual routing facts.

The user requires the existing `/wf` entry point. The earlier `/wf-launch` detour
did not satisfy that requirement. Installed `/wf` passes only `--session` with
the current Agent Deck session and supplies no per-pin routes. That explicit
target bypasses routing files. The translation helper correctly refuses a normal
passage when the back-translator shares source context. Deterministic preflight
with the acceptance DOCX reproduced that refusal without a model call.

Live-run consent has been granted. The remaining issue is platform compatibility,
not missing chat approval. A narrow extension to let `/wf` use workflow-specific
routing while preserving its current defaults has been proposed. It touches the
original launch-behavior boundary and awaits the user's answer before changes.
No isolation guard is to be weakened, and no alternate command is to be counted
as successful `/wf` acceptance.

Fixture success is not evidence of linguistic fidelity, literary quality, or
spiritual potency. Those judgments remain part of the pending live acceptance.

## Original repository observation

Read-only inspection with `GIT_OPTIONAL_LOCKS=0` confirms that original
`~/src/agent-workflows` still matches its baseline revision, branch, status, and
diff hashes. Original `~/src/agent-cat` retains its baseline revision, branch,
status, and staged diff, but the diff hash of its already-modified `flake.lock`
has changed. This work does not revert or incorporate the original repository's
concurrent changes. The observed difference is recorded rather than claiming
that the original tree is byte-identical to the initial snapshot.
