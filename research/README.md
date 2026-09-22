# Study records

These files contain aggregate results and validation records for the procedure
in [the paper](../paper/taxonomy_skill.pdf). The package retains the procedure
confirmed in the first test. The second test did not support a further release.

| Record | Contents |
| --- | --- |
| [Confirmed analysis](confirmed/analysis.json) | Results from 57 synthetic test companies |
| [Training comparison](confirmed/training-comparison.json) | Results used during instruction development |
| [Confirmed validation](confirmed/release-validation.json) | Hashes and checks for the first study |
| [Further test analysis](search/analysis.json) | Results from 116 new synthetic test companies |
| [Candidate selection](search/selection.json) | Selection on a separate validation set |
| [Release decision](search/skill-release-check.json) | Checks that the further revision did not pass |
| [Retained procedure](search/skill-retention.json) | Hashes of the procedure kept for release |
| [Offline validation](search/offline-validation.json) | Recorded score replay and hash checks |
| [Input checks](search/release-input-checks.json) | Recorded source checks |
| [Further study validation](search/release-validation.json) | Hashes and checks for the second study |
| [File manifest](manifest.json) | File sizes and SHA-256 hashes |

The private workflow export, full synthetic datasets, model responses, and
evaluation code are not distributed here. The records document the reported
checks; they are not enough to repeat the complete study independently.

The manifest identifies the files included here by size and SHA-256 hash.
Private repository names, commit IDs, and source paths are omitted. Two study
notes were updated to remove references to private history. Their hashes were
updated. Study results and the tested procedure are unchanged. The paper uses
the reviewed version 2 text. See [METHOD.md](../METHOD.md) for the design and limits.
