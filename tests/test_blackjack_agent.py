from agents.blackjack_agent import BlackJackAgent
from games.card_games.blackjack import BlackJackActions
from games.card_games.core.card import Card, Suit


def card(rank):
  return Card(Suit.SPADES, rank)


def test_agent_bets_base_bet_when_bankroll_allows():
  agent = BlackJackAgent(bankroll=100, base_bet=10)

  assert agent.place_bet() == 10


def test_agent_bets_remaining_bankroll_when_base_bet_is_too_high():
  agent = BlackJackAgent(bankroll=5, base_bet=10)

  assert agent.place_bet() == 5


def test_agent_hits_hard_16_against_dealer_10():
  agent = BlackJackAgent()
  hand = [card("10"), card("6")]

  assert agent.action(hand, card("King"), can_double=False) == BlackJackActions.HIT


def test_agent_stands_hard_17():
  agent = BlackJackAgent()
  hand = [card("10"), card("7")]

  assert agent.action(hand, card("King"), can_double=False) == BlackJackActions.STAND


def test_agent_doubles_11_when_allowed():
  agent = BlackJackAgent()
  hand = [card("6"), card("5")]

  assert agent.action(hand, card("9"), can_double=True) == BlackJackActions.DOUBLE


def test_agent_hits_soft_17():
  agent = BlackJackAgent()
  hand = [card("Ace"), card("6")]

  assert agent.action(hand, card("2"), can_double=False) == BlackJackActions.HIT
