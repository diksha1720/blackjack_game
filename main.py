
import art
import random
from replit import clear


def print_cards(computer_cards, player_cards):
  clear()
  print(f"Computer's cards {computer_cards}")
  print(f"Computer's total {sum(computer_cards)}")
  print(f"Your cards {player_cards}")
  print(f"Your total {sum(player_cards)}")



def results(computer_cards,player_cards):
  print_cards(computer_cards,player_cards)
  if sum(player_cards)==sum(computer_cards):
    print("\nDraw")
  elif sum(player_cards)>21:
    print("\nYou lose")
  elif sum(computer_cards)>21:
    print("\nYou win")
  elif sum(computer_cards)<sum(player_cards):
    print("\nYou win")
  elif sum(computer_cards)>sum(player_cards):
    print("\nYou lose")
  print("Game Over")

def play():
  clear()
  print(art.logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards=random.sample(cards, 2)
  computer_cards=random.sample(cards, 2)
  flag=True
  while flag:
    if sum(computer_cards)>21 or sum(player_cards)>21:
      results(computer_cards, player_cards)
      return
    print(f"Your cards: {player_cards}\nCurrent score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}\n")
    choice=input("Type 'y' to get another card, type 'n to pass:'")
    if choice=='y':
      player_cards.append(random.choice(cards))
      if sum(computer_cards)<17:
        computer_cards.append(random.choice(cards))
    else:
      flag=False
  results(computer_cards, player_cards)
  

flag=True
while(True):
  ans=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
  if ans=='y':
    play()
    break
  else:
    flag=False
