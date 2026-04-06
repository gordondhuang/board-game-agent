import random
from card import Card, Suit
class Deck:
  """
    Represents a standard deck of 52 cards.
  """
  def __init__(self):
    self.cards = []
    self.generate_deck()

  def generate_deck(self):
    for suit in Suit:
      for rank in Card.ranks:
        self.cards.append(Card(suit, rank))

    self.shuffle()

  def shuffle(self):
    random.shuffle(self.cards)

  def draw(self):
    if len(self.cards) == 0:
      raise ValueError("There are no more cards in the deck.")
    return self.cards.pop()

  def __len__(self):
    return len(self.cards)
  
  def __str__(self):
    return f"Deck of {len(self.cards)} cards"