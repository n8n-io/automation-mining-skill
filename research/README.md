# Study records

These files contain aggregate results and validation records for the procedure
in [the paper](../paper/taxonomy_skill.pdf). The package retains the procedure
confirmed in the first test. The second test did not support a further release.

| Record | Contents |
| --- | --- |
| [Confirmed analysis](confirmed/analysis.json) | Revised skill versus short prompt on 57 synthetic test companies |
| [Training comparison](confirmed/training-comparison.json) | Revised skill versus starting skill on the same 57 test companies |
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

The manifest identifies the 15 study, procedure, and paper files it lists by
size and SHA-256 hash. It does not cover the full repository.
Private repository names, commit IDs, and source paths are omitted. Study notes were updated to remove private history references and to define
the comparison, validation, and version scopes. Their hashes were updated. Study results and the tested procedure are unchanged. Paper version 3 revises language and structure; its numeric table entries
and study results are unchanged. See [METHOD.md](../METHOD.md) for the design and limits.

## Read the comparisons correctly

The first test has three conditions: the starting skill, the revised skill,
and a short prompt. Both result files use the same 57 test companies.

- `confirmed/training-comparison.json` compares the revised skill with the
  starting skill. It supplies the 44.7% to 53.0% quality result and the 28.2%
  to 51.7% recall result.
- `confirmed/analysis.json` compares the revised skill with the short prompt.
  The short prompt has 47.1% quality and 33.9% recall. The quality interval for
  this comparison includes zero. The study does not establish a quality gain
  over the short prompt.

The word `training` in the first filename names the instruction comparison.
It does not mean that the headline result was measured on training companies.

## Limits of the validation record

`confirmed/release-validation.json` records 240 development score replays.
It lists 20 `discovery-test-*` validation packets, but does not include their
file hashes. Those packets are not distributed here and cannot be checked from
this repository. Its `dataset` hashes cover the `refinement-test-*` final-test
records. The full source data and evaluation code are also not included.

`search/selection.json` records candidate selection on 60 separate validation
companies with two readers. It is not a final-test or release result.
The `skill_version` in `search/skill-retention.json` is a study version, not the
installable package version.
