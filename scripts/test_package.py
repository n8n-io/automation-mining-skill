"""Check release identity and archive contents."""
import tempfile
import shutil
import hashlib
import unittest
from unittest.mock import patch
import zipfile
from pathlib import Path

import package


class PackageTests(unittest.TestCase):
    def test_release_excludes_local_files_and_checks_all_downloads(self):
        with tempfile.TemporaryDirectory() as directory:
            value = package.version()
            root = Path(directory) / 'source'
            shutil.copytree(package.ROOT, root, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))
            for name in ['skills/automation-mining/.env', 'assets/local-notes.md', '.codex-plugin/debug.json']:
                (root / name).write_text('local data', encoding='utf-8')
            with patch.object(package, 'ROOT', root):
                package.build()
                first = {p.name: p.read_bytes() for p in (root / 'dist').iterdir()}
                package.build()
            self.assertEqual(first, {p.name: p.read_bytes() for p in (root / 'dist').iterdir()})
            for suffix, expected in [(f'v{value}', package.SKILL_FILES), (f'plugin-v{value}', package.PLUGIN_FILES)]:
                with zipfile.ZipFile(root / f'dist/automation-mining-{suffix}.zip') as archive:
                    destinations = [Path('automation-mining') / (p.relative_to(package.SKILL)
                                    if suffix == f'v{value}' else p) for p in expected]
                    self.assertEqual(archive.namelist(), sorted(p.as_posix() for p in destinations))
                    self.assertTrue(all(b'local data' != archive.read(name) for name in archive.namelist()))
            for line in (root / 'dist/SHA256SUMS').read_text().splitlines():
                digest, name = line.split('  ')
                self.assertEqual(digest, hashlib.sha256((root / 'dist' / name).read_bytes()).hexdigest())
            self.assertEqual((root / f'dist/automation-mining-paper-v{value}.pdf').read_bytes(),
                             (root / 'paper/taxonomy_skill.pdf').read_bytes())
            self.assertNotRegex((root / 'dist/RELEASE_NOTES.md').read_text(), r'\]\((?:docs/|METHOD)')

    def test_links_require_existing_files_and_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'README.md'
            with patch.object(package, 'ROOT', root):
                path.write_text('# Quick start\n[Start](#quick-start)\n', encoding='utf-8')
                package.check_links(path)
                for link in ['#missing', 'missing.md', 'README.md#missing']:
                    path.write_text(f'# Quick start\n[Start]({link})\n', encoding='utf-8')
                    with self.assertRaisesRegex(ValueError, 'Broken'):
                        package.check_links(path)

    def test_wrong_release_tag_fails(self):
        with self.assertRaisesRegex(ValueError, 'does not match'):
            package.check('v999.0.0')

    def test_archive_is_reproducible_and_contains_source_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = [Path(directory) / name for name in ['first.zip', 'second.zip']]
            entries = [(package.SKILL / 'SKILL.md', 'automation-mining/SKILL.md')]
            package.archive(first, entries)
            package.archive(second, entries)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), ['automation-mining/SKILL.md'])
                self.assertEqual(archive.read(archive.namelist()[0]),
                                 (package.ROOT / entries[0][0]).read_bytes())

    def test_sync_preserves_utf8_and_lf(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / package.SKILL).mkdir(parents=True)
            (root / '.agents/plugins').mkdir(parents=True)
            (root / 'package.json').write_text('{"version":"1.0.0"}', encoding='utf-8')
            (root / '.agents/plugins/marketplace.json').write_text('{"plugins":[{"source":{"ref":"main"}}]}', encoding='utf-8')
            (root / 'LICENSE').write_bytes(b'MIT License\n')
            for manifest in package.MANIFESTS:
                path = root / manifest
                path.parent.mkdir()
                path.write_text('{"version":"0.5.0"}', encoding='utf-8')
            skill = root / package.SKILL / 'SKILL.md'
            skill.write_bytes('---\nmetadata:\n  version: "0.5.0"\n---\nCafé → report\n'.encode('utf-8'))
            with patch.object(package, 'ROOT', root):
                package.sync()
            self.assertIn('Café → report'.encode('utf-8'), skill.read_bytes())
            self.assertIn(b'version: "1.0.0"', skill.read_bytes())
            self.assertNotIn(b'\r', skill.read_bytes())
            self.assertEqual((root / package.SKILL / 'LICENSE').read_bytes(), b'MIT License\n')


if __name__ == '__main__':
    unittest.main()
