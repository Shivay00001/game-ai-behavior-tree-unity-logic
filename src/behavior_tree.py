from enum import Enum, auto

class NodeStatus(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    RUNNING = auto()

class Node:
    def tick(self, blackboard) -> NodeStatus:
        raise NotImplementedError

# --- Composites ---
class Selector(Node):
    """Or / Fallback node."""
    def __init__(self, children):
        self.children = children

    def tick(self, blackboard):
        for child in self.children:
            status = child.tick(blackboard)
            if status != NodeStatus.FAILURE:
                return status
        return NodeStatus.FAILURE

class Sequence(Node):
    """And node."""
    def __init__(self, children):
        self.children = children

    def tick(self, blackboard):
        for child in self.children:
            status = child.tick(blackboard)
            if status != NodeStatus.SUCCESS:
                return status
        return NodeStatus.SUCCESS

# --- Leaves ---
class Action(Node):
    def __init__(self, func):
        self.func = func

    def tick(self, blackboard):
        return self.func(blackboard)

class Condition(Node):
    def __init__(self, func):
        self.func = func

    def tick(self, blackboard):
        if self.func(blackboard):
            return NodeStatus.SUCCESS
        return NodeStatus.FAILURE
