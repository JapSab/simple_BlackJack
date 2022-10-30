import random
playerIn = True
dealerIn = True

# deck of cards / player/dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', ]
player_hand = []
dealers_hand = []


# card dealing function
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand


def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# check for winner


def revealDealerHand():
    if len(dealers_hand) == 2:
        return dealers_hand[0]
    elif len(dealers_hand) > 2:
        return dealers_hand[0], dealers_hand[1]

# game loop over


for _ in range(2):
    dealCard(dealers_hand)
    dealCard(player_hand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealers_hand) > 16:
        dealerIn = False
    else:
        dealCard(dealers_hand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealers_hand) >= 21:
        break


if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("Blackjack! You win!")
elif total(dealers_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("Blackjack! Dealer wins!")
elif total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("You bust! Dealer wins")
elif total(dealers_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("Dealer busts! You win!")
elif 21 - total(dealers_hand) < 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("Dealer wins!")
elif 21 - total(dealers_hand) > 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
    print("You win!")
