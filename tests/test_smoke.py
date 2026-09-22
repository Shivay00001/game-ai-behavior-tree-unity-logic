"""Minimal smoke tests for the behavior-tree library (no external deps)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.behavior_tree import Selector, Sequence, Action, Condition, NodeStatus
from src.npc import NPC


class TestBehaviorTree(unittest.TestCase):
    def test_sequence_success(self):
        seq = Sequence([Action(lambda bb: NodeStatus.SUCCESS),
                        Action(lambda bb: NodeStatus.SUCCESS)])
        self.assertEqual(seq.tick({}), NodeStatus.SUCCESS)

    def test_sequence_short_circuits(self):
        seq = Sequence([Action(lambda bb: NodeStatus.FAILURE),
                        Action(lambda bb: NodeStatus.SUCCESS)])
        self.assertEqual(seq.tick({}), NodeStatus.FAILURE)

    def test_selector_fallback(self):
        sel = Selector([Action(lambda bb: NodeStatus.FAILURE),
                        Action(lambda bb: NodeStatus.SUCCESS)])
        self.assertEqual(sel.tick({}), NodeStatus.SUCCESS)

    def test_condition(self):
        self.assertEqual(Condition(lambda bb: True).tick({}), NodeStatus.SUCCESS)
        self.assertEqual(Condition(lambda bb: False).tick({}), NodeStatus.FAILURE)

    def test_npc_guard_tree(self):
        guard = NPC("Guard_01")
        tree = Selector([
            Sequence([Condition(guard.sees_enemy), Action(guard.attack)]),
            Action(guard.patrol),
        ])
        status = tree.tick({})
        self.assertIn(status, (NodeStatus.SUCCESS, NodeStatus.FAILURE,
                               NodeStatus.RUNNING))


if __name__ == "__main__":
    unittest.main()
