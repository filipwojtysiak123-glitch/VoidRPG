=========================================================================
                             VOID RPG: RA
=========================================================================

A dark, text-based RPG adventure created in Python. Set in a world where 
you play as a forgotten hero who must reclaim the shattered fragments of 
their soul to defeat the final god of destruction — RA.

-------------------------------------------------------------------------
1. STORYLINE
-------------------------------------------------------------------------
The world has completely forgotten your name. Once a legendary champion, 
you are now a mere shadow of the past. The monsters you defeated centuries 
ago are returning, and each one holds a piece of your shattered soul 
captive. Your magic is completely sealed until you reclaim at least one 
fragment of yourself. Embark on this journey, reclaim your ancient power, 
and destroy the god RA once and for all!

-------------------------------------------------------------------------
2. KEY FEATURES
-------------------------------------------------------------------------
* Modular Architecture: The game is fully split into clean, independent 
  .py modules (combat, story, shop, leveling, config, utils).
* Save Game System (3 Slots): An advanced save system built to resist 
  console path resolution bugs.
* Turn-Based Combat: Manage your Mana Points (MP), cast healing spells, 
  and launch offensive magic (unlocked as your soul gets restored).
* Mathematical EXP System: The experience points threshold required to 
  level up scales proportionally with your level (Level * 50).
* Randomized Shop & Trading: The blacksmith randomizes his stock upon 
  every visit. Buy gear to increase your stats or sell monster loot.
* Lore Journal: A deep, cinematic story uncovered step-by-step with a 
  text-paging feature mapped to the ENTER key.

-------------------------------------------------------------------------
3. PROJECT STRUCTURE
-------------------------------------------------------------------------
The project consists of the following files:
- VoidRPG.py  - The primary boot file; controls the main menu and game.
- config.py   - Holds the global data dictionary for player stats.
- utils.py    - System utilities: clears the screen and handles saving.
- combat.py   - The turn-based combat engine.
- shop.py     - Logic for the randomized shop and item trading.
- story.py    - Controls the cinematic Intro sequence and Lore Journal.
- leveling.py - Functions responsible for calculating EXP and Level Ups.

-------------------------------------------------------------------------
4. HOW TO RUN THE GAME
-------------------------------------------------------------------------
Requirements:
You must have Python (version 3.x or higher) installed on your computer.

The Easiest Way to Run (Desktop Method):
1. Create a folder named "Game" directly on your Desktop.
2. Put all the game files inside that "Game" folder (make sure the main 
   file is named "VoidRPG.py").
3. Open your computer's Start Menu, type "cmd", and press ENTER to open 
   the console.
4. Copy and paste the following commands into the black console window 
   (press ENTER after each line):

   cd Desktop\Game
   python VoidRPG.py

   (If your system displays an error on the second line, try typing 
   "py VoidRPG.py" instead).

-------------------------------------------------------------------------
5. FUTURE ROADMAP
-------------------------------------------------------------------------
[ ] Add random side encounters during exploration (grinding gold and EXP).
[ ] Implement dodge chances and critical strikes (Crit/Dodge).
[ ] Add a consumable Potions system to restore health/mana during combat.

-------------------------------------------------------------------------
6. COMMUNITY & SUPPORT
-------------------------------------------------------------------------
This game is actively being developed! Stay tuned for updates.
If you want to report a bug, suggest a feature, or track progress, 
join the official Discord server link listed inside the game's credits.
=========================================================================
