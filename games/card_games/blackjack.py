import random

class Player:
  def __init__(self, bankroll=1000, bet=0):
    self.bankroll = bankroll
    self.bet = bet
    self.hands = []

  def reset(self):
    self.hands = []

  def place_bet(self):
    return max(0, self.bet)

  def hit():
    pass

  def stand():
    pass

  def double():
    pass

  # Allows player to split cards of the same value
  # (10-value cards)
  def split():
    pass

class Dealer:
  pass

class BlackJackGame:
  def __init__(self):
    self.cards = []

  def shuffle_deck(self):
    pass