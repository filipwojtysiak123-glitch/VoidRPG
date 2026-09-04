import time
import config
import utils
import leveling

def fight_system(enemy_name, enemy_hp, enemy_dmg, enemy_exp, enemy_loot=None):
    """System walki turowej (blokada magii przy 0 shardach)."""
    utils.slow_print(f"\n[COMBAT] You are attacked by {enemy_name}! (HP: {enemy_hp})")
    input("\nPress ENTER to draw your weapon...")
    
    weapon_dmg = config.player.get("weapon_dmg", 15)
    
    while enemy_hp > 0 and config.player["hp"] > 0:
        utils.clear()
        utils.show_stats()
        print(f"\nEnemy: {enemy_name} (HP: {enemy_hp})")
        print("-" * 30)
        print("Choose your skill:")
        print(f"1. Sword Strike ({weapon_dmg} DMG, Cost: 0 MP)")
        
        has_magic = config.player["soul_shards"] > 0
        if has_magic:
            print("2. Fireball     (35 DMG, Cost: 10 MP)")
            print("3. Holy Heal    (40 HP,  Cost: 15 MP)")
        else:
            print("[X] 2. Fireball     (LOCKED - Your soul lacks magic)")
            print("[X] 3. Holy Heal    (LOCKED - Your soul lacks magic)")
            
        choice = input("\nWhat will you do? > ")
        utils.clear()
        utils.show_stats()
        
        if choice == "1":
            enemy_hp -= weapon_dmg
            utils.slow_print(f"You slash the enemy with your sword for {weapon_dmg} DMG!")
        elif choice == "2" and has_magic:
            if config.player["mp"] >= 10:
                config.player["mp"] -= 10
                enemy_hp -= 35
                utils.slow_print("BOOM! A massive fireball burns the enemy for 35 DMG!")
            else:
                utils.slow_print("Not enough Mana (MP)! You waste your turn.")
        elif choice == "3" and has_magic:
            if config.player["mp"] >= 15:
                config.player["mp"] -= 15
                config.player["hp"] = min(config.player["hp"] + 40, config.player["max_hp"])
                utils.slow_print("A golden light heals you for 40 HP!")
            else:
                utils.slow_print("Not enough Mana (MP)! You waste your turn.")
        else:
            utils.slow_print("You can't use that skill yet or you hesitated! You lose your turn!")
            
        time.sleep(1)
        if enemy_hp <= 0: break
            
        utils.simulate_thinking(0.6, f"Enemy turn ({enemy_name})")
        config.player["hp"] -= enemy_dmg
        utils.slow_print(f"Ouch! The enemy hits you for {enemy_dmg} DMG!")
        input("\nPress ENTER to continue...")
        
    utils.clear()
    if config.player["hp"] > 0:
        utils.slow_print(f"Victory! {enemy_name} has been defeated!")
        leveling.gain_exp(enemy_exp)
        
        if enemy_loot:
            config.player["inventory"].append(enemy_loot)
            utils.slow_print(f"[LOOT] You found an item: {enemy_loot}! (Added to your Bag)")
            input("\nPress ENTER to continue...")
        return True
    
    utils.slow_print("You died in battle... Game Over.")
    input("\nPress ENTER to return to the main menu...")
    return False
