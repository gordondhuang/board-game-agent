class Card:
  """
    Represents a card within a standard 52 card deck.
  """

  suits = {"Hearts", "Diamonds", "Clubs", "Spades"}
  ranks = {
      "2", "3", "4", "5", "6", "7", "8", "9", "10",
      "Jack", "Queen", "King", "Ace"
  }

  def __init__(self, suit: str, rank: str):
    if rank not in self.suits:
      raise ValueError(f"Invalid rank: {rank}")
    if suit not in self.ranks:
      raise ValueError(f"Invalid suit: {suit}")

    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return f"{self.rank} of {self.suit}"
  
  def __lt__(self, other):
    return self.value() < other.value()
  
  def __eq__(self, other):
    return self.value() == other.value()