# Try automation mining without a connection

This small example contains synthetic Slack, Linear, Notion, and Salesforce
records. It requires no service account or private data. Use it after installing
the skill, or point your agent at the skill in this repository.

## Run the example

Download [activity.json](activity.json) and give it to your agent with this prompt:

> Use automation-mining to find automation opportunities in the attached
> activity.json. These records are synthetic. The owner is unavailable. Read
> only the supplied records and write the report as JSON to report.json.

When using this repository, give the agent the explicit path
`examples/laptop-requests/activity.json`. Let it read the skill and its references.
Keep the expected report and this guide out of the agent's input for a useful test.

## Check the result

The records support one operation: copy laptop requests from Slack into Linear.
There are three requests, `LAP-001` through `LAP-003`. The follow-up about `LAP-001`
refers to an existing ticket; it is not a fourth request. Each `slack-copy-*`
record directly describes a person doing the work.

Compare your result with [the example report](expected-report.json). Its wording
is illustrative. The operation, count, source IDs, and remaining human approval
are the points to check. Access and event support must remain unverified.

From the repository root, use Python 3.12 or later:

```sh
python3 scripts/check_example.py report.json
```

This checks the expected count, distinct request IDs, and source citations. It is
specific to this fixture. It does not judge whether the proposed workflow is useful
or whether its text accurately describes the operation. Check those points yourself.

## Check a case with no supported task

Start a separate session with [routine-only.json](routine-only.json) and the same
prompt. Save the output as `routine-report.json`. The expected result is:

```json
{"proposals": []}
```

These records contain a policy, an announcement, and work already done by
successful automations. They do not establish manual work that a build can remove.

```sh
python3 scripts/check_example.py routine-report.json --routine-only
```

The example checks basic behavior. It does not measure proposal quality in real use.

## Run the tests

From the repository root:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
```

To run only the example tests, use `python3 scripts/test_example.py`.
