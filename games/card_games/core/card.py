from enum import Enum
class Suit(Enum):
  HEARTS = "Hearts"
  DIAMONDS = "Diamonds"
  CLUBS = "Clubs"
  SPADES = "Spades"
class Card:
  """
    Represents a card within a standard 52 card deck.
  """

  ranks = {
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
  }

  def __init__(self, suit: Suit, rank: str):
    if not isinstance(suit, Suit):
      raise ValueError(f"suit must be a Suit enum, retrieved {suit}")
    if rank not in self.rank:
      raise ValueError(f"Invalid rank: {rank}")

    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return f"{self.rank} of {self.suit}"
  
  def __lt__(self, other):
    return self.value() < other.value()
  
  def __eq__(self, other):
    return self.value() == other.value() and self.rank == other.rank()
  
  def get_rank(self):
    return self.rank
  
  def get_suit(self):
    return self.suit
