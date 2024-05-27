# *************** Blackjack House Rules ******************

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo  # Importing a custom logo from the art module (assumed to be available)


def choose_random_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    a_card = random.choice(cards)
    return a_card


def calculate_score(cards):
    """Calculates the score of card values."""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1 if total score exceeds 21
    return sum(cards)


def compare_cards(user_score, computer_score):
    """Compares the scores and returns the result of the game."""
    if user_score == computer_score:
        return "Draw"
    elif user_score == 21:
        return "You win with a BlackJack.\n"
    elif computer_score == 21:
        return "You lose! Opponent wins with a BlackJack.\n"
    elif user_score > 21:
        return "You went over. You lose.\n"
    elif user_score < computer_score:
        return "You lose.\n"
    else:
        return "You win.\n"


def play_game():
    """Main function to play a game of Blackjack."""
    user_cards = []
    computer_cards = []
    end_game = False

    # Deal two cards to the user and the computer
    for _ in range(2):
        user_cards.append(choose_random_card())
        computer_cards.append(choose_random_card())

    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            end_game = True
        else:
            user_add_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_add_card == 'y':
                user_cards.append(choose_random_card())
            else:
                end_game = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(choose_random_card())
        computer_score = calculate_score(computer_cards)

    print(compare_cards(user_score, computer_score))
    print(f"""
            You have final cards: {user_cards}, final score: {user_score}
            Opponent has cards: {computer_cards}, final score: {computer_score}
            """)


# Main game loop
user_choice = input("Would you like to play Blackjack? y/n: ")
while user_choice == 'y':
    print(logo)
    play_game()
    user_choice = input("Would you like to play again? y/n: ")
