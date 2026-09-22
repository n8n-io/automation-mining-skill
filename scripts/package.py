"""Check versions and build reproducible skill and plugin archives."""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/automation-mining')
MANIFESTS = ['.claude-plugin/plugin.json', '.codex-plugin/plugin.json']
SKILL_FILES = [SKILL / name for name in [
    'SKILL.md', 'LICENSE', 'agents/openai.yaml',
    'references/feedback.md', 'references/trails.md', 'references/worker-brief.md',
    'references/workflow-discovery.md', 'references/workflow-discovery.artifact.json',
    'references/workflow-discovery.schema.json',
]]
PLUGIN_FILES = SKILL_FILES + [Path(name) for name in [
    *MANIFESTS, '.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json',
    'package.json', 'LICENSE', 'assets/icon.png', 'assets/screenshot.png',
]]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def version():
    value = read_json('package.json')['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', value):
        raise ValueError('Use a version in X.Y.Z format.')
    return value


def sync():
    value = version()
    for path in MANIFESTS:
        data = read_json(path)
        data['version'] = value
        (ROOT / path).write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8', newline='\n')
    marketplace_path = '.agents/plugins/marketplace.json'
    marketplace = read_json(marketplace_path)
    marketplace['plugins'][0]['source']['ref'] = f'v{value}'
    (ROOT / marketplace_path).write_text(json.dumps(marketplace, indent=2) + '\n', encoding='utf-8', newline='\n')
    path = ROOT / SKILL / 'SKILL.md'
    text, count = re.subn(r'(?m)^  version: "[^"\n]+"$', f'  version: "{value}"', path.read_text(encoding="utf-8"), count=1)
    if count != 1:
        raise ValueError('The skill must have one metadata version.')
    path.write_text(text, encoding='utf-8', newline='\n')
    (ROOT / SKILL / 'LICENSE').write_bytes((ROOT / 'LICENSE').read_bytes())


def files_under(path):
    return sorted(p.relative_to(ROOT) for p in (ROOT / path).rglob('*') if p.is_file())


def check_links(path):
    text = (ROOT / path).read_text(encoding='utf-8')
    links = re.findall(r'\]\(([^\s)]+)\)', text) + re.findall(r'(?:src|href)="([^"]+)"', text)
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (ROOT / path).parent / unquote(url.path) if url.path else ROOT / path
        if not target.exists():
            raise ValueError(f'Broken link in {path}: {link}')
        if url.fragment and target.suffix == '.md':
            content = target.read_text(encoding='utf-8')
            headings = re.findall(r'^#{1,6} (.+)$', content, re.MULTILINE)
            anchors = {re.sub(r'[^\w -]', '', title.lower()).replace(' ', '-') for title in headings}
            anchors.update(re.findall(r'id="([^"]+)"', content))
            if unquote(url.fragment) not in anchors:
                raise ValueError(f'Broken heading link in {path}: {link}')


def check(tag=None):
    value = version()
    if tag and tag != f'v{value}':
        raise ValueError(f'Tag {tag} does not match v{value}.')
    if read_json('.agents/plugins/marketplace.json')['plugins'][0]['source']['ref'] != f'v{value}':
        raise ValueError('The Codex source must match the release tag.')
    for path in MANIFESTS:
        data = read_json(path)
        if data['version'] != value or data['name'] != 'automation-mining':
            raise ValueError(f'Incorrect name or version: {path}')
    text = (ROOT / SKILL / 'SKILL.md').read_text(encoding="utf-8")
    if not text.startswith('---\nname: automation-mining\n') or f'  version: "{value}"\n' not in text:
        raise ValueError('Incorrect skill metadata.')
    if read_json('package.json')['pi'] != {'skills': ['./skills']}:
        raise ValueError('The Pi package must contain only skills.')
    if read_json(MANIFESTS[0])['skills'] != ['./skills/automation-mining']:
        raise ValueError('Incorrect Claude Code skill path.')
    if read_json(MANIFESTS[1])['skills'] != './skills/':
        raise ValueError('Incorrect Codex skill path.')
    if (ROOT / SKILL / 'LICENSE').read_bytes() != (ROOT / 'LICENSE').read_bytes():
        raise ValueError('The skill license differs from the repository license.')
    for path in PLUGIN_FILES:
        source = ROOT / path
        if any((ROOT / p).is_symlink() for p in [path, *path.parents]):
            raise ValueError(f'Packages cannot contain symlinks: {path}')
        if not source.is_file():
            raise ValueError(f'Missing package file: {path}')
    for path, record in read_json('research/manifest.json')['files'].items():
        content = (ROOT / path).read_bytes()
        if hashlib.sha256(content).hexdigest() != record['sha256'] or len(content) != record['bytes']:
            raise ValueError(f'Research file differs from its source: {path}')
    for path in [*ROOT.glob('*.md'), *files_under(SKILL), *files_under('docs'),
                 *files_under('examples'), *files_under('research')]:
        if path.suffix != '.md':
            continue
        check_links(path)
    print(f'Package v{value}: versions, paths, links, and research hashes pass.')


def archive(path, entries):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as output:
        for source, destination in sorted(entries, key=lambda item: item[1]):
            info = zipfile.ZipInfo(destination, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            output.writestr(info, (ROOT / source).read_bytes())
    with zipfile.ZipFile(path) as output:
        if output.testzip() is not None:
            raise ValueError(f'Invalid archive: {path}')
        for source, destination in entries:
            if output.read(destination) != (ROOT / source).read_bytes():
                raise ValueError(f'Archive content differs: {destination}')


def build():
    check()
    value = version()
    out = ROOT / 'dist'
    out.mkdir(exist_ok=True)
    for old in out.glob('automation-mining-*.zip'):
        old.unlink()
    skill_zip = out / f'automation-mining-v{value}.zip'
    archive(skill_zip, [(p, (Path('automation-mining') / p.relative_to(SKILL)).as_posix()) for p in SKILL_FILES])
    plugin_zip = out / f'automation-mining-plugin-v{value}.zip'
    archive(plugin_zip, [(p, (Path('automation-mining') / p).as_posix()) for p in PLUGIN_FILES])
    paper = out / f'automation-mining-paper-v{value}.pdf'
    paper.write_bytes((ROOT / 'paper/taxonomy_skill.pdf').read_bytes())
    checksums = out / 'SHA256SUMS'
    checksums.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n'
                                for p in [skill_zip, plugin_zip, paper]), encoding='utf-8', newline='\n')
    changelog = (ROOT / 'CHANGELOG.md').read_text(encoding="utf-8")
    entry = changelog.split(f'## v{value} — ', 1)[1].split('\n', 1)[1].split('\n## ', 1)[0].strip()
    entry = re.sub(r'\]\((?![a-z]+:|#)([^)]+)\)',
                   rf'](https://github.com/n8n-io/automation-mining-skill/blob/v{value}/\1)', entry)
    (out / 'RELEASE_NOTES.md').write_text(
        f'# Automation mining v{value}\n\n'
        'Find repeated manual work in activity records and choose what to automate.\n\n'
        + entry + '\n\nDownload the skill ZIP for manual installation or the plugin ZIP '
        'for native packages. The paper is a separate PDF. Verify the downloads with SHA256SUMS. '
        f'See the [README](https://github.com/n8n-io/automation-mining-skill/blob/v{value}/README.md) '
        'for installation instructions.\n', encoding='utf-8', newline='\n')
    print(f'Built {skill_zip.name}, {plugin_zip.name}, the paper, checksums, and release notes.')


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if command == 'check':
        check(sys.argv[2] if len(sys.argv) > 2 else None)
    elif command == 'sync':
        sync()
    elif command == 'build':
        build()
    else:
        raise SystemExit('Use check [vX.Y.Z], sync, or build.')
