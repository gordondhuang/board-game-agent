# Smart Board Game Assistant
An AI agent that powers hardware to help set up and learn card and board games. It can explain rules, shuffle cards, and project a visual guide onto the table

## 🚀 Features

- Game Rule Explanation:
  Explains how to play any card or board game in a simplified, beginner-friendly way
- Card Shuffling:
  Shuffles and deals cards to the correct number of players
- Setup Projection:
  Project a schematic visual guide of the game board onto the table to guide setup and gameplay

## 🛠️ Hardware Components


## 💡 How It Works
1. User begins by specifying a game
2. User selects the number of players
3. The system explains the rules, shuffles cards
4. A projector displays a setup guide onto the table
5. If the game is a turn-based game, the system may offer hints and answer any questions

## 🧪 Running Tests

This project uses `pytest` for tests. Run tests from the project root:

Install project dependencies first:

```bash
python -m pip install -r requirements.txt
```

```bash
python -m pytest
```

To run only the blackjack tests:

```bash
python -m pytest tests/test_blackjack.py
```

Avoid running pytest-style test files directly, such as:

```bash
python ./tests/test_blackjack.py
```

Running the file directly can cause imports like `from games.card_games.blackjack import ...` to fail because Python starts from the `tests/` directory instead of the project root. `pytest` discovers and runs `test_...` functions correctly.

## 🃏 Playing Blackjack Manually

To try blackjack as a player from the terminal, run:

```bash
python -m runners.play_blackjack
```

The script lets you place a bet, see your hand and the dealer's visible card, then choose `hit` or `stand`.

## 📌 Inspiration
As someone who plays board games often, I thought it would be helpful and exciting to have an agent make card and board games easier to learn, more efficient to set up, and accessible for everyone.
