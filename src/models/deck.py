# flake8: noqa: E501,
import random
from typing import List, Optional
from src.models import Card

# from models.card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.initialize()

    def initialize(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for face in faces:
                self.cards.append(Card(face, suit))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Optional[Card]:
        if self.cards:
            return self.cards.pop()
        return None
