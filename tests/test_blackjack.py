from games.card_games.blackjack import calculate_hand_total
from games.card_games.core.card import Card, Suit


def test_ace_counts_as_11_when_safe():
  hand = [
    Card(Suit.SPADES, "Ace"),
    Card(Suit.HEARTS, "9"),
  ]

  assert calculate_hand_total(hand) == 20


def test_ace_counts_as_1_to_avoid_bust():
  hand = [
    Card(Suit.SPADES, "Ace"),
    Card(Suit.HEARTS, "9"),
    Card(Suit.CLUBS, "5"),
  ]

  assert calculate_hand_total(hand) == 15


def test_multiple_aces_adjust_correctly():
  hand = [
    Card(Suit.SPADES, "Ace"),
    Card(Suit.HEARTS, "Ace"),
    Card(Suit.CLUBS, "9"),
  ]

  assert calculate_hand_total(hand) == 21