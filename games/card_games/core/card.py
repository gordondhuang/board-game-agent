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
  rank_order = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
  }

  def __init__(self, suit: Suit, rank: str):
    if not isinstance(suit, Suit):
      raise ValueError(f"suit must be a Suit enum, retrieved {suit}")
    if rank not in self.ranks:
      raise ValueError(f"Invalid rank: {rank}")

    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return f"{self.rank} of {self.suit.value}"
  
  def __lt__(self, other):
    return self.rank_order[self.rank] < self.rank_order[other.rank]
  
  def __eq__(self, other):
    if not isinstance(other, Card):
      return False
    return self.rank == other.rank and self.suit == other.suit
  
  def get_rank(self):
    return self.rank
  
  def get_suit(self):
    return self.suit
