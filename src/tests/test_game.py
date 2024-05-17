# flake8: noqa: F401,
# pylint: disable=E0401
import pytest

from src.models import Card
from src.models import Game

# from models.card import Card
# from models.game import Game


@pytest.fixture
def game():
    return Game()


def test_start_new_game(game):
    game.start_new_game()
    assert game.get_game_state() == "playerTurn"
    assert len(game.get_player_hand()) == 2
    assert len(game.get_dealer_hand()) == 2


def test_calculate_scores(game):
    cards = [Card("A", "spades"), Card("J", "hearts")]
    game.player_hand = cards
    game.dealer_hand = cards
    game.update_scores()
    assert game.get_player_score() == 21
    assert game.get_dealer_score() == 21


def test_player_hit(game):
    game.game_state = "playerTurn"
    game.player_hit()
    assert len(game.get_player_hand()) == 3


def test_game_over_if_player_exceeds_21(game):
    game.game_state = "playerTurn"
    game.player_hand = [
        Card("10", "hearts"),
        Card("10", "diamonds"),
        Card("2", "clubs"),
    ]
    game.update_scores()
    game.player_hit()
    assert game.get_game_state() == "gameOver"


def test_dealer_play_after_player_reaches_21(game):
    game.game_state = "dealerTurn"
    game.player_score = 21
    game.dealer_play()
    assert game.get_game_state() == "gameOver"
