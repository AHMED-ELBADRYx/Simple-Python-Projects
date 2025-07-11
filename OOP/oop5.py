# Currency conversion!

import os
import time
from datetime import datetime
from enum import Enum, auto

class ConversionMode(Enum):
    OFFLINE = auto()

class CurrencyConverter:
    def __init__(self):
        # Updated exchange rates (as of November 2023)
        self.rates = {
            "USD": {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 151.47, "EGP": 30.58, "CNY": 7.30},
            "EUR": {"USD": 1.08, "EUR": 1.0, "GBP": 0.86, "JPY": 164.64, "EGP": 33.23, "CNY": 7.93},
            "GBP": {"USD": 1.26, "EUR": 1.16, "GBP": 1.0, "JPY": 191.12, "EGP": 38.61, "CNY": 9.21},
            "JPY": {"USD": 0.0066, "EUR": 0.0061, "GBP": 0.0052, "JPY": 1.0, "EGP": 0.20, "CNY": 0.048},
            "EGP": {"USD": 0.032, "EUR": 0.030, "GBP": 0.026, "JPY": 4.98, "EGP": 1.0, "CNY": 0.24},
            "CNY": {"USD": 0.14, "EUR": 0.13, "GBP": 0.11, "JPY": 20.82, "EGP": 4.19, "CNY": 1.0}
        }
        self.mode = ConversionMode.OFFLINE

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates[from_currency]:
            raise ValueError("Invalid currency code")
        rate = self.rates[from_currency][to_currency]
        return amount * rate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    print("""
___________________________________
|#######====================#######|
|#(1)UNITED STATES OF AMERICA(1)#|
|#**          /===/   ********  **#|
|# {G}      | (") |             #|
|#*  ******  | /v\\ |    O N E    *#|
|#(1)         \\===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
""")
    print("Supported currencies: USD, EUR, GBP, JPY, EGP, CNY\n")

def get_valid_currency(prompt, available_currencies):
    while True:
        currency = input(prompt).upper()
        if currency in available_currencies:
            return currency
        print(f"❌ Invalid currency. Please choose from {', '.join(available_currencies)}")

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("❌ Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

def animated_loading(message, duration=2):
    print(message, end='', flush=True)
    for _ in range(duration):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()

def main():
    converter = CurrencyConverter()
    available_currencies = list(converter.rates.keys())
    
    while True:
        show_banner()
        print(f"📶 Mode: Offline Rates")
        print(f"🕒 Last Updated: November 2023 Rates\n")
        
        # Get user input
        from_currency = get_valid_currency(
            "From currency (USD, EUR, GBP, JPY, EGP, CNY): ",
            available_currencies
        )
        
        amount = get_valid_amount(f"Amount in {from_currency}: ")
        
        to_currency = get_valid_currency(
            "To currency (USD, EUR, GBP, JPY, EGP, CNY): ",
            available_currencies
        )
        
        # Process conversion
        animated_loading("\n🔍 Calculating conversion")
        
        try:
            converted_amount = converter.convert(amount, from_currency, to_currency)
            rate = converter.rates[from_currency][to_currency]
            
            print(f"\n💱 Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
            print(f"💰 {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            
        except Exception as e:
            print(f"\n❌ Error during conversion: {str(e)}")
        
        # Continue or exit
        if input("\n🔁 Convert another amount? (Y/N): ").upper() != 'Y':
            print("\n💼 Thank you for using Currency Converter Pro!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")