# Game AI Behavior Tree (Unity Logic)

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![AI](https://img.shields.io/badge/Game_AI-Behavior_Trees-red.svg)](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,robotics_and_control))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade Game AI engine** implementing Behavior Trees. This repository demonstrates how to build modular, hierarchical AI for NPCs (Non-Player Characters) typically used in engines like Unity or Unreal.

## 🚀 Features

- **Behavior Tree Nodes**: Implementation of Selector, Sequence, and Leaf nodes.
- **Decorators**: Conditional logic (e.g., Inverter, Timer).
- **Blackboard System**: Shared memory for AI decision making.
- **NPC Simulation**: Detailed Guard AI (Patrol -> Chase -> Attack).

## 📁 Project Structure

```
game-ai-behavior-tree-unity-logic/
├── src/
│   ├── behavior_tree.py  # Core Node Classes
│   ├── npc.py            # Simulation Entities
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/game-ai-behavior-tree-unity-logic.git

# Run AI Simulation
python src/main.py
```

## 📄 License

MIT License
