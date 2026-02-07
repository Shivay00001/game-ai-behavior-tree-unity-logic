import time
from src.behavior_tree import Selector, Sequence, Action, Condition
from src.npc import NPC

def main():
    print("--- Game AI Simulation (Guard Behavior Tree) ---")
    
    guard = NPC("Guard_01")
    blackboard = {}

    # Build Tree
    # Root: Selector
    # 1. Combat Sequence (If Sees Enemy AND In Range -> Attack)
    # 2. Chase Sequence (If Sees Enemy -> Chase)
    # 3. Patrol (Default)
    
    attack_seq = Sequence([
        Condition(guard.sees_enemy),
        Condition(guard.in_range),
        Action(guard.attack)
    ])

    chase_seq = Sequence([
        Condition(guard.sees_enemy),
        Action(guard.chase)
    ])

    root = Selector([
        attack_seq,
        chase_seq,
        Action(guard.patrol)
    ])

    # Game Loop
    for frame in range(20):
        print(f"\n--- Frame {frame} ---")
        status = root.tick(blackboard)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
