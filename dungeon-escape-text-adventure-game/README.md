# 🏰 Dungeon Escape - A Text Adventure Game

A classic dungeon crawler text adventure game built with Python. Navigate through rooms, collect items, survive random encounters, and escape the dungeon!

## 📖 About This Project

This game is the capstone project from **Chapter 15** of the book *"Zero to AI Engineer: Python Foundations"*. It consolidates core Python concepts from Part 2 of the book into a fully playable game.

### Concepts Demonstrated

| Concept | How It's Used |
|:--------|:--------------|
| **Variables & Data Types** | Game state, room data, player info |
| **Dictionaries** | Nested data for rooms and player state |
| **Operators** | Health checks, item membership testing |
| **String Methods** | F-strings, `.strip()`, `.lower()`, `.split()`, `.join()` |
| **User Input** | Interactive `input()` game loop |
| **Conditionals** | `if-elif-else` and `match/case` for commands |
| **While Loops** | Main game loop |
| **For Loops** | Iterating inventory with `enumerate()` |
| **Type Hints** | Function signatures and variable annotations |

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (required for `match/case` syntax)
- No external dependencies required!

### Running the Game

```bash
# Clone this repository
git clone <repository-url>
cd dungeon-escape-text-adventure

# Run the game
python adventure_game.py
```

## 🎮 How to Play

### Commands

| Command | Description |
|:--------|:------------|
| `go <direction>` | Move north, south, east, or west |
| `take <item>` | Pick up an item from the room |
| `use <item>` | Use an item from your inventory |
| `inventory` | View items you're carrying |
| `look` | Look around the current room |
| `help` | Show available commands |
| `quit` | Exit the game |

### Tips

- **Explore thoroughly** - Visit all rooms to find useful items
- **Health matters** - Random events can hurt or heal you
- **Use items wisely** - The `health_potion` restores 30 HP
- **Check the map** - Use it to see the dungeon layout

### Sample Gameplay

```text
========================================
       DUNGEON ESCAPE
========================================

You wake up in a dark dungeon.
Find the exit to escape!
Type 'help' for available commands.


You are in the Entrance Hall.
A dusty entrance with cobwebs covering the walls.
A faint light flickers from the north.

Exits: north, east
Items here: torch

Health: 100 | Inventory: empty

What do you do? > take torch
You picked up the torch.

What do you do? > go north
You head north...

You are in the Dark Corridor.
...
```

## 🗺️ Dungeon Map

```
                    [EXIT]
                      ↑
              [Treasure Room]
                      ↑
[Library] ←→ [Dark Corridor]
                      ↑
[Armory] ←→ [Entrance Hall] ← START
```

## 🧪 Practice Exercises

Want to extend the game? Try these challenges:

### 1. Add a New Room
Add a "dungeon_cell" room connected to the corridor containing a "rusty_key" item.

### 2. Implement a Puzzle Mechanic
Make the exit door locked - require the "gold_key" to open it.

### 3. Add a Scoring System
Track points for:
- +10 for each item collected
- +50 for winning
- -5 for damage taken

### 4. Create More Random Events
Add interesting events that affect inventory or have larger consequences.

## 📚 Learning More

This project is part of **"Zero to AI Engineer: Python Foundations"**:

- **Part 2** (Chapters 6-14) covers the foundations used here
- **Part 4** will teach functions for better code organization
- **Chapter 22** covers JSON for save/load functionality
- **Chapter 44** introduces error handling

## 🤝 Contributing

Feel free to fork this project and add your own features! Ideas:
- Combat system
- Multiple dungeon levels
- Save/load game state
- More items and puzzles

## 📄 License

This project is open source and available under the MIT License.

---

Built with ❤️ as part of the *Zero to AI Engineer: Python Foundations* book.
