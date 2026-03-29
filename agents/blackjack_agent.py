class BlackJackAgent:
  """
    Represents an AI agent that can play BlackJack.
  """

  def __init__(self, bankroll=0, base_bet=0):
    self.bankroll = bankroll
    self.base_bet = base_bet

  def place_bet(self):
    return min(self.base_bet, self.bankroll)

  def action(self, hand, dealer_card, can_double):
    pass