# Word Guessing Game

A simple word-guessing game where the player tries to guess a 5-letter word within a limited number of attempts. The game provides feedback on the correctness of the player's guess, indicating if the letters are in the correct position, present but in the wrong position, or not in the word at all.

## Features
- **Random Word Selection**: The game selects a random 5-letter word from a list of words.
- **6 Attempts**: The player has 6 attempts to guess the correct word.
- **Feedback**: After each guess, the game provides feedback:
  - Letters that are in the correct position.
  - Letters that are in the word but in the wrong position.
  - Letters that are not in the word.
- **Art and Color**: The game uses ASCII art and color formatting for win/lose messages to enhance the gameplay experience.
- **Cross-platform**: Runs on any system with Python installed.

## Requirements

- Python 3.12.2
- The following Python libraries are required:
  - `colorama` for colored output
  - `art` for ASCII art

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/word-guessing-game.git
   cd word-guessing-game
   pip install -r requirements.txt
   python game.py
