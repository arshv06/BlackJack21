from unicodedata import name
import time
import random

def deck(count):
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]  
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    d_cards = {}
    for i in range(0, count):
        for suit in suits:
            for card in cards:
                d_cards[card, suit, i] = cards_values[card]

    return d_cards           
     
class Player():
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
    def money_lost(self, input_bet):
        self.balance -= input_bet 
        print("Balance Remaining: ", self.balance) 
    def money_won(self, input_bet):
        self.balance += input_bet     
        print("Balance Remaining: ", self.balance)  
    def money_wondd(self, input_bet):
        self.balance += input_bet * 2
        print("Balance Remaining: ", self.balance) 
    def blackjack(self, input_bet):
        self.balance += input_bet * 2.5 
        print("Balance Remaining: ", self.balance)  
    def push(self, input_bet):
        None              

def card_sum(list):
    card_total = 0
    for value in list.values():
        card_total += value
    return card_total

def dealer_bust_check(card_total):
    global dcard_total, input_bet, player_cards, dealer_cards
    if dcard_total > 21:    
        print("dealer's cards: ", list(dealer_cards.keys()))
        print("Dealer Bust!")
        Player1.money_won(input_bet)     
        playing = False
        return playing

    elif dcard_total < card_total:
        print("Your Cards    : ", list(player_cards.keys()))
        print("//////////////////////////")
        print("dealer's cards: ", list(dealer_cards.keys())) 
        print("Higher Value! You Won!")
        Player1.money_won(input_bet)
        playing = False
        return playing

    elif dcard_total > card_total:
        print("Your Cards    : ", list(player_cards.keys()))
        print("//////////////////////////")
        print("dealer's cards: ", list(dealer_cards.keys())) 
        print("Dealer Won!")
        Player1.money_lost(input_bet)
        playing = False
        return playing

    elif dcard_total == card_total:
        print("Your Cards    : ", list(player_cards.keys()))
        print("//////////////////////////")
        print("dealer's cards: ", list(dealer_cards.keys())) 
        print("It's a push!")
        Player1.push(input_bet)
        print("Balance Remaining: ", Player1.balance)
        playing = False
        return playing
    return Player1.balance    
        
def player_bust_check(card_total):
    global dcard_total, input_bet, player_cards, dealer_cards
    if card_total > 21:
        print(list(player_cards.keys()), card_total)
        print("Bust!")
        Player1.money_lost(input_bet)
        playing = False
        return playing
        return Player1.balance
    else:
        return None           

Player1= Player(input("Please enter your name: "))
d_cards = deck(int(input("No. of Decks: ")))
print("Welcome to BlackJack 21 {}!. Have fun. BTW, free 100$ to play 4 the babezz!".format(Player1.name))

if True:
    ready = input(f"Ready to play {Player1.name}? y/n ")
    while (ready == "y" and Player1.balance > 15): 
        playing = True
        dealer_cards = {}
        player_cards = {} 
        while True:
            try:
                input_bet = int(input("Minimum Bet is 15$, Please Place your bets (in $) when ready: "))                
            except ValueError:
                print("I repeat the Minimum bet is 15$. Place your bet again")
                continue 
            if input_bet in range(15, Player1.balance+1):
                break 
            

        print(("Bet registered: ") + str(input_bet))
        print("Dealing Cards.............")   
        time.sleep(4)

        while len(dealer_cards) <  2:
            card = random.choice(list(d_cards.items()))
            dealer_cards[card[0]] = card[1] 
        while len(player_cards) <  2:
            card = random.choice(list(d_cards.items()))
            player_cards[card[0]] = card[1] 

        if list(player_cards.values())[0] == 11 and list(player_cards.values())[1] == 11:
           player_cards[list(d_cards.keys())[list(d_cards.values()).index(11)]] = 1

        if list(dealer_cards.values())[0] == 11 and list(dealer_cards.values())[1] == 11:
           dealer_cards[list(d_cards.keys())[list(d_cards.values()).index(11)]] = 1

        card_total = card_sum(player_cards)
        dcard_total= card_sum(dealer_cards)

        if card_total == 21: 
            print("You got a BlackJack! Congratulations")
            print("Your Cards    : ", list(player_cards.keys()))
            print("Dealer's cards:  ", list(dealer_cards.keys())[0],"  __")
            Player1.blackjack(input_bet)
            continue

        if dcard_total == 21: 
            print("Dealer got a BlackJack! Sorry.")
            print("Your Cards    : ", list(player_cards.keys()))
            print("Dealer's cards:  ", list(dealer_cards.keys()))           
            Player1.money_lost(input_bet)  
            continue

        
        print("Your Cards    : ", list(player_cards.keys()))
        print("Dealer's cards:  ", list(dealer_cards.keys())[0],"  __")  
 
        while playing == True:
            move = input("""
            What's your next move?
            Hit / Stand / Split / Double Down
            """)
            if move.lower() == "hit":
                card = random.choice(list(d_cards.items()))
                player_cards[card[0]] = card[1] 
                card_total = card_sum(player_cards)
                if card_total > 21 and 11 in list(player_cards.values()): 
                   key = [k for k in player_cards.keys() if player_cards[k] == 11]
                   player_cards[key[0]] = 1
                   card_total -= 10
                if player_bust_check(card_total) != None:
                    break
                else:
                    print("Your Cards: ", list(player_cards.keys()))
                    continue
                

            elif move.lower() == "stand":
                print("Dealer's Turn")
                dcard_total = card_sum(dealer_cards)
                while dcard_total < 17:
                    card = random.choice(list(d_cards.items()))
                    dealer_cards[card[0]] = card[1] 
                    dcard_total = card_sum(dealer_cards)
                    if dcard_total > 21 and 11 in list(dealer_cards.values()):
                        key = [k for k in dealer_cards.keys() if dealer_cards[k] == 11]
                        dealer_cards[key[0]] = 1
                        dcard_total -= 10 
                dealer_bust_check(card_total)
                break    
            

            elif move.lower() == "double down":
                if (card_total in (8, 9 ,10, 11) and len(player_cards) == 2):
                    print("Doubling!")
                    input_bet = input_bet * 2
                    card = random.choice(list(d_cards.items()))
                    player_cards[card[0]] = card[1] 
                    card_total = card_sum(player_cards)
                    if card_total > 21 and 11 in list(player_cards.values()):
                        key = [k for k in player_cards.keys() if player_cards[k] == 11]
                        player_cards[key[0]] = 1
                        card_total -= 10 
                    print("Your Cards: ", list(player_cards.keys()))
                    if player_bust_check(card_total) != None:
                        break
                    else:
                        print("Dealer's Turn")
                        dcard_total = card_sum(dealer_cards)
                        while dcard_total < 17:
                            card = random.choice(list(d_cards.items()))
                            dealer_cards[card[0]] = card[1] 
                            dcard_total = card_sum(dealer_cards)
                            if dcard_total > 21 and 11 in list(dealer_cards.values()):
                                key = [k for k in dealer_cards.keys() if dealer_cards[k] == 11]
                                dealer_cards[key[0]] = 1
                                dcard_total -= 10 
                        dealer_bust_check(card_total) 
                        break
                else:
                     print("Sorry, Can't Double Down")
                continue

            elif move.lower() == "split":
                if list(player_cards.keys())[0][0] == list(player_cards.keys())[1][0]:
                    print("Spliting!")
                    deck1 = {}
                    deck2 = {} 
                    print("Splitting into two decks")
                    deck1[list(player_cards.keys())[0]] = list(player_cards.values())[0]
                    deck2[list(player_cards.keys())[1]] = list(player_cards.values())[1]
                else:
                    print("Sorry, Can't Split")
                    continue    

                S1move = input("""
                What's your next move?
                Hit / Stand
                """)
                while S1move.lower() == "hit":
                    card = random.choice(list(d_cards.items()))
                    deck1[card[0]] = card[1] 
                    deck1_total = card_sum(deck1)
                    if deck1_total > 21 and 11 in list(deck1.values()):
                        key = [k for k in deck1.keys() if deck1[k] == 11]
                        deck1[key[0]] = 1
                        deck1_total -= 10 
                    if deck1_total > 21:
                        print("Your Cards: ", list(deck1.keys()))
                        print("Your Cards: ", list(deck2.keys()))
                        print("Deck 1 Bust!")
                        break  
                    print("Your Cards: ", list(deck1.keys()))
                    print("Your Cards: ", list(deck2.keys()))
                    S1move = input("""
                    What's your next move?
                    Hit / Stand
                    """)

            
                S2move = input("""
                and For the 2nd Deck, What's your next move?
                Hit / Stand
                """)
                while S2move.lower() == "hit":
                    card = random.choice(list(d_cards.items()))
                    deck2[card[0]] = card[1] 
                    deck2_total = card_sum(deck2)
                    if deck2_total > 21 and 11 in list(deck2.values()):
                        key = [k for k in deck2.keys() if deck2[k] == 11]
                        deck2[key[0]] = 1
                        deck2_total -= 10 
                    if deck2_total > 21:
                       print("Your Cards: ", list(deck1.keys()))
                       print("Your Cards: ", list(deck2.keys()))
                       print("Deck 2 Bust!")
                       break  
                    print("Your Cards: ", list(deck1.keys()))
                    print("Your Cards: ", list(deck2.keys()))
                    S2move = input("""
                    and What's your next move?
                    Hit / Stand
                    """)                                 

                    
                print("Dealer's Turn")
                dcard_total = card_sum(dealer_cards)
                while dcard_total < 17:
                    card = random.choice(list(d_cards.items()))
                    dealer_cards[card[0]] = card[1] 
                    dcard_total = card_sum(dealer_cards)
                    if dcard_total > 21 and 11 in list(dealer_cards.values()):
                        key = [k for k in dealer_cards.keys() if dealer_cards[k] == 11]
                        dealer_cards[key[0]] = 1
                        dcard_total -= 10 
                print("Your Cards: ", list(deck1.keys()))
                print("Your Cards: ", list(deck2.keys()))
                if deck1_total < 22:
                   print("Deck 1 Check")
                   dealer_bust_check(deck1_total)
                else:
                   player_bust_check(deck1_total)
   

                if deck2_total < 22:
                   print("Deck 2 Check")
                   dealer_bust_check(deck2_total)
                else:
                   player_bust_check(deck2_total)   

                    
                break
        
            else: print("Invalid Input")
            continue 

        ready = input("Continue? y/n (Type Q to Quit)")

  
    print("Thank you for Playing!")
    print("Your net balance:", Player1.balance)
