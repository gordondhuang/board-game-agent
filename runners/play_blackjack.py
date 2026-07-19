import os
import sys

from games.card_games.blackjack import BLACKJACK, BlackJackGame


def main():
  game = BlackJackGame(num_players=1)
  player = game.players[0]

  print("Blackjack")
  print(f"Bankroll: ${player.bankroll}")
  bet = ask_for_bet(player.bankroll)

  game.start_round([bet])
  player_hand = player.hands[0]

  print_table(game, reveal_dealer=False)

  if player_hand.is_blackjack:
    print("Blackjack!")
  else:
    while not player_hand.is_bust:
      action = ask_for_action()

      if action == "h":
        card = player.hit(game.cards)
        print(f"You drew: {card}")
        print_table(game, reveal_dealer=False)
      elif action == "s":
        player.stand()
        break

  if player_hand.is_bust:
    print("You busted.")
  else:
    print("Dealer's turn.")
    print_table(game, reveal_dealer=True)

    while game.dealer.total < 17:
      card = game.dealer.hit(game.cards)
      print(f"Dealer drew: {card}")
      print_table(game, reveal_dealer=True)

  results = game.resolve_bets()
  result = results[0]

  print("Round result")
  print(f"Result: {result['result'].value}")
  print(f"Bet: ${result['bet']}")
  print(f"Payout: ${result['payout']}")
  print(f"Bankroll: ${result['bankroll']}")


def ask_for_bet(bankroll):
  while True:
    value = input("Place your bet: $").strip()

    try:
      bet = int(value)
    except ValueError:
      print("Please enter a whole number.")
      continue

    if bet <= 0:
      print("Bet must be greater than 0.")
    elif bet > bankroll:
      print("You cannot bet more than your bankroll.")
    else:
      return bet


def ask_for_action():
  while True:
    action = input("Hit or stand? [h/s]: ").strip().lower()
    if action in {"h", "hit"}:
      return "h"
    if action in {"s", "stand"}:
      return "s"
    print("Please choose hit or stand.")


def print_table(game, reveal_dealer):
  player = game.players[0]
  player_hand = player.hands[0]

  print()
  if reveal_dealer:
    print(f"Dealer: {format_hand(game.dealer.hand)} ({game.dealer.total})")
  else:
    visible_card = game.dealer.hand[0]
    print(f"Dealer: {visible_card}, [hidden]")

  print(f"You: {format_hand(player_hand.cards)} ({player_hand.total})")
  print()


def format_hand(cards):
  return ", ".join(str(card) for card in cards)


if __name__ == "__main__":
  main()
