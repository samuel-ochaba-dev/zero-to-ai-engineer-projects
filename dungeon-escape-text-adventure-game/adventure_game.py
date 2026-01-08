# ============================================
# DUNGEON ESCAPE - A Text Adventure Game
# ============================================

import random
from typing import Any

# Game configuration constants
STARTING_HEALTH: int = 100
STARTING_ROOM: str = "entrance"
WIN_ROOM: str = "exit"

# Event probabilities (0.0 to 1.0)
EVENT_CHANCE: float = 0.3  # 30% chance of random event each turn

# The game world: rooms with descriptions, exits, and items
ROOMS: dict[str, dict] = {
    "entrance": {
        "name": "Entrance Hall",
        "description": (
            "A dusty entrance with cobwebs covering the walls. "
            "A faint light flickers from the north."
        ),
        "exits": {"north": "corridor", "east": "armory"},
        "items": ["torch"],
    },
    "corridor": {
        "name": "Dark Corridor",
        "description": (
            "A narrow passage stretching into darkness. "
            "You hear strange sounds echoing from the walls."
        ),
        "exits": {
            "south": "entrance",
            "north": "treasure_room",
            "west": "library",
        },
        "items": [],
    },
    "armory": {
        "name": "Old Armory",
        "description": (
            "Rusted weapons line the walls. "
            "Most are useless, but something glints in the corner."
        ),
        "exits": {"west": "entrance"},
        "items": ["sword", "shield"],
    },
    "library": {
        "name": "Ancient Library",
        "description": (
            "Dusty books fill towering shelves. "
            "A strange map lies on a reading table."
        ),
        "exits": {"east": "corridor"},
        "items": ["map", "health_potion"],
    },
    "treasure_room": {
        "name": "Treasure Chamber",
        "description": (
            "Gold coins and jewels are scattered everywhere! "
            "A heavy door to the north looks like the way out."
        ),
        "exits": {"south": "corridor", "north": "exit"},
        "items": ["gold_key"],
    },
    "exit": {
        "name": "Freedom!",
        "description": (
            "Sunlight streams through an open doorway. " "You've found the exit!"
        ),
        "exits": {},
        "items": [],
    },
}

# Player state (mutable during gameplay)
player: dict[str, Any] = {
    "current_room": STARTING_ROOM,
    "inventory": [],
    "health": STARTING_HEALTH,
}


def display_room() -> None:
    """Display the current room information to the player."""
    room_id = player["current_room"]
    room = ROOMS[room_id]

    print(f"\nYou are in the {room['name']}.")
    print(room["description"])

    # Show available exits
    exits = room["exits"]
    if exits:
        exit_list = ", ".join(exits.keys())
        print(f"\nExits: {exit_list}")
    else:
        print("\nThere are no exits.")

    # Show items in the room
    items = room["items"]
    if items:
        item_list = ", ".join(items)
        print(f"Items here: {item_list}")
    else:
        print("Items here: none")


def display_status() -> None:
    """Display the player's current status."""
    health = player["health"]
    inventory = player["inventory"]

    if inventory:
        inv_str = ", ".join(inventory)
    else:
        inv_str = "empty"

    print(f"\nHealth: {health} | Inventory: {inv_str}")


def process_go(direction: str) -> bool:
    """
    Try to move the player in the given direction.
    Returns True if movement was successful, False otherwise.
    """
    room_id = player["current_room"]
    room = ROOMS[room_id]
    exits = room["exits"]

    if direction in exits:
        new_room = exits[direction]
        player["current_room"] = new_room
        print(f"You head {direction}...")
        return True
    else:
        valid_exits = ", ".join(exits.keys()) if exits else "none"
        print(f"You can't go {direction}. Available exits: {valid_exits}")
        return False


def process_take(item_name: str) -> bool:
    """
    Try to pick up an item from the current room.
    Returns True if successful, False otherwise.
    """
    room_id = player["current_room"]
    room = ROOMS[room_id]
    items = room["items"]

    if item_name in items:
        items.remove(item_name)
        player["inventory"].append(item_name)
        print(f"You picked up the {item_name}.")
        return True
    else:
        print(f"There's no {item_name} here.")
        return False


def process_use(item_name: str) -> bool:
    """
    Try to use an item from inventory.
    Returns True if successful, False otherwise.
    """
    inventory = player["inventory"]

    if item_name not in inventory:
        print(f"You don't have a {item_name}.")
        return False

    if item_name == "health_potion":
        inventory.remove("health_potion")
        heal_amount = 30
        player["health"] = min(player["health"] + heal_amount, STARTING_HEALTH)
        print(f"You drink the health potion and restore {heal_amount} health!")
        return True
    elif item_name == "torch":
        print("The torch illuminates your surroundings. It's already lit.")
        return True
    elif item_name == "map":
        print("The map shows the dungeon layout:")
        print("  Entrance -> Corridor -> Treasure Room -> Exit")
        print("  Entrance -> Armory")
        print("  Corridor -> Library")
        return True
    else:
        print(f"You're not sure how to use the {item_name}.")
        return False


def process_inventory() -> None:
    """Display the player's inventory."""
    inventory = player["inventory"]

    if not inventory:
        print("Your inventory is empty.")
        return

    print("You are carrying:")
    for i, item in enumerate(inventory, start=1):
        print(f"  {i}. {item}")


def show_help() -> None:
    """Display available commands."""
    print("\n=== AVAILABLE COMMANDS ===")
    print("  go <direction>  - Move (north, south, east, west)")
    print("  take <item>     - Pick up an item")
    print("  use <item>      - Use an item from inventory")
    print("  inventory       - View your inventory")
    print("  look            - Look around")
    print("  help            - Show this help")
    print("  quit            - Exit the game")


def trigger_random_event() -> None:
    """Possibly trigger a random event based on EVENT_CHANCE."""
    if random.random() > EVENT_CHANCE:
        return

    events = [
        ("monster", "A giant spider attacks! You lose 15 health.", -15),
        ("monster", "A goblin jumps from the shadows! You lose 20 health.", -20),
        ("trap", "You trigger a dart trap! You lose 10 health.", -10),
        ("treasure", "You find some gold coins! (+10 health from morale)", 10),
        ("potion", "You discover a small healing vial! (+15 health)", 15),
        ("nothing", "You hear a distant rumble... but nothing happens.", 0),
    ]

    event_type, message, health_change = random.choice(events)

    print(f"\n*** {message} ***")

    if health_change != 0:
        player["health"] += health_change
        player["health"] = min(player["health"], STARTING_HEALTH)


def main() -> None:
    """Main game loop."""
    print("\n" + "=" * 40)
    print("       DUNGEON ESCAPE")
    print("=" * 40)
    print("\nYou wake up in a dark dungeon.")
    print("Find the exit to escape!")
    print("Type 'help' for available commands.\n")

    game_running = True

    while game_running:
        if player["current_room"] == WIN_ROOM:
            display_room()
            print("\n*** CONGRATULATIONS! You escaped the dungeon! ***")
            break

        if player["health"] <= 0:
            print("\n*** GAME OVER! You have perished in the dungeon. ***")
            break

        display_room()
        display_status()

        command = input("\nWhat do you do? > ").strip().lower()

        if not command:
            continue

        parts = command.split(maxsplit=1)
        action = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        moved = False

        match action:
            case "go" | "move" | "walk":
                if argument:
                    moved = process_go(argument)
                else:
                    print("Go where? Specify a direction.")

            case "take" | "get" | "grab" | "pick":
                if argument:
                    process_take(argument)
                else:
                    print("Take what? Specify an item.")

            case "use":
                if argument:
                    process_use(argument)
                else:
                    print("Use what? Specify an item.")

            case "inventory" | "inv" | "i":
                process_inventory()

            case "look" | "l":
                pass

            case "help" | "h" | "?":
                show_help()

            case "quit" | "exit" | "q":
                print("Thanks for playing! Goodbye.")
                game_running = False

            case _:
                print(f"I don't understand '{command}'. Type 'help'.")

        if moved:
            trigger_random_event()


if __name__ == "__main__":
    main()
