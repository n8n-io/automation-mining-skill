# Security

Review the skill instructions and the permissions of
your agent before you connect activity sources.

## Report a vulnerability

Follow [n8n's security reporting instructions](https://github.com/n8n-io/n8n/blob/master/SECURITY.md).
Include the affected skill version, the impact, and steps that reproduce the
problem with synthetic data. Do not put credentials or private activity in a
public issue.

## Access to activity

The skill instructs the agent to use read access while mining. It does not
enforce tool permissions. Your agent and model provider can process source
data under your account settings. Set access limits in the connected tools.

Reports must use source pointers and counts instead of copied message bodies,
personal data, or credentials. Review a report before you share it.
