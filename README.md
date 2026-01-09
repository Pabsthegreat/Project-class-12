# Project-class-12
Class 12 Capstone Project

## About

This was our Final Capstone Project for 12th Grade in the Python Programming Course.
My 2 friends and I put to use everything we learnt in Python over the course of 2 years and also used pygame and its modules to make an online copy of a game called "Hunter Assassin", which is a single player action game.
This was a year-long project; we integrated tkinter as a UI component for logging in for the users and displaying the leaderboard, and we also used SQL to store the user data from the game.
All in all this was a fun project to work on. Even though it was hard, I felt a real sense of accomplishment.
This will always be one of my favourite projects as it is my first big project!

## Documentation

Check out the Google Docs link to see detailed documentation:

https://docs.google.com/document/d/1gG5GlDFsZc5sXrJZGDaPpaz73cwT_8psOzX2xjGbKKA/edit?usp=sharing

Cheers!

---

## Game Overview

Hunter Assassin is a top‑down, single‑player action game built in Python using:

- **pygame** for the main game loop, graphics, and input
- **tkinter** for the menu UI (start game, rules, leaderboard, exit)
- **MySQL** for persistent storage of player scores and times

### Key Features

- Smooth player and enemy movement with animated sprites
- Line‑of‑sight‑based enemy AI that shoots when the player is in range and within a vision cone
- Health system and scoring
- Automatic enemy spawning over time
- SQL‑backed leaderboard with ranking logic (insertion sort + tie‑breaking by completion time)

## Controls

### In‑game (pygame window)

- Movement: `W / A / S / D` or Arrow keys
- Attack: `Space` (when overlapping an enemy to eliminate them)

### Menu (tkinter window)

- **Start Game** – enter your name, launch the game, and record your score
- **Rules** – view instructions and mechanics
- **Leaderboard** – view the top players from the SQL database
- **End Game** – quit the application

## Project Structure (high‑level)

- `Menu.py` – tkinter main menu and leaderboard UI
- `FINAL_GAME.py` – core pygame game loop and logic
- `SQL_Scoring.py` – runs the game, computes ranking, and writes/reads MySQL leaderboard entries
- `setup_db.py` – one‑time database setup helper for new systems
- `db_config.py` / `db_config.json` – shared MySQL connection configuration
- `Hunter_Move/`, `Enemy_Move/`, `pics/` – game art assets
- `usedcode/` – experimental and alternate versions of main/game logic used during development

---

## Setup Guide (new system)

This section explains how to get the project running on a fresh macOS machine.

### 1. Requirements

- **Python** with Tk support (on this repo we use `python3.12`):
  - Confirm Tk is available:
    - `python3.12 -c "import tkinter; print('tk_ok')"`
- **MySQL Server** running on `localhost`
- Internet access the first time (to install Python packages)

### 2. Clone the repository

```bash
git clone https://github.com/Pabsthegreat/Project-class-12.git
cd Project-class-12
```

### 3. Install Python dependencies (for the Tk‑enabled Python)

Install `pygame` and `mysql-connector-python` for the interpreter you will use (here `python3.12`):

```bash
python3.12 -m pip install pygame mysql-connector-python
```

> If you prefer another Python version, replace `python3.12` consistently in the commands below, but make sure that version supports `tkinter`.

### 4. One‑time database setup

We provide `setup_db.py` to create the database, table, user, and write a shared config file.

Run:

```bash
cd /Users/adarsh/Documents/GitHub/Project-class-12  # or your clone path
python3.12 setup_db.py
```

The script will prompt you for:

1. **MySQL host** – usually just press Enter to keep `localhost`.
2. **MySQL admin username** – often `root`.
3. **Password for admin user** – the same password you use with `mysql -u root -p`.
4. **Database name to use** – default `project`; you can also type something like `hunterassassin`.
5. **MySQL username for the game** – you can reuse the admin user or specify a dedicated user (e.g. `hunter`).
6. **Password for the game user** – only needed if you choose a dedicated user with its own password.

What `setup_db.py` does:

- Creates the database if it does not exist (e.g. `hunterassassin`).
- Creates the `leaderboard` table if it does not exist:
  - Columns: `rank`, `name`, `score`, `time`.
- Optionally creates and grants privileges to a dedicated MySQL user for the game.
- Writes `db_config.json` next to the code containing something like:

```json
{
  "host": "localhost",
  "user": "hunter",
  "password": "...",
  "database": "hunterassassin"
}
```

Both `Menu.py` and `SQL_Scoring.py` read this file via `db_config.load_db_config()`, so you don’t have to hardcode credentials.

### 5. Running the game

After `setup_db.py` completes successfully:

```bash
cd /Users/adarsh/Documents/GitHub/Project-class-12  # or your clone path
python3.12 Menu.py
```

Workflow:

- The tkinter **Main Menu** appears.
- Click **Start Game**, enter your name, and play the pygame game.
- When the run ends, your score and time are saved into MySQL.
- Click **Leaderboard** in the menu to see the ranked results.

### 6. Troubleshooting

- **Tkinter import error** (`No module named '_tkinter'`):
  - Use a Python build that includes Tk (e.g. python.org macOS installer) and run `Menu.py` with that interpreter.

- **MySQL access denied**:
  - Confirm you can log in from terminal: `mysql -u root -p`.
  - Re‑run `setup_db.py` with the same credentials that work there.

- **Missing packages**:
  - Reinstall using the same Python you use to run `Menu.py`, e.g.:
    - `python3.12 -m pip install pygame mysql-connector-python`

---

If you want to contribute or adapt this project for your own class, you can tweak the assets, difficulty, or database schema and re‑run `setup_db.py` to match your environment.

On macOS, if import tkinter ever fails, you’ll need a Python build that includes Tk (e.g. install Python 3.12 from python.org, or via Homebrew plus brew install tcl-tk and configure, not via pip).