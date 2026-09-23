# Distribution and releases

The installed skill is in `skills/automation-mining/`. Claude Code, Codex, and Pi
load the same files. The package has no executable agent extension and no
runtime dependencies.

## Check a change

Use Python 3.12 or later from the repository root:

```sh
python3 scripts/package.py check
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/package.py build
```

The checks compare package versions, local links and heading links, licenses,
required files, and research hashes. Builds use an explicit file list. Files
outside that list cannot enter an archive. Add a new installable file to
`SKILL_FILES` or `PLUGIN_FILES` in `scripts/package.py` when required.

ZIP timestamps, permissions, and file order are fixed. Tests check that repeated
builds produce identical bytes, local files stay out of archives, and download
checksums match. The release workflow also compares Linux and Windows builds.

For Claude Code package validation:

```sh
claude plugin validate .
claude plugin validate .claude-plugin/marketplace.json
```

Test installation in a temporary agent configuration. Confirm that one skill
appears and that its reference files are present. Package checks do not test
the quality of a mining run. Use a separate evaluation for procedure changes.

## Release files

`python3 scripts/package.py build` writes these files to `dist/`:

| File | Contents |
| --- | --- |
| `automation-mining-vX.Y.Z.zip` | Skill, references, display metadata, and license |
| `automation-mining-plugin-vX.Y.Z.zip` | Skill, plugin manifests, marketplace files, and display images |
| `automation-mining-whitepaper-vX.Y.Z.pdf` | Current whitepaper revision |
| `SHA256SUMS` | SHA-256 checksums for all three downloads |
| `RELEASE_NOTES.md` | Changelog entry with links fixed to the release tag |

The whitepaper and study records stay out of the installable archives. The repository
contains those records. The plugin archive includes only the images needed for
its display. The README graphics and social preview remain in `assets/`.

## Package formats

The Claude marketplace `owner` field is an object with a `name`, as specified
in the [Claude marketplace schema](https://code.claude.com/docs/en/plugin-marketplaces#required-fields).
The Codex compatibility manifest uses `skills: "./skills/"`, as specified in
the [OpenAI package guide](https://developers.openai.com/plugins/build/plugins#plugin-creator-output).
These fields have different schemas; do not copy one format into the other.

## Prepare a release

1. Change `version` in `package.json`.
2. Run `python3 scripts/package.py sync`. This updates the plugin versions, the
   Codex source tag, skill metadata, and copied license.
3. Replace `Unreleased` in `CHANGELOG.md` with the release date. Update the
   version in `CITATION.cff`. Add the top-level `date-released` field for the
   first release; update it on later releases. Set its whitepaper URL to the release tag.
4. Run the checks above and review the packages.
5. Check the repository description, homepage, and social preview in GitHub
   settings.
6. Merge the release change, then tag the merged commit with `vX.Y.Z` and push
   that tag.
7. After publication, verify the download and installation links. Remove the
   pending-release notes from the README and installation guide in a follow-up
   documentation change.

The release workflow requires the tag to point to a commit on `main`. It runs
checks and tests on Linux and Windows, compares package checksums, and verifies
the downloads before publication. It updates an existing draft release or
creates a new release. It does not replace an existing published release.

GitHub Actions use fixed commit hashes. Dependabot checks them each month.
Pull requests, pushes to `main`, and releases run Gitleaks on all fetched Git
history. The scanner version and download checksum are fixed in
`.github/workflows/secrets.yml`. Matches fail the check; values are hidden in
the log. A finding in an older commit also blocks new changes. This is
intentional: deleting a secret from the current tree does not remove it from
Git history. Revoke exposed credentials and remove them from reachable history
before release. Review false positives before adding any narrowly scoped scanner
configuration. To run the same scan locally after you install Gitleaks:

```sh
gitleaks git --log-opts=--all --redact --max-decode-depth=3 --max-archive-depth=3 --ignore-gitleaks-allow --no-banner
```

The repository keeps `private: true` in `package.json` to prevent accidental npm
publication. This flag does not affect Git or ZIP installation.

## Preserve the measured procedure

The procedure, schema, whitepaper, and study records have fixed hashes in
`research/manifest.json`. Keep their bytes unchanged for a distribution change.
See the [study record guide](../research/README.md) for file details and access limits.

To build the whitepaper, use [Tectonic](https://tectonic-typesetting.github.io/en-US/):

```sh
cd whitepaper
tectonic -X compile taxonomy_skill.tex
```

Build in a temporary copy when you only want to check the source. A local
compiler can change PDF metadata and file hashes. Do not replace the versioned
PDF during an unrelated package change.

## License

The package uses the [Apache License 2.0](../LICENSE). Both installable archives include
its full text. The package check compares the skill license with the root license.
