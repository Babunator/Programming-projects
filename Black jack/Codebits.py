import random

all_used_cards = []
values_cards_dealer = []
values_cards_player = []
game_rounds = 1

class Cards_Info:
    def __init__(self, symbol, colour, number, value, current_card):
        self.symbol = symbol
        self.colour = colour
        self.number = number
        self.value =  value
        self.current_card = current_card
     
    global all_used_cards    
    
    def draw_card(self):
        # drawing a card that hasn't been used yet
        while self.current_card not in all_used_cards:
            self.colour = random.choice(["Red", "Black"])
            self.symbol = random.choice(["Club", "Spade", "Heart", "Diamond"])
            self.number = random.choice(["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack"])
            self.value = {"Ace":(1,11), "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "King":10, "Queen":10, "Jack":10}[self.number]
            self.current_card = self.colour + "_" + self.symbol + "_" + self.number
            if self.current_card in all_used_cards:
                break
            all_used_cards.append(self.current_card)
            return self.current_card
    
    def current_card_value(self):
        return self.value
    
        
class Game_setup:
    def __init__(self, player_card_1, player_card_2, dealer_card_1):
        self.player_card_1 = player_card_1
        self.player_card_2 = player_card_2
        self.dealer_card_1 = dealer_card_1

    def new_game_setup(self):
        # New game will be setup.
        global all_used_cards
        global values_cards_player
        global values_cards_dealer
        all_used_cards = []
        values_cards_dealer = []
        values_cards_player = []
        
        # Player gets 2 cards at the beginning & 1 new dealer card
        new_card = Cards_Info("","","","","")
        self.player_card_1 = new_card.draw_card()
        values_cards_player.append(new_card.value)
        new_card = Cards_Info("","","","","")
        self.player_card_2 = new_card.draw_card()
        values_cards_player.append(new_card.value)
        new_card = Cards_Info("","","","","")
        self.dealer_card_1 = new_card.draw_card()
        values_cards_dealer.append(new_card.value)
        
    def first_game(self):
        # Explaining rules
        print("These are the rules. bla bla bla")
        self.new_game_setup()
    
    def ask_new_game(self):
        # Asking if the Player wants to play a new game
        if game_rounds > 1:
            play_again = input("Do you want to play again? Y/N").lower
            while true:
                if play_again == "y":
                    new_game_setup()
                    game_rounds =+ 1
                    break
                elif play_again =="n":
                    # SOMETHING HAPPENING TO CLOSE
                    pass
                    break
                else:
                    play_again = input("Sorry invalid input. Do you want to play again? Y/N").lower
            