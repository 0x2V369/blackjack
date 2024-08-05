
# Blackjack Game

Welcome to the Blackjack game! This is a simple text-based implementation of the classic casino card game, written in Python.

## Game Rules

- The game is played with a standard deck of cards.
- The cards 2 through 10 are worth their face value.
- The Jack, Queen, and King are each worth 10 points.
- The Ace can be worth either 11 or 1 point, depending on which value keeps the player's total score below or equal to 21.
- The objective of the game is to have a hand value closer to 21 than the dealer without exceeding 21.

## Features

- Player vs. Computer (Dealer) mode.
- Randomized card dealing.
- Correct handling of Aces.
- Clear and simple game interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/0x2v369/blackjack.git
    ```
2. Navigate to the project directory:
    ```sh
    cd blackjack
    ```

### Running the Game

Run the game using the following command:
```sh
python blackjack.py
```

## How to Play

1. When prompted, type 'y' to start a new game or 'n' to exit.
2. You will be dealt two cards initially. The dealer will also be dealt two cards, but only one of the dealer's cards will be shown.
3. You can choose to 'hit' (get another card) or 'stand' (end your turn).
4. The dealer will reveal their hand and will draw cards until their total is at least 17.
5. The winner is determined based on whose hand is closer to 21 without exceeding it.

## Code Structure

- `blackjack.py`: The main game file containing all the logic and functions to play the game.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- GitHub: [0x2v369](https://github.com/0x2v369)

## Acknowledgments

- Inspired by the classic casino game Blackjack.

Enjoy the game and good luck!
