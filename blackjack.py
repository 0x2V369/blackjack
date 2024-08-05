import random
from os import system, name

# Available cards for the game, represents a single deck of cards
CARDS = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
         10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def deal_card():
    """
    Draws a random card from the deck and removes it from CARDS.

    :return: A card from the deck.
    """
    card = random.choice(CARDS)
    CARDS.remove(card)
    return card


def find_winner(user_score, computer_score):
    """
    Determins the winner of the game based on user and computer scores.

    :param user_score: Calculated score from user cards.
    :param computer_score: Calculated score from computer cards.
    :return: A statement indicating whether the user won, lost or drew.
    """
    if user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 21:
        return "You have a Blackjack! You won!"
    elif computer_score == 21:
        return "Computer has Blackjack! You lose."
    elif user_score > computer_score:
        return "Congratulations, you win!"
    else:
        return "You lose."


def calculate_score(cards):
    """
    Calculates the score of a hand of cards. Adjusts for the Ace value to avoid busting.

    :param cards: List of cards in hand.
    :return: The score of the hand.
    """
    score = sum(cards)
    ace_count = cards.count(11)

    # Adjust the score for Ace if score > 21
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    return score


def clear_screen():
    """
    Clears the console screen.
    Works on both Windows and Unix-like systems.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_cards(user_cards, user_score, computer_cards, reveal_computer=False):
    """
    Displays the cards and scores for the user and the computer.

    :param user_cards: List of user cards.
    :param user_score: Current score for the user based on user cards.
    :param computer_cards: List of computer cards.
    :param reveal_computer: Bool to determine if all computer cards should be shown or just the first one.
    """
    print(f"Your cards: {user_cards}, current score: {user_score}")
    if reveal_computer:
        print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}")
    else:
        print(f"Computer's first card: {computer_cards[0]}")


def blackjack_game():
    """
    The main function for the blackjack game containing the gameplay logic.

    :return: The result of the game (win, lose, draw).
    """
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 21 or computer_score == 21:
        display_cards(user_cards, user_score, computer_cards, True)
        return find_winner(user_score, computer_score)

    game_over = False

    while not game_over:
        display_cards(user_cards, user_score, computer_cards)

        user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ").casefold()
        if user_should_continue == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score > 21:
                game_over = True
        else:
            game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    display_cards(user_cards, user_score, computer_cards, True)
    return find_winner(user_score, computer_score)


def main():
    """
    The main entry point for the blackjack game.
    Manages the game loop and user prompts.
    """
    clear_screen()
    print("Welcome to the Blackjack game!")
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").casefold() == 'y':
        clear_screen()
        result = blackjack_game()
        print(result)


if __name__ == "__main__":
    main()
