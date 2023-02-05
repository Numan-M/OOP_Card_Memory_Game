# Card Memory Game

This is a command-line based memory game that requires players to find matches between cards. The game consists of a 4x4 grid of cards, and each card has a word written on it. The game is won when all the cards have been matched.

## Classes

### Card

The Card class represents a single card in the game. It has two attributes: word and location. The word attribute is the word written on the card, and the location attribute is the location of the card on the 4x4 grid. The class also has a matched attribute which is set to False by default. If a player successfully matches two cards, the matched attribute of both cards is set to True.

### Game

The Game class represents the game itself. It has several attributes:

* size: the size of the grid (4x4 in this case)
* card_options: a list of words that can appear on the cards
* columns: a list of column labels for the grid
* cards: a list of Card instances
* locations: a list of locations on the 4x4 grid

The Game class has several methods:

* set_cards: sets the cards attribute by randomly selecting words from card_options and assigning them to random locations on the grid.
* create_row: takes an integer num representing the row number and returns a list of words representing that row. If a card has not been matched, it will show an empty string.
* create_grid: displays the 4x4 grid with the current state of the cards.
* check_match: takes two location strings (e.g. "A1") and checks if the cards at those locations are a match. If they are, the matched attribute of both cards is set to True. If they are not a match, the method returns False.
* check_win: checks if all the cards have been matched, and returns True if they have.
* check_location: takes a string time ("first" or "second") representing the player's guess, and prompts the player for a location. The method checks if the input is a valid location and returns it if it is.
* start_game: starts the game by calling other methods in the class to initialize the grid, prompt players for guesses, and check if the game is won.

## How to Play

To start the game, run the following code:

```
if __name__ == "__main__":
    game = Game()
    game.start_game()
```

The game will prompt you to enter the location of two cards. If the cards match, they will be revealed and you will be prompted to guess again. If the cards do not match, they will be hidden again and you will be prompted to guess again. The game continues until all the cards have been matched.

## Installation
To use the memory card game, you'll need to clone the repository to your local machine:


```
$ git clone https://github.com/Numan-M/card-memory-game.git
```
Then, navigate to the directory:


```
$ cd card-memory-game
```
You will need to have Python installed on your machine. You can check if you have it installed by running:


```
$ python --version
```

If you don't have Python installed, you can download it from the official Python website.
Once you have Python installed, you can run the memory game with the following command:

```
$ python main.py
```
You can start playing the game in the terminal!

# Contact
Feel free to contact me on:

[LinkedIn](https://www.linkedin.com/in/numan-mahmood-197951242/)
