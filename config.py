import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

player = {
    "name": "", 
    "hp": 100, 
    "max_hp": 100, 
    "mp": 30, 
    "max_mp": 30, 
    "gold": 15, 
    "level": 1, 
    "exp": 0,           
    "progress": 0,      
    "soul_shards": 0,    
    "weapon_dmg": 15,
    "discovered_lore": [],
    "inventory": []  # Torba na przedmioty gracza do sprzedaży
}

def get_save_path(slot_number):
    return os.path.join(BASE_DIR, f"savegame_{slot_number}.txt")
