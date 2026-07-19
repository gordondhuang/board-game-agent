from games.card_games.blackjack import (
  BlackJackActions,
  calculate_hand_total,
  card_value,
)


class BlackJackAgent:
  """
    Represents an AI agent that can play BlackJack.
  """

  def __init__(self, bankroll=0, base_bet=0):
    self.bankroll = bankroll
    self.base_bet = base_bet

  def place_bet(self):
    if self.bankroll <= 0 or self.base_bet <= 0:
      return 0
    return min(self.base_bet, self.bankroll)

  def action(self, hand, dealer_card, can_double):
    total = calculate_hand_total(hand)
    dealer_value = card_value(dealer_card)
    soft = self._is_soft(hand)

    if can_double and self._should_double(total, dealer_value, soft):
      return BlackJackActions.DOUBLE
    if self._should_hit(total, dealer_value, soft):
      return BlackJackActions.HIT
    return BlackJackActions.STAND

  def _should_double(self, total, dealer_value, soft):
    if soft:
      return total in {17, 18} and 3 <= dealer_value <= 6
    return (
      total == 11
      or total == 10 and dealer_value <= 9
      or total == 9 and 3 <= dealer_value <= 6
    )

  def _should_hit(self, total, dealer_value, soft):
    if soft:
      return total <= 17 or total == 18 and dealer_value >= 9
    return (
      total <= 11
      or total == 12 and dealer_value in {2, 3}
      or total <= 16 and dealer_value >= 7
    )

  def _is_soft(self, hand):
    total_with_aces_high = sum(card_value(card) for card in hand)
    return any(card.get_rank() == "Ace" for card in hand) and total_with_aces_high <= 21
