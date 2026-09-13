"""Regression tests for observable state validation; not legal runtime proof."""
import runpy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBES = runpy.run_path(str(ROOT / 'research/reviews/skill-audit-probes-2026-09-13.py'))
CHECKER = runpy.run_path(str(ROOT / 'scripts/check_runtime_trace.py'))


class StateValidationTests(unittest.TestCase):
    def check(self, events):
        return PROBES['inspect_events'](CHECKER, events)

    def test_stale_and_invalidated_blockers_rejected(self):
        for change in ('STALE', 'INVALIDATE', 'PROPOSITION_STATUS_STALE'):
            with self.subTest(change=change):
                self.assertTrue(self.check(PROBES['terminal_blocker_events'](change)))

    def test_current_blocker_accepted(self):
        self.assertEqual([], self.check(PROBES['terminal_blocker_events'](None)))

    def test_refreshed_blocker_accepted(self):
        events = PROBES['terminal_blocker_events']('STALE')
        events.insert(-2, {'event': 'PROPOSITION_STATUS', 'owner': 'BL7',
                          'proposition_id': 'P-BLOCK', 'status': 'SUPPORTED'})
        self.assertEqual([], self.check(events))

    def test_wrong_owner_rejected(self):
        self.assertTrue(self.check(PROBES['owner_events']('BL5')))

    def test_correct_owner_accepted(self):
        self.assertEqual([], self.check(PROBES['owner_events']('BL6')))

    def test_rejected_foreign_write_does_not_mutate(self):
        events = PROBES['owner_events']('BL5')
        events[-1]['write_result'] = 'REJECTED'
        del events[-1]['committed_state_revision']
        self.assertEqual([], self.check(events))

    def test_reassignment_cannot_launder_foreign_write(self):
        events = PROBES['owner_events']('BL5')
        events.insert(1, {'event': 'OWNER_ASSIGN', 'owner': 'BL5', 'proposition_id': 'P-REL'})
        self.assertTrue(self.check(events))

    def test_unrelated_stale_event_does_not_remove_blocker(self):
        events = PROBES['terminal_blocker_events'](None)
        events.insert(-2, {'event': 'STALE', 'proposition_id': 'P-OTHER'})
        self.assertEqual([], self.check(events))

    def test_reconciled_write_still_requires_owner(self):
        events = PROBES['owner_events']('BL5')
        events[-1]['write_result'] = 'RECONCILED'
        self.assertTrue(self.check(events))

    def test_shared_conflict_and_authority_objects_are_not_bl_propositions(self):
        events = PROBES['owner_events']('BL6')
        events.append({'event': 'STATE_DELTA', 'owner': 'AUTHORITY_RESOLVER',
                       'base_state_revision': 1, 'committed_state_revision': 2,
                       'write_result': 'APPLIED', 'affected_object_ids': ['AR-1']})
        events.append({'event': 'STATE_DELTA', 'owner': 'BL7',
                       'base_state_revision': 2, 'committed_state_revision': 3,
                       'write_result': 'APPLIED', 'affected_object_ids': ['C-1']})
        self.assertEqual([], self.check(events))

    def test_cli_rejects_stale_blocker_and_accepts_current_control(self):
        candidate = subprocess.check_output(
            ['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
        with tempfile.TemporaryDirectory(prefix='vblp-checker-test-') as folder:
            temp = Path(folder)
            oracle = temp / 'synthetic-oracle.json'
            oracle.write_text(json.dumps({'candidate_sha': candidate,
                                         'fixtures': {'SYNTHETIC': {}}}), encoding='utf-8')
            for change, expected in [(None, 0), ('STALE', 1), ('INVALIDATE', 1)]:
                with self.subTest(change=change):
                    events = PROBES['terminal_blocker_events'](change)
                    events = [dict(event, seq=i, run_id='SYNTHETIC',
                                   fixture_id='SYNTHETIC', candidate_sha=candidate,
                                   ts='2026-09-13T00:00:00Z')
                              for i, event in enumerate(events, 1)]
                    trace = temp / 'synthetic-trace.jsonl'
                    trace.write_text('\n'.join(map(json.dumps, events)) + '\n', encoding='utf-8')
                    result = subprocess.run(
                        [sys.executable, str(ROOT / 'scripts/check_runtime_trace.py'),
                         '--repo-root', str(ROOT), '--oracle', str(oracle),
                         '--trace', str(trace)], capture_output=True, text=True)
                    self.assertEqual(expected, result.returncode, result.stdout + result.stderr)
                    self.assertEqual('PASS' if expected == 0 else 'FAIL',
                                     json.loads(result.stdout)['verdict'])


if __name__ == '__main__':
    unittest.main()
