import utils
import config
import time

def play_intro(hero_name):
    """Wstęp fabularny podzielony na sekcje z wymaganym ENTER."""
    utils.clear()
    print("=" * 65)
    print("                  BEFORE THE AMNESIA...                  ")
    print("=" * 65)
    time.sleep(0.5)
    
    utils.slow_print("\nLegends speak of an immortal champion who once stood against the darkness.")
    utils.slow_print("A warrior whose blade shattered gods, and whose name was whispered with awe.")
    input("\n[Press ENTER to continue...]")
    
    utils.clear()
    print("=" * 65)
    print("                  BEFORE THE AMNESIA...                  ")
    print("=" * 65)
    utils.slow_print(f"\nThat warrior... was you, {hero_name}.")
    utils.slow_print("\nBut in your final clash against RA, the God of Destruction, something went wrong.")
    input("\n[Press ENTER to continue...]")
    
    utils.clear()
    print("=" * 65)
    print("                  BEFORE THE AMNESIA...                  ")
    print("=" * 65)
    utils.slow_print("\nRA did not just defeat you. He shattered your very soul into fragments,")
    utils.slow_print("scattering them across the realms and cursing the world to forget you.")
    input("\n[Press ENTER to continue...]")
    
    utils.clear()
    print("=" * 65)
    print("                     PRESENT DAY...                      ")
    print("=" * 65)
    time.sleep(0.5)
    
    utils.slow_print("\nCenturies have passed. You wake up on the cold floor of a forgotten cave.")
    utils.slow_print("Your memories are gone. Your magical powers are sealed.")
    utils.slow_print("The world knows you only as a nameless stranger.")
    input("\n[Press ENTER to continue...]")
    
    utils.clear()
    print("=" * 65)
    print("                     PRESENT DAY...                      ")
    print("=" * 65)
    utils.slow_print("\nBut as your ancient enemies begin to reawaken, a spark ignites in your chest.")
    utils.slow_print("Your shattered soul is calling out to you.")
    utils.slow_print("It is time to hunt your past, reclaim your power, and face RA once again.")
    
    if 1 not in config.player["discovered_lore"]:
        config.player["discovered_lore"].append(1)
        
    print("\n" * 2)
    input("Press ENTER to begin your destiny...")

def open_lore_journal():
    lore_database = {
        1: {
            "title": "The Fall of the Champion",
            "lines": [
                "Historical records are blank, but a faint memory remains...",
                "RA used a forbidden spell called the 'Soul Fracture'.",
                "It separated your power from your physical body,",
                "turning your divine magic into physical shards guarded by his generals."
            ]
        },
        2: {
            "title": "The Secrets of the Crypt Horror",
            "lines": [
                "The beast in the Whispering Ruins wasn't always a monster.",
                "It was once your loyal hound, guarding your chamber.",
                "It was corrupted by RA's dark energy when it tried to protect your falling body.",
                "By defeating it, you didn't just take the shard — you granted it eternal peace."
            ]
        },
        3: {
            "title": "The True Power of RA",
            "lines": [
                "RA feeds on the collective amnesia of the world.",
                "As long as nobody remembers your triumph, his domain over Time remains absolute.",
                "Reclaiming all soul fragments forces the world to remember,",
                "stripping RA of his divine invulnerability for the final battle."
            ]
        }
    }
    
    while True:
        utils.clear()
        print("=========================================================")
        print("                   LORE JOURNAL                          ")
        print("=========================================================")
        
        discovered = config.player.get("discovered_lore", [])
        for key, data in lore_database.items():
            if key in discovered:
                print(f"{key}. [UNLOCKED] - {data['title']}")
            else:
                print(f"{key}. [LOCKED] - ???")
        print(f"{len(lore_database) + 1}. Close Journal")
        print("=========================================================")
        
        choice = input("Select a chapter to read: ").strip()
        try:
            choice_int = int(choice)
            if choice_int in discovered and choice_int in lore_database:
                current_lines = lore_database[choice_int]["lines"]
                for i, line in enumerate(current_lines):
                    utils.clear()
                    print(f"=== {lore_database[choice_int]['title']} ===")
                    print("-" * 55)
                    for j in range(i + 1):
                        print(current_lines[j])
                    print("-" * 55)
                    if i < len(current_lines) - 1:
                        input("\n[Press ENTER to read next line...]")
                    else:
                        input("\n[End of Chapter. Press ENTER to go back...]")
            elif choice_int == len(lore_database) + 1:
                break
            else:
                print("\nThis chapter is still locked!")
                time.sleep(1.0)
        except ValueError:
            print("\nInvalid choice!")
            time.sleep(1.0)
