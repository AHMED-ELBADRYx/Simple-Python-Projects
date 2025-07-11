# Blackjack

import random
import os
import time
from enum import Enum, auto

class GameResult(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()
    BLACKJACK = auto()

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        value_map = {11: "A", 10: "10", 9: "9", 8: "8", 
                    7: "7", 6: "6", 5: "5", 4: "4", 
                    3: "3", 2: "2"}
        return f"{value_map[self.value]}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()
        
    def reset(self):
        suits = ['♠', '♥', '♦', '♣']
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) < 10:  # Reshuffle when running low
            self.reset()
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.calculate_score()
    
    def calculate_score(self):
        self.score = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.value == 11)
        
        while self.score > 21 and aces:
            self.score -= 10
            aces -= 1
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.score == 21
    
    def __str__(self):
        return " ".join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.balance = 1000
        self.current_bet = 0
    
    def place_bet(self):
        clear_screen()
        print(f"💰 Current Balance: ${self.balance}")
        while True:
            try:
                bet = int(input("\nPlace your bet (min $10): $"))
                if bet < 10:
                    print("Minimum bet is $10")
                elif bet > self.balance:
                    print("You don't have enough funds")
                else:
                    self.current_bet = bet
                    self.balance -= bet
                    break
            except ValueError:
                print("Please enter a valid number")
    
    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
    
    def player_turn(self):
        while True:
            clear_screen()
            self.display_hands(hide_dealer_card=True)
            
            if self.player_hand.score > 21:
                break
            
            choice = input("\nHit or Stand? (H/S): ").lower()
            if choice == 'h':
                self.player_hand.add_card(self.deck.deal())
            elif choice == 's':
                break
            else:
                print("Invalid choice. Enter H or S.")
                time.sleep(3)
    
    def dealer_turn(self):
        while self.dealer_hand.score < 17 and self.player_hand.score <= 21:
            self.dealer_hand.add_card(self.deck.deal())
            time.sleep(1)
            clear_screen()
            self.display_hands()
            print("\nDealer draws a card...")
    
    def determine_result(self):
        if self.player_hand.is_blackjack():
            return GameResult.BLACKJACK
        elif self.player_hand.score > 21:
            return GameResult.LOSE
        elif self.dealer_hand.is_blackjack():
            return GameResult.LOSE
        elif self.dealer_hand.score > 21:
            return GameResult.WIN
        elif self.player_hand.score > self.dealer_hand.score:
            return GameResult.WIN
        elif self.player_hand.score < self.dealer_hand.score:
            return GameResult.LOSE
        else:
            return GameResult.DRAW
    
    def payout(self, result):
        if result == GameResult.BLACKJACK:
            win_amount = int(self.current_bet * 1.5)
            self.balance += self.current_bet + win_amount
            return win_amount
        elif result == GameResult.WIN:
            self.balance += self.current_bet * 2
            return self.current_bet
        elif result == GameResult.DRAW:
            self.balance += self.current_bet
            return 0
        else:
            return -self.current_bet
    
    def display_hands(self, hide_dealer_card=False):
        print("\nDealer's Hand:")
        if hide_dealer_card:
            print(f"{self.dealer_hand.cards[0]} ?")
            print(f"Score: ?")
        else:
            print(self.dealer_hand)
            print(f"Score: {self.dealer_hand.score}")
        
        print("\nYour Hand:")
        print(self.player_hand)
        print(f"Score: {self.player_hand.score}")
    
    def play_round(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.place_bet()
        self.deal_initial_cards()
        
        # Check for immediate blackjack
        if self.player_hand.is_blackjack():
            clear_screen()
            self.display_hands()
            print("\nBlackjack! 🎉")
            result = GameResult.BLACKJACK
        else:
            self.player_turn()
            if self.player_hand.score <= 21:
                self.dealer_turn()
            result = self.determine_result()
        
        clear_screen()
        self.display_hands()
        
        result_messages = {
            GameResult.BLACKJACK: "Blackjack! You win 1.5x your bet! 🎉",
            GameResult.WIN: "You win! 🎉",
            GameResult.LOSE: "Dealer wins. 😢",
            GameResult.DRAW: "It's a push. Your bet is returned. 🤝"
        }
        
        win_amount = self.payout(result)
        print(f"\n{result_messages[result]}")
        if win_amount > 0:
            print(f"You won ${win_amount}!")
        elif win_amount < 0:
            print(f"You lost ${abs(win_amount)}")
        
        print(f"\n💰 New Balance: ${self.balance}")
        input("\nPress Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    clear_screen()
    print(r"""
__      __       .__                        
/  \    /  \ ____ |  |   ____  ____   _____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \ 
 \        /\  __/|  |\  \(  <_> )  Y Y  \
  \/\  /  \___  >/\___  >/||_|  /
       \/       \/          \/            \/ 
    """)
    time.sleep(2)

def main():
    show_welcome()
    game = BlackjackGame()
    
    while True:
        clear_screen()
        print(f"💰 Current Balance: ${game.balance}")
        print("\n1. Play Blackjack")
        print("2. Rules")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            if game.balance < 10:
                print("\nYou don't have enough money to play!")
                input("Press Enter to continue...")
                continue
            game.play_round()
        elif choice == '2':
            clear_screen()
            print("""
            Blackjack Rules:
            - Try to get as close to 21 without going over
            - Face cards are worth 10, Aces are 11 or 1
            - Blackjack (Ace + 10) pays 1.5x your bet
            - Dealer must hit until they reach 17
            - Standard payouts: 1:1 for win, push for tie
            """)
            input("\nPress Enter to continue...")
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()