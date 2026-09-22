"""Check counts and citations in a report for the synthetic laptop example."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_report(report, routine_only=False):
    if set(report) != {'proposals'} or not isinstance(report['proposals'], list):
        raise ValueError('Return one proposals array.')
    proposals = report['proposals']
    if routine_only:
        if proposals:
            raise ValueError('The routine-only records support no proposal.')
        return
    if len(proposals) != 1:
        raise ValueError('The laptop example supports one proposal.')
    proposal = proposals[0]
    schema = json.loads((ROOT / 'skills/automation-mining/references/workflow-discovery.schema.json').read_text(encoding="utf-8"))
    fields = schema['properties']['proposals']['items']
    if set(proposal) != set(fields['required']):
        raise ValueError('The proposal fields do not match the report schema.')
    for field, rule in fields['properties'].items():
        if rule.get('type') == 'string' and not isinstance(proposal[field], str):
            raise ValueError(f'{field} must be a string.')
    if proposal['kind'] != 'build' or type(proposal['claimed_occurrences']) is not int or proposal['claimed_occurrences'] != 3:
        raise ValueError('Count the three distinct laptop requests.')
    instances = proposal['work_instances']
    if not isinstance(instances, list) or len(instances) != 3:
        raise ValueError('List one instance for each of the three requests.')
    seen = set()
    evidence = set()
    for item in instances:
        if set(item) != {'unit_id', 'evidence'}:
            raise ValueError('Each instance needs a unit ID and evidence.')
        unit = item['unit_id']
        if unit not in {'LAP-001', 'LAP-002', 'LAP-003'} or unit in seen:
            raise ValueError('Use each observed LAP request ID exactly once.')
        seen.add(unit)
        n = int(unit[-1])
        allowed = {f'slack-request-{n}', f'slack-copy-{n}', f'linear-ticket-{n}'}
        citations = item['evidence']
        if not isinstance(citations, list) or not all(isinstance(x, str) for x in citations):
            raise ValueError('Citations must be an array of source IDs.')
        if len(citations) != len(set(citations)) or not set(citations) <= allowed or f'slack-copy-{n}' not in citations:
            raise ValueError('Cite the human copy operation and only records for that request.')
        evidence.update(citations)
    citations = proposal['evidence']
    if not isinstance(citations, list) or not all(isinstance(x, str) for x in citations):
        raise ValueError('Proposal evidence must be an array of source IDs.')
    if set(citations) != evidence or len(citations) != len(evidence):
        raise ValueError('Proposal evidence must be the distinct union of instance citations.')
    unknowns = proposal['material_unknowns']
    if not isinstance(unknowns, list) or not unknowns or not all(isinstance(x, str) for x in unknowns):
        raise ValueError('List the material unknowns.')


if __name__ == '__main__':
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != '--routine-only'):
        raise SystemExit('Usage: python3 scripts/check_example.py report.json [--routine-only]')
    check_report(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")), routine_only=len(sys.argv) == 3)
    print('Example counts and citations pass. Review the proposed operation and remaining human work manually.')
