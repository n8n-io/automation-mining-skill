"""Check the example report and reject incorrect counts or evidence."""
import json
import unittest
from copy import deepcopy
from pathlib import Path

from check_example import check_report

ROOT = Path(__file__).resolve().parents[1]
REPORT = json.loads((ROOT / 'examples/laptop-requests/expected-report.json').read_text(encoding="utf-8"))


class ExampleTests(unittest.TestCase):
    def test_expected_report(self):
        check_report(REPORT)

    def test_duplicate_request_is_not_another_instance(self):
        report = deepcopy(REPORT)
        report['proposals'][0]['work_instances'].append(report['proposals'][0]['work_instances'][0])
        report['proposals'][0]['claimed_occurrences'] = 4
        with self.assertRaises(ValueError):
            check_report(report)

    def test_invented_citation_fails(self):
        report = deepcopy(REPORT)
        report['proposals'][0]['work_instances'][0]['evidence'].append('invented-source')
        with self.assertRaises(ValueError):
            check_report(report)

    def test_routine_activity_has_no_proposal(self):
        check_report({'proposals': []}, routine_only=True)
        with self.assertRaises(ValueError):
            check_report(REPORT, routine_only=True)

    def test_missing_task_fails(self):
        with self.assertRaises(ValueError):
            check_report({'proposals': []})
