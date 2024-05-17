# flake8: noqa: F401,
# pylint: disable=E0401
import pytest

from src.models import Card

# from models.card import Card


def test_ace_value():
    card = Card("A", "hearts")
    assert card.get_value() == 11


def test_face_cards_value():
    jack = Card("J", "spades")
    queen = Card("Q", "diamonds")
    king = Card("K", "clubs")
    assert jack.get_value() == 10
    assert queen.get_value() == 10
    assert king.get_value() == 10


def test_numeric_cards_value():
    two = Card("2", "hearts")
    nine = Card("9", "clubs")
    assert two.get_value() == 2
    assert nine.get_value() == 9
