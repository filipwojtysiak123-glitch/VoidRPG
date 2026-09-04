import os
import time
import sys
import config

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def simulate_thinking(seconds=1, message="Thinking..."):
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(int(seconds / 0.2)):
        time.sleep(0.2)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()

def show_stats():
    import leveling
    req_exp = leveling.get_required_exp(config.player["level"])
    print("=" * 85)
    print(f" Hero: {config.player['name']} | LVL: {config.player['level']} ({config.player['exp']}/{req_exp} XP)")
    print(f" HP: {config.player['hp']}/{config.player['max_hp']} | MP: {config.player['mp']}/{config.player['max_mp']} | Gold: {config.player['gold']} | Souls: {config.player['soul_shards']}/2")
    inv_content = ", ".join(config.player["inventory"]) if config.player["inventory"] else "Empty"
    print(f" Bag: {inv_content}")
    print("=" * 85)

def choose_save_slot(title_message):
    while True:
        clear()
        print(f"=== {title_message} ===")
        for i in range(1, 4):
            path = config.get_save_path(i)
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        name = f.readline().strip()
                    print(f"{i}. Slot {i} [Hero: {name}]")
                except Exception:
                    print(f"{i}. Slot {i} [Occupied]")
            else:
                print(f"{i}. Slot {i} [Empty]")
        print("4. Cancel")
        print("=======================")
        choice = input("Choose slot (1-4): ").strip()
        if choice in ["1", "2", "3"]: return int(choice)
        elif choice == "4": return None

def save_game():
    slot = choose_save_slot("SAVE GAME")
    if slot is None: return
    save_file_path = config.get_save_path(slot)
    clear()
    simulate_thinking(1, f"Saving game to Slot {slot}")
    try:
        with open(save_file_path, "w", encoding="utf-8") as file:
            file.write(f"{config.player['name']}\n")
            file.write(f"{config.player['hp']}\n")
            file.write(f"{config.player['max_hp']}\n")
            file.write(f"{config.player['mp']}\n")
            file.write(f"{config.player['max_mp']}\n")
            file.write(f"{config.player['gold']}\n")
            file.write(f"{config.player['level']}\n")
            file.write(f"{config.player['exp']}\n")          
            file.write(f"{config.player['progress']}\n")
            file.write(f"{config.player['soul_shards']}\n")
            file.write(f"{config.player['weapon_dmg']}\n")    
            lore_string = ",".join(str(x) for x in config.player["discovered_lore"])
            file.write(f"{lore_string}\n")
            inv_string = ",".join(config.player["inventory"])
            file.write(f"{inv_string}\n")
        slow_print(f"\n[Game successfully saved in Slot {slot}!]")
        time.sleep(1)
    except Exception as e:
        print(f"\n[Save Error: {e}]")
        input("Press ENTER...")

def load_game():
    slot = choose_save_slot("LOAD GAME")
    if slot is None: return False
    save_file_path = config.get_save_path(slot)
    if not os.path.exists(save_file_path):
        clear()
        print(f"\n[Slot {slot} is empty! Cannot load.]")
        input("\nPress ENTER...")
        return False
    clear()
    simulate_thinking(1, f"Loading save from Slot {slot}")
    try:
        with open(save_file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines) >= 13:
                config.player["name"] = lines[0]
                config.player["hp"] = int(lines[1])
                config.player["max_hp"] = int(lines[2])
                config.player["mp"] = int(lines[3])
                config.player["max_mp"] = int(lines[4])
                config.player["gold"] = int(lines[5])
                config.player["level"] = int(lines[6])
                config.player["exp"] = int(lines[7])          
                config.player["progress"] = int(lines[8])
                config.player["soul_shards"] = int(lines[9])
                config.player["weapon_dmg"] = int(lines[10])   
                
                lore_line = lines[11]
                if lore_line:
                    config.player["discovered_lore"] = [int(x) for x in lore_line.split(",") if x]
                else:
                    config.player["discovered_lore"] = []
                    
                inv_line = lines[12]
                if inv_line:
                    config.player["inventory"] = [x for x in inv_line.split(",") if x]
                else:
                    config.player["inventory"] = []
                return True
    except Exception:
        return False
    return False

