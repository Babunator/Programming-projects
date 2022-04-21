import random

class Card_Info:
    def __init__(self, symbol, colour, number, value, current_card):
        self.symbol = symbol
        self.colour = colour
        self.number = number
        self.value = value
        self.current_card = current_card

    global all_used_cards

    def draw_card(self):
        # drawing a card that hasn't been used yet
        self.current_card =[]
        while self.current_card not in all_used_cards:
            self.colour = random.choice(["Red", "Black"])
            self.symbol = random.choice(["Club", "Spade", "Heart", "Diamond"])
            self.number = str(random.choice([_ for _ in range(2, 11)] + ['Jack']+ ['Queen']+ ['King']+ ['Ace']))

            self.current_card.append(self.colour  + " " + self.symbol + " " + self.number)
            if self.current_card in all_used_cards:
                continue
            all_used_cards.append(self.current_card)
        return self.current_card

    def card_value(self):
        self.value = {"Ace": (1, 11), "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "King": 10,
         "Queen": 10, "Jack": 10}[self.number]
        return self.value

def new_game_setup():
    # New game will be setup.
    global all_used_cards
    global dealer_cards
    global player_cards
    global stand
    all_used_cards = []
    dealer_cards = []
    player_cards = []
    stand = False
    split = False

def ask_new_game():
    # Asking if the Player wants to play a new game
    global game_rounds
    if game_rounds > 1:
        play_again = input("Do you want to play again? Y/N").lower
        while True:
            if play_again == "y":
                new_game_setup()
                game_rounds = + 1
                break
            elif play_again == "n":
                # SOMETHING HAPPENING TO CLOSE
                pass
                break
            else:
                play_again = input("Sorry invalid input. Do you want to play again? Y/N").lower


def give_bet(amount):
    global money
    while True:
        if money >= amount:
            money = money - amount
            break
        else:
            amount = float(input("Sorry, you don't have that much money. How much € do you want to bet?"))
    print(f"You now have {money}€ left.")
    return amount


def hit():
    if split == True:
        player_cards.append(Card_Info("", "", "", "", "").draw_card())
        split_player_cards.append(Card_Info("", "", "", "", "").draw_card())
    else:
        player_cards.append(Card_Info("","","","","").draw_card())

def double_down(amount):
    if amount < money:
        give_bet(amount)
    else:
        print("Sorry, you don't have enough money, but you can still hit.")
    player_cards.append(Card_Info("","","","","").draw_card())

def stand():
    global stand
    stand = True

def split():
    if amount < money:
        give_bet(amount)
        symbol_1 = []
        for i in player_cards[0]: symbol_1.extend(i.split())
        symbol_2 = []
        for i in player_cards[1]: symbol_2.extend(i.split())
        # checking if the 2 cards are the same
        if symbol_1[2] == symbol_2[2]:
            split_player_cards = player_cards.pop(1)
            player_cards.append(Card_Info("", "", "", "", "").draw_card())
            split_player_cards.append(Card_Info("", "", "", "", "").draw_card())
            split = True
        else:
            print("Sorry, you need to have 2 cards with the same number/picture. You can still hit."
            player_cards.append(Card_Info("", "", "", "", "").draw_card())
    else:
        print("Sorry, you need to bet the same betting amount again to split. You don't have enough money, but you can still hit.")


def check_busted():
    player_value1 = 0
    if split == True:
        pass
    else:
        for j in range(len(player_cards)):
            for i in player_cards[j]: value_list.extend(i.split())
            player_value1 += Card_Info("", "", value_list[2], "", "").card_value()
        if player_value1 > 21:
            print("Sorry, you busted. The house wins.")
            stand()

# _________________________________________________________________
# Defining some parameters
all_used_cards = []
dealer_cards = []
player_cards = []
split_player_cards =[]
game_rounds = 1
money = float(1000)
stand = False
split = False

print("These are the rules. bla bla bla")

while True:
    # At the beginning player get 2 cards and the dealer 1
    player_cards.append(Card_Info("","","","","").draw_card())
    player_cards.append(Card_Info("","","","","").draw_card())
    dealer_cards.append(Card_Info("","","","","").draw_card())
    # Player can bet money
    bet = give_bet(float(input(f"You currently have {money}€. How much € do you want to bet?:")))
    # Show the player the cards.
    print(f'The Dealer has a {dealer_cards[0]}. \nYou have on your hand:')
    for i in range(len(player_cards)): print(player_cards[i])

    player_choice = int(input("\nWhat do you want to do? Do you want to hit(1), stand(2), double down(3) or split(4)?. Enter a number 1-4."))
    current_round = 1
    while stand == False:
        if current_round == 1:
            if player_choice == 1:
                hit()
                current_round +=1
            elif player_choice == 2:
                stand()
                current_round +=1
            elif player_choice == 3:
                double_down(bet)
                current_round +=1
            elif player_choice == 4:
                split()
                current_round +=1
            else:
                player_choice = int(input("Sorry, your input was invalid. Do you want to hit(1), stand(2), double down(3) or split(4)?. Enter a number 1-4."))
        if current_round > 1:
            print(f'The Dealer has a {dealer_cards[0]}. \nYou have on your hand:')
            for i in range(len(player_cards)): print(player_cards[i])
            player_choice = int(input("\nWhat do you want to do? Do you want to hit(1) or stand(2)?. Enter 1 or 2."))
            if player_choice == 1:
                hit()
            elif player_choice == 2:
                stand()
            else:
                player_choice = int(input("Sorry, your input was invalid. Do you want to hit(1) or stand(2)?. Enter 1 or 2."))








