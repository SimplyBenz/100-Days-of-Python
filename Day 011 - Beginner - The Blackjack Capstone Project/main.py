import random
from operator import itemgetter

import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calc_score(card_in_hand):
    score = 0
    for item in card_in_hand:
        if item == 11:
            score += 0
        else:
            score += item
    for item in card_in_hand:
        if item == 11 and score <= 10:
            score += 11
        elif item == 11 and score > 10:
            score += 1
    return score

def draw_card():
    random_card = random.choice(cards)
    return random_card

def compare(dealer_score,player_score):
    if dealer_score == player_score:
        print("DRAW")
    elif dealer_score > player_score and dealer_score <= 21 :
        print("Dealer WIN")
    elif player_score > dealer_score and player_score <= 21 :
        print("You WIN")
    elif player_score > 21 and dealer_score <= 21 :
        print("Dealer WIN")
    elif dealer_score > 21 and player_score <= 21 :
        print("Player WIN")

def game_start(game_status):
    dealer_hand = []
    player_hand = []
    if game_status == "y":
        print(art.logo)
        count = 0
        while count < 2: #draw 2 cards to both dealer and player
            dealer_hand.append(draw_card())
            player_hand.append(draw_card())
            count += 1
    else:
        exit()

    print(f"Your cards: {player_hand} current score:{player_hand[0] + player_hand[1]}")
    print(f"Computer first card is {dealer_hand[0]}")
    print(dealer_hand)

    for item in dealer_hand:
        if len(dealer_hand) <= 4 and calc_score(dealer_hand) <= 16: #if score in dealer hand <= 16 and not more than 4 cards dealer will draw card.
            dealer_hand.append(draw_card())
        else:
            break

    draw_status = input("Type 'y' to get another card or type 'n' to pass:").lower()

    if draw_status == "y":
        player_hand.append(draw_card())
        print(f"You got {player_hand[-1]} now you have {player_hand}")
        draw_status = input("Type 'y' to get another card or type 'n' to pass:").lower()
        if draw_status == "y":
            player_hand.append(draw_card())
            print(f"You got {player_hand[-1]} now you have {player_hand}")

    print(compare(dealer_score=calc_score(dealer_hand), player_score=calc_score(player_hand)))
    print(player_hand)
    print(dealer_hand)

    game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    game_start(game_status)

game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
game_start(game_status)