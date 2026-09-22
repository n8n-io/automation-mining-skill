# How the workflow taxonomy shaped the skill

The skill finds supported human work in activity records and proposes at most
five changes that remove that work. Version 1.0.0 includes the exact procedure
tested in *Improving Automation Discovery with a Workflow Taxonomy*.

## From workflows to tasks

The source export contains 907,353 workflow rows from 100,282 instance IDs.
We select portfolios with sustained successful use and work across several
business domains. The source shows configured automation. It provides examples
of operations that automation can perform.

For each selected workflow, the method defines a task through its trigger,
work unit, operation, source, destination, and outcome. A second model checks
these task definitions. The definitions then guide the construction of
synthetic Slack, Notion, Linear, and Salesforce activity. Each task has a hidden
answer key and distinct work instances. Other records provide routine activity,
existing automation, and cases with no supported task.

## From tasks to instructions

The training process runs a starting skill on development companies. It checks
the proposed task, the cited activity, the proposed change, and the work-instance
count. This feedback shapes a complete replacement procedure. A separate
development selection compares candidate procedures before the final test.

The selected procedure reads all supplied sources, keeps the full observed task,
joins records only when their identifiers support the connection, and checks
each proposal against its evidence. One supported instance can establish a
task. A claim of repeated work requires more than one distinct instance. The
procedure can return an empty list when the records support no proposal.

Training changes the instruction text. It does not change model weights.

## Validation and the separate test

The source split excludes prior instance IDs and matching normalized workflow
summaries. Construction uses fixed structural checks, task-instance checks,
and a source privacy check. Each source slot has a fixed attempt limit. Failed
slots stay in the construction record and receive no replacement.

The final test admitted 57 of 80 new source slots. It contains 105 tasks and
4,844 activity records. Eighteen companies have no keyed task. Two models read
each company under each instruction condition with the same five-proposal cap,
output schema, and scoring rules.

Task identity and cited support receive separate model checks. The scorer also
checks whether the change removes the stated operation, whether the count is
supported, whether citations resolve, and whether work instances are distinct.
Empty reports receive zero useful-proposal credit. The analysis averages paired
reader differences within each company and uses 10,000 company bootstrap samples.

## Completed result

| Primary measure | Starting skill | Trained procedure | Paired change, 95% interval |
| --- | ---: | ---: | ---: |
| Useful proposal quality | 44.7% | 53.0% | +8.3 points [0.3, 16.8] |
| Verified task recall | 28.2% | 51.7% | +23.5 points [13.0, 34.4] |

Both measures pass the fixed improvement rule. The trained procedure returns
nonempty reports in 77 of 78 runs on companies with a keyed task. Its pooled
verified proposal precision is 72.0%.

These measurements apply to fixed synthetic exports and the bundled procedure.
The interactive flow adds source collection, owner direction, proposal review,
and owner verdicts. The study does not measure those steps.

## Further instruction search

A ten-hour search uses completed companies for training, then selects a further
revision on 60 new validation companies. A fresh test compares that revision
with the bundled procedure on 116 other synthetic companies. The test has 208
tasks and 10,088 Slack, Notion, Linear, and Salesforce records.

Verified recall rises from 59.2% to 65.9%, a gain of 6.8 points [0.3, 13.0].
Useful quality changes from 59.3% to 58.1%, a change of −1.2 points [−6.4, 4.1].
Pooled precision falls from 76.0% to 72.4%. These comparisons use 95% paired-company
intervals for quality and recall. All 464 jobs have terminal records; two reference
miners fail and receive zero under the fixed rule. There are no missing judge scores.

The new revision does not meet the joint release rule or the added checks for
no observed decrease on each quality measure. Version 1.0.0 therefore retains
the confirmed procedure. The bundled [search results](research/search/analysis.json)
and [release decision](research/search/skill-release-check.json) record the
comparison. Each test uses its own dataset and reference.

## Files and reproducibility

- [Tested procedure](skills/automation-mining/references/workflow-discovery.md),
  [report schema](skills/automation-mining/references/workflow-discovery.schema.json), and
  [source hashes](skills/automation-mining/references/workflow-discovery.artifact.json).
- [Paper PDF](paper/taxonomy_skill.pdf) and [LaTeX source](paper/taxonomy_skill.tex),
  with all tables, references, and TikZ diagrams in one source file.
- [Confirmed training comparison](research/confirmed/training-comparison.json)
  and [confirmed release checks](research/confirmed/release-validation.json).
- [Fresh test analysis](research/search/analysis.json),
  [validation selection](research/search/selection.json), and
  [skill release checks](research/search/skill-release-check.json).
- [Offline score replay](research/search/offline-validation.json),
  [source input checks](research/search/release-input-checks.json), and
  [skill retention record](research/search/skill-retention.json).
- [File hashes](research/manifest.json).
- [Study record index and access limits](research/README.md).

The procedure file is copied without text edits. Its source hash fixes the
measured version. It includes the instruction body and common benchmark contract
that both formed the tested system text. The report schema specifies field
structure; the study's scoring checks also verify evidence, counts, and work
instances. The schema alone does not establish proposal quality.
It does not enforce unique citation arrays or cross-field count rules. Those
requirements remain in the procedure's final checks. The file's final block is
the common output contract appended to each instruction condition during the
test. Both blocks and the schema retain their tested bytes.

The routing instructions in the installed skill select this procedure for
explicitly synthetic exports. Real exports and connected activity use the
owner-review flow. This prevents the test procedure's fictional-data assumption
from being applied to actual activity.

The paper uses the latest reviewed version 2 text. Its PDF and LaTeX source
retain their reviewed bytes. The manifest records the hashes of the included files. Private repository
references are omitted. Two study notes were updated to remove references to
private history. Study results and the tested procedure are unchanged.

The private workflow export, complete synthetic datasets, model responses, and
evaluation code are not distributed here. The bundled records document the
reported checks. They do not let readers repeat the complete study independently.

Build the paper from this repository with Tectonic:

```sh
cd paper
tectonic -X compile taxonomy_skill.tex
```

The copied offline record reports 768 score replays, 176 dataset hash checks,
three instruction body hash checks, and an identical final analysis. These are
recorded study checks, not checks that the package build runs again.
