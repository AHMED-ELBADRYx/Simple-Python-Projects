# Match money with cost

import os
from enum import Enum, auto
from dataclasses import dataclass
from typing import List
import json
from datetime import datetime

class TransactionResult(Enum):
    SUCCESS = auto()
    INSUFFICIENT_FUNDS = auto()
    INVALID_INPUT = auto()

@dataclass
class Transaction:
    item: str
    quantity: int
    unit_price: float
    total_cost: float
    timestamp: str
    result: TransactionResult
    remaining_balance: float

class BudgetCalculator:
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.current_balance = 0.0
        self.load_data()

    def calculate_total(self, quantity: int, unit_price: float) -> float:
        return quantity * unit_price

    def process_transaction(self, item: str, quantity: int, unit_price: float) -> TransactionResult:
        try:
            total_cost = self.calculate_total(quantity, unit_price)
            
            if total_cost <= self.current_balance:
                self.current_balance -= total_cost
                result = TransactionResult.SUCCESS
            else:
                result = TransactionResult.INSUFFICIENT_FUNDS
            
            transaction = Transaction(
                item=item,
                quantity=quantity,
                unit_price=unit_price,
                total_cost=total_cost,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                result=result,
                remaining_balance=self.current_balance
            )
            self.transactions.append(transaction)
            self.save_data()
            return result
            
        except (ValueError, TypeError):
            return TransactionResult.INVALID_INPUT

    def add_funds(self, amount: float):
        self.current_balance += amount
        self.save_data()

    def save_data(self):
        data = {
            "balance": self.current_balance,
            "transactions": [
                {
                    "item": t.item,
                    "quantity": t.quantity,
                    "unit_price": t.unit_price,
                    "total_cost": t.total_cost,
                    "timestamp": t.timestamp,
                    "result": t.result.name,
                    "remaining_balance": t.remaining_balance
                } for t in self.transactions
            ]
        }
        with open("budget_data.json", "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        try:
            with open("budget_data.json", "r") as f:
                data = json.load(f)
                self.current_balance = data["balance"]
                self.transactions = [
                    Transaction(
                        item=t["item"],
                        quantity=t["quantity"],
                        unit_price=t["unit_price"],
                        total_cost=t["total_cost"],
                        timestamp=t["timestamp"],
                        result=TransactionResult[t["result"]],
                        remaining_balance=t["remaining_balance"]
                    ) for t in data["transactions"]
                ]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass

    def generate_report(self):
        print("\n📊 Budget Report")
        print("="*40)
        print(f"Current Balance: ${self.current_balance:.2f}")
        print("\nRecent Transactions:")
        for t in self.transactions[-5:]:
            status = "✅" if t.result == TransactionResult.SUCCESS else "❌"
            print(f"{status} {t.timestamp}: {t.quantity}x {t.item} @ ${t.unit_price:.2f} = ${t.total_cost:.2f}")
        print("="*40)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_numeric_input(prompt: str, input_type=float) -> float:
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a positive number.")

def main():
    calculator = BudgetCalculator()
    
    while True:
        clear_screen()
        print("💰 Budget Calculator")
        print("1. Add Funds")
        print("2. Make Purchase")
        print("3. View Report")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            clear_screen()
            print("💵 Add Funds")
            amount = get_numeric_input("Enter amount to add: $")
            calculator.add_funds(amount)
            print(f"\n✅ Added ${amount:.2f}. New balance: ${calculator.current_balance:.2f}")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            clear_screen()
            print("🛒 Make Purchase")
            item = input("Item name: ").strip()
            quantity = get_numeric_input("Quantity: ", int)
            unit_price = get_numeric_input("Unit price: $")
            
            result = calculator.process_transaction(item, quantity, unit_price)
            
            if result == TransactionResult.SUCCESS:
                print("\n✅ Purchase successful!")
                print(f"Remaining balance: ${calculator.current_balance:.2f}")
            elif result == TransactionResult.INSUFFICIENT_FUNDS:
                total = calculator.calculate_total(quantity, unit_price)
                print("\n❌ Insufficient funds!")
                print(f"Required: ${total:.2f} | Available: ${calculator.current_balance:.2f}")
            else:
                print("\n❌ Invalid transaction details")
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            clear_screen()
            calculator.generate_report()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            calculator.save_data()
            print("\n💾 Data saved. Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()