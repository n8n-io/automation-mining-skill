<p align="center">
  <img src="assets/hero.svg" alt="Automation mining by n8n labs. Find the work you keep doing by hand." width="1280">
</p>

<p align="center">
  <a href="https://automation-mining-skill.pages.dev/">Website</a> ·
  <a href="#quick-start"><strong>Install the skill</strong></a> ·
  <a href="examples/laptop-requests/README.md">Try the example</a> ·
  <a href="whitepaper/taxonomy_skill.pdf">Read the whitepaper</a> ·
  <a href="docs/installation.md">Installation guide</a>
</p>

# Automation mining

**Discover what you could automate.**

Requests you copy into a tracker. Questions you answer every week. Reports you
assemble by hand. Automation Mining helps your agent find this work in activity
it can read and show you what an automation could do.

Give it one work source. It finds repeated manual tasks and returns **up to five
proposals**. Each proposal includes source records, a count of work instances,
and a clear description of the change. You check the evidence and choose what
to build.

An **n8n labs** experiment for Claude Code, Codex, Cursor, Pi, and other agents
that support [Agent Skills](https://agentskills.io/home). Open source under the
[Apache License 2.0](LICENSE).

## Quick start

Install with [Skills CLI](https://www.skills.sh/docs):

```sh
npx skills@latest add n8n-io/automation-mining-skill --skill automation-mining
```

Choose your agent and installation scope. The installer needs Node.js and Git.
Start a new agent session, then ask:

> Use automation-mining to find repeated manual work in my agent sessions from
> the last two weeks.

This needs no external connection if your agent can read those session files.
With a Slack connection, try:

> Use automation-mining on #ops-requests for the last 30 days. I handle operations
> for the team.

**No activity to connect yet?** Use the [small synthetic example](examples/laptop-requests/README.md).
It includes the input records and a report for comparison.

<details>
<summary><strong>Claude Code, Codex, and Pi packages</strong></summary>

Choose one installation route per agent.

**Claude Code** — run these commands inside Claude Code:

```text
/plugin marketplace add n8n-io/automation-mining-skill
/plugin install automation-mining@n8n-automation-mining
```

Start a new session, then use `/automation-mining:automation-mining`.

**Codex** — run these commands in your terminal:

```sh
codex plugin marketplace add n8n-io/automation-mining-skill
codex plugin add automation-mining@n8n-automation-mining
```

Start a new session, then select **Automation mining** in the skill picker.
Use Skills CLI if your client does not support plugins.

**Pi** — run this command in your terminal:

```sh
pi install git:github.com/n8n-io/automation-mining-skill
```

Start a new session, then use `/skill:automation-mining`.

For ZIP downloads, updates, and removal, see the
[installation guide](docs/installation.md).

</details>

## What it can find

| The work you keep doing | The change to investigate |
| --- | --- |
| Copy a request from chat into a tracker | Create the record and route it for approval |
| Answer the same question with the same links | Put the answer and its source with the request |
| Check a lead in several tools, then update the CRM | Collect the fields and update the record |
| Assemble a weekly report from several sources | Prepare a report for a person to review |
| Notice a failed job and tell its owner | Detect the failure and notify the owner |
| Ask your agent for the same meeting brief | Prepare it from the calendar and source records |

These are examples, not promises. The skill checks your records before it
proposes a change. It also identifies work already automated and gaps that need
a decision, an owner, or a document first.

## From activity to a decision

1. **Choose a starting point.** The agent states what it can read and asks about
   your work. Start with one source and a clear time window.
2. **Steer the findings.** Review short cards. Keep, drop, or deepen a candidate.
   Approve a new source when the evidence points there.
3. **Check the proposal.** See the work, its count, the proposed change, and what
   still needs a person. Source links let you check the claims.
4. **Give your verdict.** Build it. Real, but not worth it. You misread this.

<img src="assets/example-report.svg" alt="Synthetic example: three laptop requests support one proposal to copy requests from Slack into Linear, with approval kept with a person." width="1280">

Run time and model cost depend on the agent, tools, and number of records.
A report can be empty when the records do not support a useful proposal.

## How we tested the method

The released skill includes the procedure tested in **[Improving Automation
Discovery with a Workflow Taxonomy](whitepaper/taxonomy_skill.pdf)**, by Albert
Alises, n8n. The repository includes the reviewed whitepaper and its LaTeX source.

The study used a taxonomy of **907,353 workflow rows** to define tasks and make
synthetic activity. Feedback changed the skill instructions; it did not change
model weights. A separate test used **57 synthetic companies** and two AI models
to read their activity.

| Measure | Starting procedure | Included procedure | Change, with 95% interval |
| --- | ---: | ---: | ---: |
| Useful proposal quality | 44.7% | **53.0%** | +8.3 points [0.3, 16.8] |
| Verified task recall | 28.2% | **51.7%** | +23.5 points [13.0, 34.4] |

These results compare the released procedure with its starting version on
synthetic records. They do not measure the full interactive flow or time saved
by real teams. A later procedure did not pass the release rule, so the package
keeps the confirmed version. A separate comparison with a short prompt did not
show a clear gain in proposal quality.

[Whitepaper PDF](whitepaper/taxonomy_skill.pdf) · [Method and limits](METHOD.md) ·
[Study records](research/README.md) · [Citation](CITATION.cff)

## Your data and your control

The skill tells the agent to read source activity without posting, editing, or
reacting. Reports use pointers and counts, not copied message bodies, personal
data, or credentials. Use your own work or a channel you belong to, and tell
the channel.

The package contains instructions. It does not add data connections or a
background service. Your agent, tools, and model provider process data under
your account settings. Tool permissions must enforce access limits.

Building an automation is a separate task after review. Changes to a source
require your approval for that source.

## Found it? Build it in n8n.

An accepted proposal states the trigger, operation, output, and checks that
remain. Use it as the starting specification for an [n8n workflow](https://n8n.io/).

Help improve the skill: [report a problem or share feedback](https://github.com/n8n-io/automation-mining-skill/issues/new?template=feedback.yml).
Use synthetic examples and remove private data before sharing.

---

[Install and update](docs/installation.md) · [Contribute](CONTRIBUTING.md) ·
[Release notes](CHANGELOG.md) · [Security](SECURITY.md) · [Apache License 2.0](LICENSE)
