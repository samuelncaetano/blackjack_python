class Card:
    def __init__(self, face: str, suit: str):
        self.face = face
        self.suit = suit

    def get_value(self) -> int:
        if self.face == "A":
            return 11
        if self.face in ["J", "Q", "K"]:
            return 10
        return int(self.face)
