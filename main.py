# card game
import random
import time

random.seed(random.randint(1,1000))

deck = []
colours = ["Red", "Yellow", "Black"]
player1_cards = []
player2_cards = []
player1_won = False
player2_won = False


def display_cards(d):
    for x in d:
        colour = x.get_colour()
        number = x.get_number()
        print(" " + colour + " " + str(number))

class Card:
    def __init__(self, colour:str, number:int):
        self.colour = colour
        self.number = number

    def get_colour(self):
        return self.colour

    def get_number(self):
        return self.number


for x in range(1,11):
    #print("Iteration: " + str(x)) - for testing purposes
    y = Card("Red", x)
    z = Card("Yellow", x)
    a = Card("Black", x)

    deck.append(y)
    deck.append(z)
    deck.append(a)

#testing method to display deck
#for y in deck:
 #   print("Card:" + y.get_colour() + " " + str(y.get_number()))


# main game
while len(deck) > 0:
    #game continues
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    deck.remove(card2)

    cards = [card1, card2]
    cards_colours = [card1.get_colour(), card2.get_colour()]
    
    print("Player 1 has the card: " + card1.get_colour() + " " + str(card1.get_number()))
    time.sleep(1)
    print("Player 2 has the card: " + card2.get_colour() + " " + str(card2.get_number()))
    time.sleep(1)
    #compare cards
    if card1.get_colour() == card2.get_colour():
        #they are the same colour
        print("Both cards are the same colour, the numbers shall be compared!")
        if card1.get_number() > card2.get_number():
            #player1 has won and gets both cards
            print("Player 1's card has a greater number and has won!")
            player1_cards.append(card1)
            player1_cards.append(card2)
        elif card1.get_number() < card2.get_number():
            #player2 has won
            print("Player 2's card has a greater number and has won!")  
            player2_cards.append(card1)
            player2_cards.append(card2)
        else:
            #this isn't even possible
            print("How did we get here?")

            
    else:
        #they are not the same colour
        print("The cards are not the same colour!")
        if cards_colours[0] == "Red" and cards_colours[1] == "Black":
            #card1 (player1) will win
            print("Red beats Black so Player 1 has won!, they take both cards!")
            player1_cards.append(card1)
            player1_cards.append(card2)
        elif cards_colours[0] == "Black" and cards_colours[1] == "Red":
            #card2 (player2) will win
            print("Red beats Black so Player 2 has won!, they take both cards!")
            player2_cards.append(card1)
            player2_cards.append(card2)
        elif cards_colours[0] == "Yellow" and cards_colours[1] == "Red":
            #card1 (player1) will win
            print("Yellow beats Red so Player 1 has won!, they take both cards!")
            player1_cards.append(card1)
            player1_cards.append(card2)
        elif cards_colours[0] == "Red" and cards_colours[1] == "Yellow":
            #card2 (player2) will win
            print("Yellow beats Red so Player 2 has won!, they take both cards!")
            player2_cards.append(card1)
            player2_cards.append(card2)
        elif cards_colours[0] == "Black" and cards_colours[1] == "Yellow":
            #card1 (player1) will win
            print("Black beats Yellow so Player 1 has won!, they take both cards!")
            player1_cards.append(card1)
            player1_cards.append(card2)
        elif cards_colours[0] == "Yellow" and cards_colours[1] == "Black":
            #card2 (player2) will win
            print("Black beats Yellow so Player 2 has won!, they take both cards!")
            player2_cards.append(card1)
            player2_cards.append(card2)
        else: print("How did we even get here?")
    
    # end of round - print decks
    time.sleep(1)
    print("End of round!:")
    print("Player 1's Cards:")
    display_cards(player1_cards)
    print("Player 2's Cards:")
    display_cards(player2_cards)
    time.sleep(1)

time.sleep(2)
p1len = len(player1_cards)
p2len = len(player2_cards) 
# rounds have finished - calculate game end
if p1len ==  p2len:
    #overtime
    u = random.randint(1,10)
    i = random.randint(1,10)
    
    while u == i:
        i = random.randint(1,10)
    else:
        print("Player 1 your number is: " + str(u))
        print("Player 2 your number is: " + str(i))
        
        if u > i:
            #player 1 has won
            print("Player 1 has won! Their deck is:")
            display_cards(player1_cards)
        else:
            #player 2 has won
            print("Player 2 has won! Their deck is:")
            display_cards(player2_cards)
        
elif p1len > p2len:
    #player1 has won
    player1_won = True
    print("Player 2 has won! Their deck is:")
    display_cards(player2_cards)
elif p1len < p2len:
    #player2 has won
    player2_won = True
    print("Player 2 has won! Their deck is:")
    display_cards(player2_cards)
else: print("How did we get here?")