Цифровой Кузнечик (Digital Grasshopper)
Digital Grasshopper Game 
A challenging slide puzzle game built with Python using PyQt5 for the GUI and Pygame for sound effects. Rearrange numbered tiles (1-4) on a 4x4 grid by sliding them into the empty space, with unique mechanics based on tile numbers determining move distances. Test your strategic skills across multiple levels!
🎮 Game Overview

Objective: Move each tile once, with the step length equal to the number on the tile, to solve the puzzle or complete the level.
Controls:
Click a tile to see available moves (marked with a cross if moves are possible).
Use arrow keys (↑ ↓ ← →) or mouse clicks for navigation.
Restart: Resets the current level.
Randomize: Starts a new game with a random level (1-10).

Win Condition: Successfully arrange tiles according to level-specific logic (e.g., completing a pattern or sequence).
Levels: Adjustable from 1 to 10, with increasing difficulty.

🛠️ Tech Stack

Language: Python 3.x
Libraries:LibraryPurposePyQt5GUI framework (windows, buttons, table view)QtSvgScalable vector graphics for tilespygameSound effects (e.g., restart, intro)Standard libsos, random, sys for file handling and randomization

🚀 Quick Start

Clone the Repo:textgit clone https://github.com/jawharval/Python-Mini-Puzzle-Game.git
cd Python-Mini-Puzzle-Game
Install Dependencies:textpip install PyQt5 pygame
Run the Game:textpython main.py
Play! Start by selecting a level or randomizing, then slide tiles to solve.


🎯 Features

Dynamic Grid: 4x4 grid with tiles (1-4) and an empty space.
Level System: Adjustable levels (1-10) via a spin box.
Randomization: Random level selection with prevention of repetition.
Sound Effects: Background music, button clicks, and exit sounds (toggleable via checkbox).
Visuals: SVG-based tiles with states (active, locked, step indicators).
Interactive UI: Restart and randomize buttons, menu with play/rules/exit options.
Rules Dialog: Displays game instructions in Russian.

🔍 Rules (from the Game)

Objective: Make one move with each tile, with the step length equal to the number on the tile.
Controls: Click a tile to see available moves (marked with a cross if possible). Restart or randomize levels as needed.
Strategy: Plan moves carefully, as only one move per tile is allowed. If stuck, use the "Restart" button.
Details: Presented as a logical puzzle where space is limited, requiring foresight.
