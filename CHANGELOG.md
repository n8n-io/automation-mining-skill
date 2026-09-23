# Changelog

## Unreleased

The project now uses the [Apache License 2.0](LICENSE), which adds an explicit
patent grant. Releases up to v1.0.0 remain available under the MIT License.
The study is now called a whitepaper. Its source moved to `whitepaper/`, and the
release download is now `automation-mining-whitepaper-vX.Y.Z.pdf`.

## v1.0.0 — 2026-09-22

**Your next useful automation is already hiding in your work.**

The request you copy into a tracker. The question you answer every week.
The Friday report that starts with five open tabs. Start there.

Automation mining from **n8n labs** helps your agent find repeated manual work
and turn it into proposals you can check. Point it at one work source or a set
of activity records. Choose what deserves a build.

### Five proposals. Your call.

Get up to five proposals, each with source records, a count of distinct work
instances, the proposed change, and the decisions that still need a person.
Keep a finding, drop it, or ask the agent to investigate further. A report can
be empty when the records do not support a useful proposal.

An accepted proposal gives you a starting specification for an
[n8n workflow](https://n8n.io/). You decide what happens next.

### Give it a first job

```sh
npx skills@latest add n8n-io/automation-mining-skill --skill automation-mining
```

Start a new agent session, then ask:

> Use automation-mining to find repeated manual work in my agent sessions from
> the last two weeks.

Your agent needs access to those session files. Want to try it with supplied
records? The [synthetic example](examples/laptop-requests/README.md) includes
three laptop requests and a report for comparison.

Use Skills CLI, the Claude Code or Codex plugin, the Pi package, or a ZIP
download. Choose your route in the [installation guide](docs/installation.md).

### Read the evidence

This release includes the [whitepaper](whitepaper/taxonomy_skill.pdf), version 3, its
LaTeX source, and aggregate study records. The procedure was tested on
**57 synthetic companies** with two reader models. The study does not measure
the full interactive flow or time saved in use. See the [method](METHOD.md)
for the results and limits.

The skill contains instructions, not a background service. Your agent supplies
the connections. You choose the scope and review the findings before a build.

Both installable archives include the MIT License. Linux and Windows builds
produce the same package bytes, with SHA-256 checksums for each download.

[Visit the website](https://automation-mining-skill.pages.dev/) ·
[Try the example](examples/laptop-requests/README.md) ·
[Share feedback](https://github.com/n8n-io/automation-mining-skill/issues/new?template=feedback.yml)
