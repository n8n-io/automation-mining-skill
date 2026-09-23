# Install and update

Choose one installation route per agent. The package supplies instructions and
reference files. Connect the tools you want to read through your agent.

## Choose a route

| Route | Use it when | Availability |
| --- | --- | --- |
| [Local files](#local-files) | You want to try a checkout before installing | Available from this checkout |
| [Skills CLI](#skills-cli) | You want the installer to configure your agent | Available |
| [Claude Code plugin](#claude-code-plugin) | You use Claude Code marketplaces | Available |
| [Codex plugin](#codex-plugin) | You use a Codex client with plugin support | Available in v1.0.0 |
| [Pi package](#pi-package) | You use Pi packages | Available |
| [ZIP download](#zip-download) | You want a versioned manual installation | Available in v1.0.0 |

GitHub access is required while the repository is private. The Codex
marketplace source is pinned to the `v1.0.0` release tag.

## Local files

From a checkout, ask your agent to read `skills/automation-mining/SKILL.md`
and follow its references. Then give it the records to examine. Start with the
[synthetic example](../examples/laptop-requests/README.md) if you do not want to
connect a work source.

For a manual installation, copy the complete `skills/automation-mining/` folder
into your agent's skills directory. Include the `references/` and `agents/`
folders and `LICENSE`; copying only `SKILL.md` is not sufficient. Save any local
edits before replacing an existing installation. The [ZIP section](#zip-download)
lists common destination directories.

## Skills CLI

Use Node.js and Git:

```sh
npx skills@latest add n8n-io/automation-mining-skill --skill automation-mining
```

Select your agent and installation scope. Start a new session, then ask the
agent to use automation-mining. See the [Skills CLI documentation](https://www.skills.sh/docs).

## Claude Code plugin

Run these commands inside Claude Code:

```text
/plugin marketplace add n8n-io/automation-mining-skill
/plugin install automation-mining@n8n-automation-mining
```

Start a new session, then use `/automation-mining:automation-mining`.
See the [Claude Code plugin guide](https://code.claude.com/docs/en/discover-plugins).

## Codex plugin

This route requires a client with plugin support.

Run these commands in your terminal:

```sh
codex plugin marketplace add n8n-io/automation-mining-skill
codex plugin add automation-mining@n8n-automation-mining
```

Start a new session, then select **Automation mining** in the skill picker.
The marketplace pins the package to its release tag. Use Skills CLI if your
client does not support plugins. See the [Codex plugin guide](https://developers.openai.com/codex/plugins).

## Pi package

```sh
pi install git:github.com/n8n-io/automation-mining-skill
```

Start a new session, then use `/skill:automation-mining`.
The package contains one skill and no executable extension.
See the [Pi package guide](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md).

## ZIP download

Open the [latest release](https://github.com/n8n-io/automation-mining-skill/releases/latest).
Download the skill ZIP and extract its `automation-mining/` folder into your
agent's skills directory:

| Agent | Personal skills directory |
| --- | --- |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.agents/skills/` |
| Pi | `~/.pi/agent/skills/` |

The skill ZIP includes the skill, its references, display metadata, and license.
The plugin ZIP also includes the plugin manifests, marketplace files, and images.
The whitepaper is a separate PDF download.

Download `SHA256SUMS` and the three release files to one folder. Check them on macOS:

```sh
shasum -a 256 -c SHA256SUMS
```

On Linux, use `sha256sum -c SHA256SUMS`.

On Windows, run this in PowerShell from the download folder. It stops if a
file is missing or its checksum does not match:

```powershell
Get-Content .\SHA256SUMS | ForEach-Object {
    $expected, $name = $_ -split '  ', 2
    $actual = (Get-FileHash -LiteralPath $name -Algorithm SHA256 -ErrorAction Stop).Hash
    if ($actual -ne $expected) { throw "Checksum mismatch: $name" }
    Write-Output "OK: $name"
}
```

## Update or remove

Use the route you used to install:

| Route | Update | Remove |
| --- | --- | --- |
| Skills CLI | `npx skills update` (all installed skills) | `npx skills remove automation-mining` |
| Claude Code | `/plugin update automation-mining@n8n-automation-mining` | `/plugin uninstall automation-mining@n8n-automation-mining` |
| Codex | Refresh the marketplace and reinstall; see below | `codex plugin remove automation-mining@n8n-automation-mining` |
| Pi | `pi update git:github.com/n8n-io/automation-mining-skill` | `pi remove git:github.com/n8n-io/automation-mining-skill` |
| ZIP | Save local edits, then replace the installed folder | Delete the installed `automation-mining/` folder |

To update the Codex package:

```sh
codex plugin marketplace upgrade n8n-automation-mining
codex plugin add automation-mining@n8n-automation-mining
```

Start a new session after an update. Reports stay in their output locations.

## Migrate from a development version

Version 1.0.0 stores the skill in `skills/automation-mining/`. If you cloned a
development version directly into your agent's skills directory, save local
edits and move that clone outside the directory. Then install with one route
above. A `git pull` alone does not move the skill to the expected location.

## Check the installation

Start a new session and ask the agent to use `automation-mining`. Confirm that
it can read the skill and its reference files. Run the synthetic example before
connecting work data. Python is needed only for the example checker and package
tests, not for the skill itself.

## If installation fails

| Symptom | What to check |
| --- | --- |
| Repository not found | Confirm that your Git client has access to this repository. |
| Codex cannot find `v1.0.0` | Check repository access and update the marketplace. Use local files if needed. |
| The agent cannot find the skill | Start a new session. Check the installation scope and client support. |
| More than one copy appears | Keep one installation route. Remove the extra copy with its installer. |
| A reference file is missing | Reinstall the complete skill folder, including `references/`. |
| A source cannot be read | Configure that connection in your agent and confirm read access. The skill does not add connectors. |

If the problem remains, [report it](https://github.com/n8n-io/automation-mining-skill/issues/new?template=feedback.yml)
with the agent version and installation route. Do not include credentials,
private records, or a session export.
