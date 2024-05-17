from src.models import Deck

# from models.deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_state = "waiting"
        self.start_new_game()

    def start_new_game(self):
        self.deck = Deck()
        self.player_hand = [self.deck.draw(), self.deck.draw()]
        self.player_hand = [card for card in self.player_hand if card]
        self.dealer_hand = [self.deck.draw(), self.deck.draw()]
        self.dealer_hand = [card for card in self.dealer_hand if card]
        self.game_state = "playerTurn"
        self.update_scores()

    def restart_game(self):
        if self.game_state == "gameOver":
            self.start_new_game()
        else:
            print("Game is not over yet!")

    def get_player_hand(self):
        return self.player_hand

    def get_dealer_hand(self):
        return self.dealer_hand

    def get_player_score(self):
        return self.player_score

    def get_dealer_score(self):
        return self.dealer_score

    def update_scores(self):
        self.player_score = self.calculate_score(self.player_hand)
        self.dealer_score = self.calculate_score(self.dealer_hand)

    def calculate_score(self, hand):
        score = sum(card.get_value() for card in hand)
        ace_count = sum(1 for card in hand if card.face == "A")
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    def player_hit(self):
        if self.game_state != "playerTurn":
            return
        new_card = self.deck.draw()
        if new_card:
            self.player_hand.append(new_card)
            self.update_scores()
            if self.player_score > 21:
                self.game_state = "gameOver"
            elif self.player_score == 21:
                self.game_state = "dealerTurn"

    def dealer_play(self):
        while self.dealer_score < 17:
            new_card = self.deck.draw()
            if new_card:
                self.dealer_hand.append(new_card)
                self.update_scores()
            else:
                break
        self.game_state = "gameOver"

    def get_game_state(self):
        return self.game_state
