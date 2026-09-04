import config
import utils

def get_required_exp(level):
    """Matematyczny wzór na wymagany EXP (Level * 50)."""
    return level * 50

def gain_exp(amount):
    """Dodaje EXP graczowi i sprawdza awans."""
    config.player["exp"] += amount
    utils.slow_print(f"\n[EXP] You gained {amount} XP!")
    input("\n[Press ENTER to proceed...]")
    
    while True:
        req_exp = get_required_exp(config.player["level"])
        if config.player["exp"] >= req_exp:
            config.player["exp"] -= req_exp
            config.player["level"] += 1
            
            config.player["max_hp"] += 20
            config.player["max_mp"] += 10
            config.player["hp"] = config.player["max_hp"]
            config.player["mp"] = config.player["max_mp"]
            
            utils.clear()
            print("=" * 40)
            utils.slow_print(f"🎉 LEVEL UP! You reached Level {config.player['level']}! 🎉")
            utils.slow_print(f"-> Max HP increased to {config.player['max_hp']}!")
            utils.slow_print(f"-> Max MP increased to {config.player['max_mp']}!")
            print("=" * 40)
            input("\nPress ENTER to continue...")
        else:
            break
