# Contribute

Use the [feedback form](https://github.com/n8n-io/automation-mining-skill/issues/new?template=feedback.yml)
to report an installation problem, incorrect count, missing evidence, or proposal
that leaves the manual work in place. State your agent version, the steps you
used, and the expected result. Use synthetic examples. Do not include source
messages, customer records, credentials, or session exports.

## Change the repository

1. Create a branch for one clear change.
2. Update the relevant files and documentation.
3. Run the [package checks](docs/distribution.md#check-a-change).
4. Open a pull request. Describe the problem, the new behavior, and the checks
   you ran. Use a conventional commit title, such as `fix: check duplicate requests`.

The installable skill is in `skills/automation-mining/`. Use ASD-STE100
Simplified Technical English for new technical text. Keep temporary reports,
data exports, and development notes outside the repository.

## Preserve the study record

The tested procedure, schema, paper, and aggregate result files have hashes in
`research/manifest.json`. A package or documentation change must preserve those
files. A new procedure needs its own evaluation and source record; it must not
inherit claims from a different tested version.

Changes use the repository's [MIT License](LICENSE).

## Check a claim before changing it

Separate a source finding, a proposed automation, and a measured result.
A work count needs distinct instances. A benefit claim needs evidence.
Do not turn the synthetic study results into a claim about customer savings.
Use the comparison names in [the study guide](research/README.md#read-the-comparisons-correctly).

The instruction count and hashes in the procedure metadata refer to different
text scopes. Run `python3 scripts/test_skill.py` before changing that metadata.
Do not edit the tested procedure to make a metadata check pass.
