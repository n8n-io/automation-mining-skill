"""Check the tested instruction text against its recorded size and hashes."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillTests(unittest.TestCase):
    def test_recorded_instruction_identity(self):
        references = ROOT / 'skills/automation-mining/references'
        record = json.loads((references / 'workflow-discovery.artifact.json').read_text(encoding='utf-8'))
        content = (references / 'workflow-discovery.md').read_bytes()
        text = content.decode('utf-8')
        guide = text[text.index('# Automation discovery'):].split(
            '\nFind automation candidates in the supplied fictional activity.', 1)[0].strip()
        self.assertEqual(len(guide), record['instructions_characters'])
        self.assertEqual(hashlib.sha256(guide.encode('utf-8')).hexdigest(), record['source_guide_sha256'])
        self.assertEqual(hashlib.sha256(content).hexdigest(), record['skill_file_sha256'])


if __name__ == '__main__':
    unittest.main()
