# Repository Audit — 2026-08-06

## Scope

Repository: `pugazg/kalaignar-murasoli-letters`

This audit reviewed every branch against the canonical `main` branch after completion of the source-checked English translations through Volume 49 letter 3804.

## Canonical state before consolidation

- Canonical branch: `main`
- Canonical commit audited: `a69cbf9622ddc4f2a75674083e4cfae394e6a38e`
- Volume 49 Tamil transcription: complete, letters 3764–3816
- English translations source-checked: letters 3764–3804
- Translation count: 41 of 53
- Open pull requests: none
- One-use export/finalizer workflows: absent from the canonical tree

## Branch audit

| Branch | Relation to pre-audit `main` | Branch-only history/content | Decision |
|---|---:|---|---|
| `complete-volume-49` | 11 ahead / 155 behind | Old `.import-volume49/part-*` transport fragments only | Do not import temporary payloads; synchronise branch to canonical `main` |
| `stage-v49-3785-3789` | 7 ahead / 61 behind | Obsolete export/finalizer trigger files | Do not restore staging files; synchronise to `main` |
| `stage-v49-3790-3794` | 2 ahead / 36 behind | Obsolete export/finalizer trigger files | Do not restore staging files; synchronise to `main` |
| `stage-v49-3795-3799` | 3 ahead / 28 behind | Obsolete export/finalizer trigger files | Do not restore staging files; synchronise to `main` |
| `stage-v49-3800-3804` | 3 ahead / 18 behind | Obsolete export/finalizer trigger files | Do not restore staging files; synchronise to `main` |
| `translation-3775-3779` | 14 ahead / 75 behind | Earlier translation/audit commits and older progress metadata | Useful results already exist on `main` in the later source-checked history; synchronise to `main` without reverting newer work |
| `translation-import-3770-3774` | 18 ahead / 76 behind | Earlier translation import history plus cleanup of temporary importer files | Useful results already exist on `main` in the later source-checked history; synchronise to `main` |
| `translation-work` | 7 ahead / 70 behind | Obsolete import workflow and compressed staging payloads | Do not restore transport files; synchronise to `main` |
| `trigger-v49-3780-3784-finalizer` | 2 ahead / 65 behind | One obsolete finalizer trigger file | Do not restore trigger file; synchronise to `main` |

## Findings

1. No branch contained a legitimate translation, canonical Tamil correction, audit conclusion or repository document that was absent from the current `main` state.
2. The translation branches contain earlier histories of work that was subsequently committed to `main` in audited, source-checked form.
3. The staging branches contain only temporary workflows, triggers, encoded payload fragments or import transport files that the completed batch commits intentionally removed.
4. A conventional content merge would reintroduce obsolete operational files or risk replacing newer progress metadata with older versions.
5. The correct consolidation action is therefore to retain the current `main` tree as authoritative and move every historical branch reference to the audited canonical commit.

## Consolidation policy

- Preserve the canonical `main` content exactly.
- Do not reintroduce `.import-*`, `.translation-staging`, encoded payloads, one-use workflows or trigger files.
- Do not overwrite later source-checked translations or progress records with older branch versions.
- Synchronise every non-`main` branch to the final audit commit so that all named branches resolve to one canonical repository state.

## Next work

Resume the locked translation workflow with letters **3805–3809**, including visual scan comparison of every corresponding Tamil Markdown page before translation.
