from enum import Enum
import random
from core.deck import Deck 
class BlackJackActions(Enum):
  HIT = "Hit"
  STAND = "Stand"
  DOUBLE = "Double"
  SPLIT = "Split"

class BlackJackPlayer:
  def __init__(self, bankroll=1000):
    self.bankroll = bankroll
    self.hand = []
    self.curr_bet = 0
    self.hand_total = 0

  def reset(self):
    self.hand = []

  def place_bet(self, bet: int):
    if (bet < 0 or bet > self.bankroll):
      raise ValueError(f"Invalid value to bet: {bet}")
    
    self.curr_bet = bet
    self.bankroll -= self.curr_bet
    return self.curr_bet

  def hit(self, deck):
    card = deck.draw()
    self.hand.append(card)
    return card

  def stand(self):
    return BlackJackActions.STAND

  def double(self, deck):
    updated_bet = self.curr_bet * 2
    if (updated_bet <= 0 or updated_bet > self.bankroll):
      raise ValueError(f"Insufficient bankroll to double current bet: {self.curr_bet}")
    self.bankroll -= self.curr_bet
    self.curr_bet = updated_bet
    return self.hit(deck)
    
  # Allows player to split cards of the same value
  # (10-value cards)
  def split():
    pass

class BlackJackDealer:
  def __init__(self):
    self.hand = []
    self.hand_total = 0

class BlackJackGame:
  """
    Represents a Black Jack Game.
  """
  def __init__(self, num_players=0):
    self.cards = Deck()
    self.num_players = num_players
    self.dealer = BlackJackDealer()

  def deal_cards(self):
    for _ in range(2):
      for player in self.players:
        player.hit(self.cards)
      self.dealer.hit(self.cards)

  def check_winner(self):
    pass
  