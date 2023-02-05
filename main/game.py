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

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f"{column}{num}":
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append("   ")
        return row

    def create_grid(self):
        # | A | B | C | D |
        header = " |  " + "  |  ".join(self.columns) + "  |"
        print(header)
        for row in range(1, self.size + 1):
            print_row = f"{row}| "
            get_row = self.create_row(row)
            print_row += " | ".join(get_row) + " |"
            print(print_row)

    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f"{card.location}:{card}")
            return False

    def check_win(self):
        for card in self.cards:
            if card.matched == False:
                return False
        return True

    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card?")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("That's not a valid location. It should look like this: A1")

    def start_game(self):
        game_running = True
        print("Memory game")
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location("first")
            guess2 = self.check_location("second")
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print("You win!!")
                    self.create_grid()
                    game_running = False
            else:
                input("Those cards are not a match. Press Enter to contine")
        print("GAME OVER")


if __name__ == "__main__":
    game = Game()
    game.start_game()

    # print(game.create_row(1))
    # print(game.create_row(2))
    # print(game.create_row(3))
    # print(game.create_row(4))
