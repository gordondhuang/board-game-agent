import random
from card import Card
class Deck:
  """
    Represents a standard deck of 52 cards.
  """
  def __init__(self):
    self.cards = []
    self.generate_deck()

  def generate_deck(self):
    suits = Card.suits
    ranks = Card.ranks

    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit, rank))

    self.shuffle()

  def shuffle(self):
    random.shuffle(self.cards)

  def __len__(self):
    return len(self.cards)
  
  def __str__(self):
    return f"Deck of {len(self.cards)} cards"