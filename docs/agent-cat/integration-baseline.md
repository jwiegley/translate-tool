# Isolated integration baseline

This is the initial, pre-implementation record. Current deployment and acceptance
status belongs in `implementation-evidence.md`. The commands below record the
baseline checks rather than superseding the current workflow installation guide.

## Checkouts

The two development checkouts are independent local clones, created with
`git clone --no-hardlinks` and checked out on `translation-workflow`:

- `agent-cat/` at `8a300822186a5702abb308f7c3516ff268620e6c`.
- `agent-workflows/` at `bee7b619bf5f8421901373740fc8e7d9ce8830bb`.

The originals under `~/src` remain read-only for this work. Their initial states
are recorded in `source-baseline.json`. Concurrent work in those originals is
unrelated. Do not pull it into these clones, restack against it, or revert its
changes to force a baseline comparison to pass. A later difference in an original
checkout requires attribution, not remediation by this project.

The root `.gitignore` excludes these nested repositories and Pi session state.
Changes from the baseline are visible with `git -C agent-cat diff 8a30082` and
`git -C agent-workflows diff bee7b61`. Existing `RESUME.md` remains untouched.

## Build and test evidence

The original Python tests pass:

```sh
uv run --frozen --extra dev pytest tests/ -v -m 'not integration'
```

Result: seven passed, one live integration test deselected.

Both Haskell packages build from the workflow clone using the supported Nix
shell and the sibling runtime source:

```sh
cd agent-workflows
CABAL_BUILDDIR="$PWD/dist-newstyle" \
  nix develop . --override-input agent-cat path:../agent-cat --no-write-lock-file \
  -c bash ../agent-cat/test/cabal.sh build all
```

The initial successful build used `path:.` in place of `.`. Subsequent commands
use the Git flake path so that Nix does not copy local build products into its
source snapshot. Both select the same pinned inputs with an explicit local
agent-cat override. Neither command writes a lock file. The Cabal plan confirms
that both project package sources are beneath translate-tool, and the compiler is
GHC 9.10.3. The only reported warnings concern the deliberately unwritten override
lock and the age of the unused Hackage index. No compiler warning was reported.

The owning workflow gate also passes:

```sh
CABAL_BUILDDIR="$PWD/dist-newstyle" \
  nix develop . --override-input agent-cat path:../agent-cat --no-write-lock-file \
  -c bash ci/workflows.sh
```

Result: 75 workflows pinned, zero failures. The gate checks scripted paths,
workflow help and its printed commands, and the `refocus-flow` test suite.
Both clones were clean before implementation.

Full local logs remain available at:

- `.pi/translation-evidence/baseline-build.log`
- `.pi/translation-evidence/baseline-workflows.log`

These are baseline checks, not evidence that the new translation workflow exists.

## Existing Pi integration

A read-only `agent_cat_workflow` catalogue request discovers both configured
runners, `agent-cat` and `wf`, including `wf:translate-en`, `wf:translate`, and
`wf:translate-es`. The existing Pi integration therefore needs no redesign.
The new implementation must replace the installed `wf` row through its supported
package route and be discovered through this same catalogue.

At this baseline, no live workflow had been launched and no package had been
installed or updated.

## Native composition findings

The following existing APIs determine the implementation approach:

- `Agentic.Workflow.taking` supports command-tail and standard-input text through
  `argsInputAs` and `stdinInputAs`. File content inputs in the generic CLI are
  UTF-8 text, not DOCX decoders. A declared path plus a deterministic document
  reader can support DOCX without treating its bytes as a prompt.
- `panelText` preserves every named review inside escaped, labelled blocks.
  `panel` instead folds verdicts and is not sufficient to transmit all six
  reviewers' proposed changes.
- `ParameterizedOf 'CodeText` and `answer` provide a Pi-visible translation result
  without a final model turn that could rewrite the verified text.
- `running` tools and registered `rowTools` provide deterministic local operations
  below the workflow. Existing Taskmaster helpers demonstrate schema validation
  and canonicalization without model calls inside the helpers.
- Native bounded revisions admit at most 64 amendments. The underlying builder
  already accepts an arbitrary typed right-hand side as an amendment, including
  a function call, but the public `amend` helper currently accepts only `Ask`.
  A small authoring-surface extension can expose that existing composition if
  needed for sequential document sections. It must preserve the raw language,
  model, and runtime semantics, and receive a regression test before use.
- Function bodies are straight-line programs. Both review rounds can be explicit
  within a section function, with deterministic validation between stages. The
  two-round process must not be modeled as an early-exit approval loop.
- `Workflows.Parties.reasoning`, `broad`, and `lateral` each install automatic
  fallback chains. The new translation workflow must not inherit those chains
  merely to obtain a primary model. Existing symbolic routing owns provider and
  sampling configuration, and adapters that cannot honor a requested setting
  must be identified rather than silently treated as equivalent.

These are implementation findings, not completed feature claims. Specific helper
schemas, repair behavior, short-input classification, and output publication still
require implementation and tests.
