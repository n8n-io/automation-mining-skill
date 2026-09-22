<p align="center">
  <img src="assets/hero.svg" alt="Automation mining by n8n labs. Find the work you keep doing by hand." width="1280">
</p>

<p align="center">
  <a href="#quick-start"><strong>Install the skill</strong></a> ·
  <a href="examples/laptop-requests/README.md">Try the example</a> ·
  <a href="paper/taxonomy_skill.pdf">Read the paper</a> ·
  <a href="docs/installation.md">Installation guide</a>
</p>

# Automation mining

**Find repeated manual work. Get proposals you can check. Choose what to build.**

Give your agent a set of activity records or access to one work source. The
skill looks for manual work: requests copied into a tracker, questions answered
each week, or reports assembled from several tools.

You get **up to five proposals**, each with the source records, a count of work
instances, and a clear description of what an automation could do. You choose
what to build.

An **n8n labs** experiment for Claude Code, Codex, Cursor, Pi, and other agents
that support [Agent Skills](https://agentskills.io/home). Available under the
[MIT License](LICENSE).

## Quick start

**Release status:** the first release is in preparation. After these changes
reach `main`, use the Git installation below. Release ZIP files and the Codex
marketplace package require the first version tag. Repository access is required
while this repository is private.

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

**Codex** — after `v1.0.0` is published, run these commands in your terminal:

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

For ZIP downloads, updates, removal, and migration, see the
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

## The method, measured

The skill includes the procedure tested in **[Improving Automation Discovery
with a Workflow Taxonomy](paper/taxonomy_skill.pdf)**, by Albert Alises, n8n.
The repository includes the latest reviewed paper, version 2, and its LaTeX source.

The study used a taxonomy of **907,353 workflow rows** to define tasks and create
synthetic activity. Feedback changed the skill instructions; model weights
stayed fixed. A separate test used **57 synthetic companies** and two reader models.

| Measure | Starting procedure | Included procedure | Change, with 95% interval |
| --- | ---: | ---: | ---: |
| Useful proposal quality | 44.7% | **53.0%** | +8.3 points [0.3, 16.8] |
| Verified task recall | 28.2% | **51.7%** | +23.5 points [13.0, 34.4] |

These results apply to the procedure on synthetic exports. The study does not
measure the full interactive flow, user demand, or time saved in use. A later
revision failed the release rule, so the package keeps the confirmed procedure.

[Paper PDF](paper/taxonomy_skill.pdf) · [Method and limitations](METHOD.md) ·
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
[Changelog](CHANGELOG.md) · [Security](SECURITY.md) · [MIT License](LICENSE)
