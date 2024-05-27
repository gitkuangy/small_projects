# Blackjack Game

This is a simple Blackjack game written in Python. The game follows the standard rules of Blackjack, where the player competes against the computer (dealer).

## Features

- Unlimited deck size.
- No jokers.
- Jack, Queen, and King all count as 10.
- Ace can count as 11 or 1.
- Equal probability of drawing any card.
- The computer is the dealer.
- Option to continue playing with the same hand.

## Requirements

- Python 3.x
- `art` library for displaying ASCII art logos (optional)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/gitkuangy/small_projects.git
    cd blackjack-game
    ```

2. Install the `art` library (if not already installed):
    ```sh
    pip install art
    ```

3. Run the program:
    ```sh
    python blackjack.py
    ```

4. Follow the prompts to play the game.

## Example

```plaintext
   __        ___           _       _            _    
  / /       / _ \         | |     | |          | |   
 / /____  _| | | |___  ___| | __ _| |_ ___  ___| | __
| '_ \ \ / / | | / __|/ __| |/ _` | __/ _ \/ __| |/ /
| | | \ V /| |_| \__ \ (__| | (_| | ||  __/ (__|   < 
|_| |_|\_/  \___/|___/\___|_|\__,_|\__\___|\___|_|\_\
                                                     
                                                     
Would you like to play Blackjack? y/n: y
   Your cards: [10, 6], current score: 16
   Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [10, 6, 5], current score: 21
   Computer's first card: 7
You win with a BlackJack.
You have final cards: [10, 6, 5], final score: 21
Opponent has cards: [7, 8, 6], final score: 21
Would you like to play again? y/n: n
