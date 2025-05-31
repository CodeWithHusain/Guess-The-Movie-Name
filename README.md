# 🎬 Movie Guessing Game

A simple terminal-based guessing game where the player tries to guess the name of a randomly chosen movie with some letters hidden.

---

## 🧩 How the Game Works

- A movie title is randomly selected from a predefined list.
- Some characters in the movie name are replaced with underscores (`_`) at random.
- The partially hidden movie title is displayed to the player.
- The player is prompted to guess the full movie name.
- The game checks the guess (case-insensitive).
- If correct, the player wins; otherwise, the correct answer is revealed.

---

## 🎮 How to Play

1. Run the script in Python 3.
2. View the movie name with some letters hidden.
3. Type your guess and press Enter.
4. See if your guess matches the actual movie name.

---

## ⚙️ Code Summary

- Uses the `random` module to pick movies and hide characters randomly.
- Converts the movie name into a list of characters to replace some with underscores.
- Compares the player's guess in a case-insensitive manner.
- Provides feedback on success or failure.

---

## 🚀 Running the Game

Save the script as `movie_guessing_game.py` and run:

```bash
python movie_guessing_game.py
['_', 'r', '_', '_', '_', 'y', 'a', 'm']
guess the movie name: drishyam
take your trophy
