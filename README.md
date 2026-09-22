# Automation mining

Find repeated manual work in activity records and propose automations with
source evidence. The owner reviews each proposal and chooses what to build.

## Use the skill

Give your agent [the skill](skills/automation-mining/SKILL.md) and a set of
activity records. Ask it to find repeated manual work in those records.
The skill returns up to five proposals with source references and work counts.
It can return no proposals when the records do not support a useful change.

The package contains instructions. Your agent supplies access to data and tools.
Review tool permissions before you connect a source. Building an automation is
a separate task after review.

Available under the [MIT License](LICENSE).

Try the [synthetic laptop example](examples/laptop-requests/README.md) without a connection.

Read the [method and limits](METHOD.md), [paper](paper/taxonomy_skill.pdf), and
[study records](research/README.md). The study uses synthetic activity. It does
not measure time saved in use.
