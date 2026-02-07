import random
from src.behavior_tree import NodeStatus

class NPC:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.target = None
        self.position = 0

    # --- Actions ---
    def patrol(self, bb):
        print(f"[{self.name}] 🛡️ Patrolling area... (Pos: {self.position})")
        self.position += 1
        if random.random() < 0.2:
            print(f"[{self.name}] 👁️ Spotted Player!")
            bb['target_spotted'] = True
            self.target = "Player1"
        return NodeStatus.SUCCESS

    def chase(self, bb):
        print(f"[{self.name}] 🏃 Chasing {self.target}!")
        if random.random() < 0.3:
             print(f"[{self.name}] 🤏 Close enough to attack!")
             bb['in_range'] = True
        return NodeStatus.RUNNING

    def attack(self, bb):
        print(f"[{self.name}] ⚔️ Attacking {self.target}!")
        if random.random() < 0.5:
             print(f"[{self.name}] 💀 Target eliminated.")
             bb['target_spotted'] = False
             bb['in_range'] = False
             self.target = None
             return NodeStatus.SUCCESS
        return NodeStatus.RUNNING

    # --- Conditions ---
    def sees_enemy(self, bb):
        return bb.get('target_spotted', False)

    def in_range(self, bb):
        return bb.get('in_range', False)
