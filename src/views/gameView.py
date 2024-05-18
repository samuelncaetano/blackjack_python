# flake8: noqa: E501,
from src.models import Game


class GameView:
    def __init__(self, game: Game):
        self.game = game

    def display_game(self):
        print(
            "\nPlayer Hand:",
            [f"{card.face} of {card.suit}" for card in self.game.get_player_hand()],
        )
        print("Player Score:", self.game.get_player_score())
        print(
            "Dealer Hand:",
            [f"{card.face} of {card.suit}" for card in self.game.get_dealer_hand()],
        )
        print("Dealer Score:", self.game.get_dealer_score())

    def display_player_options(self):
        if self.game.get_game_state() == "playerTurn":
            print("Options: [h] Hit, [s] Stand, [q] Quit")

    def display_game_over(self):
        if self.game.get_game_state() == "gameOver":
            print("\nGame Over.")
            if self.game.get_player_score() > 21:
                print("Player busts! Dealer wins.")
            elif self.game.get_dealer_score() > 21:
                print("Dealer busts! Player wins.")
            elif self.game.get_player_score() > self.game.get_dealer_score():
                print("Player wins!")
            elif self.game.get_player_score() < self.game.get_dealer_score():
                print("Dealer wins!")
            else:
                print("It's a tie!")
