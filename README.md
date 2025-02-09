
# Blackjack Game in Python

Welcome to the Blackjack game! This project contains two implementations of a text-based Blackjack game written in Python:

- **Version 1 (Original):**  
  A basic implementation using a simplified deck (with card values represented as numbers) and straightforward logic.

- **Version 2 (Improved & Recommended):**  
  An enhanced version featuring:
  - A realistic deck generated using card ranks and suits.
  - Robust card handling through dedicated functions (e.g., `get_rank()`) to accurately extract card values (especially for multi-character ranks like "10").
  - A more modular design with improved game flow.
  - Realistic dealer behavior, including revealing only the dealer's first card (with its score) during gameplay.

> **Note:** Version 2 is recommended for its improved accuracy, realistic gameplay, and code clarity.

---

## Game Rules

- The game is played with a single deck of cards.
- Cards 2 through 10 are worth their face value.
- The Jack, Queen, and King are each worth 10 points.
- The Ace can count as 11 or 1, depending on which value keeps the player's hand at or below 21.
- The objective is to beat the dealer's hand by having a hand value closer to 21 without exceeding it.

---

## Features

- **Realistic Deck & Card Handling:**  
  - Version 2 uses a deck of strings (e.g., `"10 of Hearts"`, `"A of Spades"`) generated with `itertools.product` and shuffles it for random dealing.
  - A helper function `get_rank()` ensures accurate extraction of card ranks from strings.

- **Modular Design:**  
  - Clear separation of functionality into functions such as dealing cards, calculating scores (with proper Ace adjustments), and determining the winner.
  
- **User-Friendly Interface:**  
  - Displays your cards and score.
  - Reveals only the dealer’s first (visible) card and its score during your turn.
  - Allows you to choose whether to "hit" (draw another card) or "stand" (end your turn).

- **Dealer Logic:**  
  - The dealer automatically draws cards until reaching a minimum score of 17.

---

## Getting Started

### Prerequisites

- Python 3.x (Tested on Python 3.8+)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/0x2V369/blackjack.git
   cd blackjack
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

---

## How to Run the Game

### For the Improved Version (Recommended)

Run the game using:

```bash
python blackjack_v2.py
```

### For the Original Version

If you wish to run the original version:

```bash
python blackjack.py
```

---

## How to Play

1. **Starting the Game:**  
   - When prompted, type 'y' to start a new game or 'n' to exit.
2. **Initial Deal:**  
   - You and the dealer are each dealt two cards.
   - Your cards and total score are displayed.
   - Only the dealer’s first card (and its score) is shown until your turn ends.
3. **Your Turn:**  
   - Choose to "hit" to receive another card or "stand" to end your turn.
   - If your score exceeds 21, you bust and lose.
4. **Dealer’s Turn:**  
   - The dealer reveals the full hand and draws cards until reaching a score of at least 17.
5. **Outcome:**  
   - Final hands and scores are compared to determine the winner.

---

## Code Structure

- **Version 1 (Original):**  
  - `blackjack.py` contains the initial implementation using a deck represented by a list of numbers.
  - Basic card dealing and score calculation functions are implemented, with simple logic for Ace adjustment and winner determination.

- **Version 2 (Improved):**  
  - `blackjack_v2.py` features a realistic deck created using card ranks and suits.
  - Utilizes a helper function `get_rank(card)` to correctly extract card values.
  - Improved game flow and dealer logic with a clear display of only the dealer’s visible card during play.
  - Modular functions for dealing cards, calculating scores, checking for blackjack, and formatting card output.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [0x2V369](https://github.com/0x2V369).

---

## Acknowledgments

- Inspired by the classic casino game Blackjack.
- Thanks to the Python community for continuous support and inspiration.
