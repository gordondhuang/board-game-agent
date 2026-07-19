from enum import Enum

try:
  from .core.deck import Deck
except ImportError:
  from core.deck import Deck


BLACKJACK = 21
DEALER_STAND_TOTAL = 17


class BlackJackActions(Enum):
  HIT = "Hit"
  STAND = "Stand"
  DOUBLE = "Double"
  SPLIT = "Split"


class RoundResult(Enum):
  PLAYER_BLACKJACK = "Player blackjack"
  PLAYER_WIN = "Player win"
  DEALER_WIN = "Dealer win"
  PUSH = "Push"


class BlackJackHand:
  def __init__(self, cards=None, bet=0):
    self.cards = list(cards or [])
    self.bet = bet
    self.is_standing = False
    self.is_doubled = False

  def add_card(self, card):
    self.cards.append(card)
    return card

  @property
  def total(self):
    return calculate_hand_total(self.cards)

  @property
  def is_bust(self):
    return self.total > BLACKJACK

  @property
  def is_blackjack(self):
    return len(self.cards) == 2 and self.total == BLACKJACK

  @property
  def can_split(self):
    return len(self.cards) == 2 and card_value(self.cards[0]) == card_value(self.cards[1])


class BlackJackPlayer:
  def __init__(self, bankroll=1000):
    self.bankroll = bankroll
    self.reset()

  def reset(self):
    self.hands = [BlackJackHand()]
    self.active_hand_index = 0

  @property
  def hand(self):
    return self.hands[self.active_hand_index].cards

  @property
  def curr_bet(self):
    return self.hands[self.active_hand_index].bet

  def place_bet(self, bet: int, pos: int = 0):
    if bet <= 0 or bet > self.bankroll:
      raise ValueError(f"Invalid value to bet: {bet}")
    if pos < 0 or pos >= len(self.hands):
      raise IndexError(f"Invalid hand position: {pos}")

    self.hands[pos].bet += bet
    self.bankroll -= bet
    return self.hands[pos].bet

  def hit(self, deck, pos: int = None):
    hand = self._get_hand(pos)
    return hand.add_card(deck.draw())

  def stand(self, pos: int = None):
    self._get_hand(pos).is_standing = True
    return BlackJackActions.STAND

  def double(self, deck, pos: int = None):
    hand = self._get_hand(pos)
    if len(hand.cards) != 2:
      raise ValueError("Can only double on the first two cards")
    if hand.bet <= 0:
      raise ValueError("Cannot double before placing a bet")
    if hand.bet > self.bankroll:
      raise ValueError(f"Insufficient bankroll to double current bet: {hand.bet}")

    self.bankroll -= hand.bet
    hand.bet *= 2
    hand.is_doubled = True
    hand.add_card(deck.draw())
    hand.is_standing = True
    return hand.cards[-1]

  def get_hand_total(self, pos: int = None):
    return self._get_hand(pos).total

  def split(self, deck, pos: int = None):
    hand = self._get_hand(pos)
    if not hand.can_split:
      raise ValueError("Can only split two cards with the same blackjack value")
    if hand.bet > self.bankroll:
      raise ValueError(f"Insufficient bankroll to split current bet: {hand.bet}")

    self.bankroll -= hand.bet
    split_card = hand.cards.pop()
    new_hand = BlackJackHand([split_card], hand.bet)
    hand.add_card(deck.draw())
    new_hand.add_card(deck.draw())
    self.hands.append(new_hand)
    return new_hand

  def is_bust(self, pos: int = None):
    return self._get_hand(pos).is_bust

  def is_blackjack(self, pos: int = None):
    return self._get_hand(pos).is_blackjack

  def _get_hand(self, pos: int = None):
    index = self.active_hand_index if pos is None else pos
    if index < 0 or index >= len(self.hands):
      raise IndexError(f"Invalid hand position: {index}")
    return self.hands[index]


class BlackJackDealer:
  def __init__(self):
    self.hand = []

  def reset(self):
    self.hand = []

  def hit(self, deck):
    card = deck.draw()
    self.hand.append(card)
    return card

  @property
  def total(self):
    return calculate_hand_total(self.hand)

  @property
  def is_bust(self):
    return self.total > BLACKJACK

  @property
  def is_blackjack(self):
    return len(self.hand) == 2 and self.total == BLACKJACK


class BlackJackGame:
  """
    Represents a Black Jack Game.
  """
  def __init__(self, num_players=1):
    self.cards = Deck()
    self.players = [BlackJackPlayer() for _ in range(num_players)]
    self.dealer = BlackJackDealer()

  def play_round(self, bets=None):
    self.start_round(bets)
    self.handle_player_turns()
    self.handle_dealer_turn()
    return self.resolve_bets()

  def start_round(self, bets=None):
    if len(self.cards) < (len(self.players) + 1) * 2:
      self.cards.reset()

    self.dealer.reset()
    for player in self.players:
      player.reset()

    if bets is not None:
      if len(bets) != len(self.players):
        raise ValueError("Must provide one bet per player")
      for player, bet in zip(self.players, bets):
        player.place_bet(bet)

    self.deal_cards()

  def deal_cards(self):
    for _ in range(2):
      for player in self.players:
        player.hit(self.cards)
      self.dealer.hit(self.cards)

  def check_winner(self, player, pos: int = 0):
    hand = player.hands[pos]
    if hand.is_blackjack and not self.dealer.is_blackjack:
      return RoundResult.PLAYER_BLACKJACK
    if hand.is_bust:
      return RoundResult.DEALER_WIN
    if self.dealer.is_bust:
      return RoundResult.PLAYER_WIN
    if self.dealer.is_blackjack and not hand.is_blackjack:
      return RoundResult.DEALER_WIN
    if hand.total > self.dealer.total:
      return RoundResult.PLAYER_WIN
    if hand.total < self.dealer.total:
      return RoundResult.DEALER_WIN
    return RoundResult.PUSH

  def handle_player_turns(self):
    for player in self.players:
      for hand in player.hands:
        while hand.total < DEALER_STAND_TOTAL:
          hand.add_card(self.cards.draw())
        hand.is_standing = True

  def handle_dealer_turn(self):
    while self.dealer.total < DEALER_STAND_TOTAL:
      self.dealer.hit(self.cards)

  def resolve_bets(self):
    results = []
    for player_index, player in enumerate(self.players):
      for hand_index, hand in enumerate(player.hands):
        result = self.check_winner(player, hand_index)
        payout = self._payout_for(result, hand.bet)
        player.bankroll += payout
        results.append({
          "player": player_index,
          "hand": hand_index,
          "result": result,
          "bet": hand.bet,
          "payout": payout,
          "bankroll": player.bankroll,
        })
    return results

  def _payout_for(self, result, bet):
    if result == RoundResult.PLAYER_BLACKJACK:
      return bet + (bet * 3 // 2)
    if result == RoundResult.PLAYER_WIN:
      return bet * 2
    if result == RoundResult.PUSH:
      return bet
    return 0


def calculate_hand_total(cards):
  total = sum(card_value(card) for card in cards)
  aces = sum(1 for card in cards if card.get_rank() == "Ace")

  while total > BLACKJACK and aces:
    total -= 10
    aces -= 1

  return total


def card_value(card):
  rank = card.get_rank()
  if rank == "Ace":
    return 11
  if rank in {"Jack", "Queen", "King"}:
    return 10
  return int(rank)
