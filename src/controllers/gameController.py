import sys
from src.models import Game
from src.views import GameView

# from models.game import Game
# from views.gameView import GameView


class GameController:
    def __init__(self):
        self.game = Game()
        self.view = GameView(self.game)

    def start_game(self):
        self.game.start_new_game()
        self.view.display_game()
        self.process_player_turn()

    def process_player_turn(self):
        if self.game.get_game_state() == "gameOver":
            self.view.display_game_over()
            self.offer_restart_option()
        else:
            self.view.display_player_options()
            answer = input("Choose an option: ").lower()
            if answer == "h":
                self.game.player_hit()
                self.view.display_game()
                self.process_player_turn()
            elif answer == "s":
                self.game.dealer_play()
                self.view.display_game()
                self.process_player_turn()
            elif answer == "q":
                print("Thank you for playing!")
                sys.exit()
            else:
                print("Invalid option.")
                self.process_player_turn()

    def offer_restart_option(self):
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer == "y":
            self.game.restart_game()
            self.view.display_game()
            self.process_player_turn()
        elif answer == "n":
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Invalid option.")
            self.offer_restart_option()


if __name__ == "__main__":
    GameController().start_game()
