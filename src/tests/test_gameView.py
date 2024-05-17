from src.models import Game
from src.views import GameView


def test_display_game(capsys):
    game = Game()
    game_view = GameView(game)
    game_view.display_game()
    captured = capsys.readouterr()
    output = captured.out
    assert "Player Hand:" in output
    assert "Player Score:" in output
    assert "Dealer Hand:" in output
    assert "Dealer Score:" in output


def test_display_player_options(capsys):
    game = Game()
    game_view = GameView(game)
    game.game_state = "playerTurn"
    game_view.display_player_options()
    captured = capsys.readouterr()
    output = captured.out
    assert "Options: [h] Hit, [s] Stand, [q] Quit" in output


def test_player_wins(capsys):
    game = Game()
    game_view = GameView(game)
    game.game_state = "gameOver"
    game.player_score = 20
    game.dealer_score = 18
    game_view.display_game_over()
    captured = capsys.readouterr()
    output = captured.out
    assert "Player wins!" in output


def test_display_game_over(capsys):
    game = Game()
    game_view = GameView(game)
    game.game_state = "gameOver"
    game.player_score = 22
    game.dealer_score = 20
    game_view.display_game_over()
    captured = capsys.readouterr()
    output = captured.out
    assert "Game Over." in output
    assert "Player busts! Dealer wins." in output
