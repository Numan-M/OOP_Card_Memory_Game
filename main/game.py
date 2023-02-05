# --PSEUDOCODE--
# grid size
# card options
# columns
# locations
# methods
# create cards
# create grid
# check for matches
# check game won
# run game
# dunder main
# create game instance
# call start game
import random

from cards import Card


class Game:
    def __init__(self):
        self.size = 4  # 4x4
        self.card_options = ["Boo", "Bar", "Foo", "Git", "Hub", "OOP", "Pro", "Gum"]
        self.columns = ["A", "B", "C", "D"]
        self.cards = []  # populated by Card class
        self.locations = (
            []
        )  # locations on 4x4 grid set by columns and size in a for loop
        for columns in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f"{columns}{num}")

    def set_cards(self):
        used_locations = (
            []
        )  # locations which are taken will be added to this list so we can check available locations
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(
                    used_locations
                )  # removes duplicates by subtracting all locations from used ones
                random_location = random.choice(
                    list(available_locations)
                )  # turns locations back into list from set and randomly selects from available locations
                used_locations.append(
                    random_location
                )  # location used is added to used_location list
                card = Card(word, random_location)  # Card instance
                self.cards.append(card)  # appending instance to instance attribute


if __name__ == "__main__":
    game = Game()
    game.set_cards()
    for card in game.cards:
        print(card)
