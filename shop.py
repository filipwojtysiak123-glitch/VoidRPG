import config
import utils
import time
import random

def open_shop():
    """Sklep u kowala z losowym asortymentem i opcją sprzedaży łupów."""
    weapons_pool = [
        {"name": "Rusty Iron Sword", "dmg": 20, "cost": 10},
        {"name": "Steel Longsword", "dmg": 26, "cost": 18},
        {"name": "Champion's Blade", "dmg": 32, "cost": 25},
        {"name": "Void Infused Dagger", "dmg": 38, "cost": 35}
    ]
    
    armors_pool = [
        {"name": "Leather Vest", "max_hp": 120, "cost": 12},
        {"name": "Knight's Iron Plate", "max_hp": 145, "cost": 22},
        {"name": "Guardian's Heavy Armor", "max_hp": 170, "cost": 32},
        {"name": "Ancient Soul Ward Plating", "max_hp": 200, "cost": 45}
    ]
    
    random_weapon = random.choice(weapons_pool)
    random_armor = random.choice(armors_pool)

    while True:
        utils.clear()
        utils.show_stats()
        print("\n=== THE FORGOTTEN BLACKSMITH ===")
        print("1. BUY Gear (Browse today's re-forged weapons and armor)")
        print("2. SELL Items (Sell monster drops for gold)")
        print("3. Exit Shop")
        print("-" * 55)
        
        main_choice = input("Select an option (1-3): ").strip()
        
        if main_choice == "1":
            while True:
                utils.clear()
                utils.show_stats()
                print("\n=== BUYING GEAR ===")
                print(f"1. WEAPON: {random_weapon['name']} [DMG: {random_weapon['dmg']}] -> {random_weapon['cost']} Gold")
                print(f"2. ARMOR:  {random_armor['name']} [Max HP: {random_armor['max_hp']}] -> {random_armor['cost']} Gold")
                print("3. Back")
                print("-" * 55)
                
                buy_choice = input("What do you want to buy? (1-3): ").strip()
                if buy_choice == "1":
                    if config.player["gold"] >= random_weapon["cost"]:
                        if config.player.get("weapon_dmg", 15) >= random_weapon["dmg"]:
                            print(f"\nYou already own an equal or stronger weapon!")
                        else:
                            config.player["gold"] -= random_weapon["cost"]
                            config.player["weapon_dmg"] = random_weapon["dmg"]  
                            print(f"\nYou bought {random_weapon['name']}!")
                    else:
                        print("\nYou don't have enough gold!")
                    input("\nPress ENTER to continue...")
                elif buy_choice == "2":
                    if config.player["gold"] >= random_armor["cost"]:
                        if config.player["max_hp"] >= random_armor["max_hp"]:
                            print(f"\nYou already own equal or better armor!")
                        else:
                            config.player["gold"] -= random_armor["cost"]
                            config.player["max_hp"] = random_armor["max_hp"]
                            config.player["hp"] = random_armor["max_hp"]  
                            print(f"\nYou bought {random_armor['name']}!")
                    else:
                        print("\nYou don't have enough gold!")
                    input("\nPress ENTER to continue...")
                elif buy_choice == "3":
                    break
        
        elif main_choice == "2":
            while True:
                utils.clear()
                utils.show_stats()
                print("\n=== SELLING ITEMS ===")
                print("The blacksmith buys any monster drop for 8 Gold each.")
                print("-" * 55)
                
                inventory = config.player.get("inventory", [])
                if not inventory:
                    print("[Your bag is empty. Go defeat monsters to get loot!]")
                    print("1. Back")
                    print("-" * 55)
                    input("\nPress ENTER to go back...")
                    break
                
                for index, item in enumerate(inventory):
                    print(f"{index + 1}. Sell: {item} (+8 Gold)")
                print(f"{len(inventory) + 1}. Back")
                print("-" * 55)
                
                sell_choice = input(f"Select item to sell (1-{len(inventory) + 1}): ").strip()
                try:
                    sell_index = int(sell_choice) - 1
                    if 0 <= sell_index < len(inventory):
                        sold_item = inventory.pop(sell_index)
                        config.player["gold"] += 8
                        print(f"\nYou sold {sold_item} for 8 Gold!")
                        input("\nPress ENTER to refresh inventory...")
                    elif sell_index == len(inventory):
                        break
                except ValueError:
                    print("\nInvalid choice!")
                    time.sleep(1)
                    
        elif main_choice == "3":
            break
