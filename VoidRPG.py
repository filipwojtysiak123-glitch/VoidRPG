import time
import config
import utils
import combat
import shop
import story

def gameplay():
    while True:
        utils.clear()
        utils.show_stats()
        
        # ACT 1: Cave
        if config.player["progress"] == 0:
            utils.slow_print("\nYou are standing at a crossroads inside a dark cave.")
            print("1. Explore the Whispering Ruins (Track down the reborn Crypt Horror)")
            print("2. Save game and exit to menu")
            
            choice = input("\n> ")
            if choice == "1":
                if combat.fight_system("Crypt Horror (Reborn)", enemy_hp=60, enemy_dmg=12, enemy_exp=50, enemy_loot="Goblin Ear"):
                    config.player["soul_shards"] += 1
                    config.player["progress"] = 1
                    if 2 not in config.player["discovered_lore"]:
                        config.player["discovered_lore"].append(2)
                        
                    utils.clear()
                    utils.show_stats()
                    utils.slow_print("\nYou defeated the beast! A glowing fragment rises from its ashes.")
                    utils.slow_print("[YOU RECOVERED 1st PIECE OF YOUR SOUL! MAGIC HAS AWAKENED!]")
                    utils.slow_print("[NEW LORE UNLOCKED IN YOUR JOURNAL!]")
                    input("\nPress ENTER to continue your journey...")
                else: 
                    break
            elif choice == "2":
                utils.save_game()
                break
                
        # ACT 2: Obsidian Citadel (Village)
        elif config.player["progress"] == 1:
            utils.slow_print("\nYou arrive at the Obsidian Citadel. A blacksmith and a sanctuary are here.")
            print("\n1. Challenge the Infernal Drake (Your ancient nemesis)")
            print("2. Visit the Blacksmith (Buy/Sell Weapons & EQ)")
            print("3. Rest at the Sanctuary (Cost: 10 gold - Restores HP & MP)")
            print("4. Read your Lore Journal (Check discovered history)")
            print("5. Save game and exit to menu")
            
            choice = input("\n> ")
            if choice == "1":
                if combat.fight_system("Infernal Drake (Reborn)", enemy_hp=90, enemy_dmg=15, enemy_exp=120, enemy_loot="Drake Scale"):
                    config.player["soul_shards"] += 1
                    config.player["progress"] = 2
                    if 3 not in config.player["discovered_lore"]:
                        config.player["discovered_lore"].append(3)
                        
                    utils.clear()
                    utils.show_stats()
                    utils.slow_print("\nThe dragon falls! The second fragment merges with your chest.")
                    utils.slow_print("[YOU RECOVERED 2nd PIECE OF YOUR SOUL! YOUR SOUL IS WHOLE NOW!]")
                    utils.slow_print("[NEW LORE UNLOCKED IN YOUR JOURNAL!]")
                    input("\nPress ENTER to face the final doom...")
                else:
                    break
            elif choice == "2":
                shop.open_shop()
            elif choice == "3":
                utils.clear()
                utils.show_stats()
                if config.player["gold"] >= 10:
                    config.player["gold"] -= 10
                    config.player["hp"] = config.player["max_hp"]
                    config.player["mp"] = config.player["max_mp"]
                    utils.slow_print("\nThe holy water restores your strength and magical energy.")
                else:
                    utils.slow_print("\nYou don't have enough gold to offer to the Sanctuary.")
                input("\nPress ENTER to continue...")
            elif choice == "4":
                story.open_lore_journal()  
            elif choice == "5":
                utils.save_game()
                break

        # ACT 3: FINAL SHOWDOWN WITH RA
        elif config.player["progress"] == 2:
            utils.slow_print("\nThe sky turns pitch black. The final boss, RA, awaits you at the End of Time.")
            utils.slow_print("Your soul is complete. It's time to banish him once and for all!")
            print("\n1. FACE RA IN THE FINAL CONFRONTATION!")
            print("2. Save game and exit to menu")
            
            choice = input("\n> ")
            if choice == "1":
                utils.clear()
                utils.simulate_thinking(2, "RA IS SUMMONING HIS DIVINE POWER")
                if combat.fight_system("RA - THE GOD OF DESTRUCTION", enemy_hp=150, enemy_dmg=20, enemy_exp=0, enemy_loot=None):
                    utils.clear()
                    print("=" * 65)
                    utils.slow_print(f"🎉 CONGRATULATIONS {config.player['name']}! 🎉")
                    utils.slow_print("RA has been destroyed once and for all.")
                    utils.slow_print("The world will forever remember the Forgotten Champion.")
                    print("=" * 65)
                    input("\n[Press ENTER to read game credits...]")
                    
                    utils.clear()
                    print("=" * 65)
                    print("                       GAME CREDITS                      ")
                    print("=" * 65)
                    time.sleep(0.5)
                    utils.slow_print("\nThank you so much for playing my game!")
                    utils.slow_print("This text-based RPG adventure was fully created by Ne3x.")
                    time.sleep(0.5)
                    utils.slow_print("\nStay tuned and wait for future content updates!")
                    utils.slow_print("New locations, bosses, items, and mechanics are coming soon.")
                    time.sleep(0.5)
                    
                    print("\n" + "-" * 65)
                    utils.slow_print("Join my official Discord server for updates and feedback:")
                    # --- Dc Link ---
                    print("👉 https://discord.gg/mSegYXGsYe 👈")
                    print("-" * 65)
                    
                    input("\nPress ENTER to finish the game and return to Main Menu...")
                    
                    config.player["progress"] = 0
                    config.player["soul_shards"] = 0
                    config.player["discovered_lore"] = []
                    config.player["inventory"] = []
                    break
                else:
                    break
            elif choice == "2":
                utils.save_game()
                break

while True:
    utils.clear()
    print("=========================")
    print("      VOID RPG: RA")
    print("=========================")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")
    print("=========================")
    
    main_choice = input("> ")
    if main_choice == "1":
        utils.clear()
        print("=== CHARACTER CREATION ===")
        name = input("Enter your hero's name: ").strip()
        
        config.player["name"] = name if name else "Hero"
        config.player["hp"] = 100
        config.player["max_hp"] = 100
        config.player["mp"] = 30
        config.player["max_mp"] = 30
        config.player["gold"] = 15  
        config.player["level"] = 1
        config.player["exp"] = 0  
        config.player["progress"] = 0
        config.player["soul_shards"] = 0
        config.player["weapon_dmg"] = 15  
        config.player["discovered_lore"] = []  
        config.player["inventory"] = []  
        
        story.play_intro(config.player["name"])  
        gameplay()
    elif main_choice == "2":
        if utils.load_game():
            gameplay()
    elif main_choice == "3":
        utils.clear()
        print("Thanks for playing!")
        break
