# flake8: noqa: F401,
# pylint: disable=E0401
import pytest
from src.models import Card
from src.models import Deck


@pytest.fixture
def deck():
    return Deck()


def test_deck_initialization(deck):
    assert len(deck.cards) == 52


def test_unique_cards(deck):
    unique_cards = set(f"{card.face} of {card.suit}" for card in deck.cards)
    assert len(unique_cards) == 52


def test_shuffle_changes_order(deck):
    initial_order = list(deck.cards)
    deck.shuffle()
    new_order = list(deck.cards)
    assert initial_order != new_order


def test_draw_reduces_card_count(deck):
    initial_count = len(deck.cards)
    deck.draw()
    assert len(deck.cards) == initial_count - 1


def test_draw_returns_card(deck):
    card = deck.draw()
    assert isinstance(card, Card)


def test_draw_returns_none_when_deck_is_empty(deck):
    while deck.draw() is not None:
        pass  # Esvaziar o baralho
    assert deck.draw() is None
