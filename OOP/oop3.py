# Salary calculation after tax

from dataclasses import dataclass
from typing import List
import json
from datetime import datetime

class TaxBracket:
    def __init__(self, min_income, max_income, rate):
        self.min_income = min_income
        self.max_income = max_income
        self.rate = rate

@dataclass
class SalaryRecord:
    date: str
    base_salary: float
    bonus: float
    tax: float
    net_salary: float

class SalaryCalculator:
    TAX_BRACKETS = [
        TaxBracket(0, 10000, 0.10),
        TaxBracket(10001, 40000, 0.15),
        TaxBracket(40001, 80000, 0.20),
        TaxBracket(80001, float('inf'), 0.25)
    ]
    
    def __init__(self):
        self.history: List[SalaryRecord] = []
        self.load_history()
    
    def calculate_tax(self, income: float) -> float:
        """Calculate tax based on progressive tax brackets"""
        tax = 0.0
        for bracket in self.TAX_BRACKETS:
            if income > bracket.min_income:
                taxable_amount = min(income, bracket.max_income) - bracket.min_income
                tax += taxable_amount * bracket.rate
        return tax
    
    def calculate_net_salary(self, base_salary: float, bonus: float = 0.0) -> tuple:
        """Calculate net salary after tax"""
        gross_salary = base_salary + bonus
        tax = self.calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        return gross_salary, tax, net_salary
    
    def add_record(self, base_salary: float, bonus: float = 0.0):
        """Add a new salary record to history"""
        gross, tax, net = self.calculate_net_salary(base_salary, bonus)
        record = SalaryRecord(
            date=datetime.now().strftime("%Y-%m-%d"),
            base_salary=base_salary,
            bonus=bonus,
            tax=tax,
            net_salary=net
        )
        self.history.append(record)
        self.save_history()
        return record
    
    def save_history(self):
        """Save calculation history to JSON file"""
        with open("salary_history.json", "w") as f:
            json.dump([{
                "date": r.date,
                "base_salary": r.base_salary,
                "bonus": r.bonus,
                "tax": r.tax,
                "net_salary": r.net_salary
            } for r in self.history], f, indent=2)
    
    def load_history(self):
        """Load calculation history from JSON file"""
        try:
            with open("salary_history.json", "r") as f:
                data = json.load(f)
                self.history = [
                    SalaryRecord(
                        date=r["date"],
                        base_salary=r["base_salary"],
                        bonus=r["bonus"],
                        tax=r["tax"],
                        net_salary=r["net_salary"]
                    ) for r in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    
    def generate_report(self, months: int = 12):
        """Generate salary report for specified period"""
        recent_records = [r for r in self.history if self.is_recent(r.date, months)]
        if not recent_records:
            print("\nNo records found for the specified period.")
            return
        
        print(f"\n📊 Salary Report (Last {months} months)")
        print("=" * 60)
        print(f"{'Date':<12} {'Base Salary':>12} {'Bonus':>12} {'Tax':>12} {'Net Salary':>12}")
        print("-" * 60)
        
        for record in recent_records:
            print(f"{record.date:<12} {record.base_salary:>12.2f} {record.bonus:>12.2f} "
                  f"{record.tax:>12.2f} {record.net_salary:>12.2f}")
        
        print("=" * 60)
        
        total_base = sum(r.base_salary for r in recent_records)
        total_bonus = sum(r.bonus for r in recent_records)
        total_tax = sum(r.tax for r in recent_records)
        total_net = sum(r.net_salary for r in recent_records)
        
        print(f"{'Totals:':<12} {total_base:>12.2f} {total_bonus:>12.2f} "
              f"{total_tax:>12.2f} {total_net:>12.2f}")
        print("=" * 60)
    
    def is_recent(self, date_str: str, months: int) -> bool:
        """Check if record is within specified number of months"""
        record_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        cutoff_date = datetime.now().date().replace(month=datetime.now().date().month - months)
        return record_date >= cutoff_date

def get_positive_float(prompt: str) -> float:
    """Get and validate positive float input"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    calculator = SalaryCalculator()
    
    while True:
        print("\n💰 Salary Calculator")
        print("1. Calculate Net Salary")
        print("2. View Salary History")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\n💵 Calculate Net Salary")
            base = get_positive_float("Enter base salary: ")
            bonus = get_positive_float("Enter bonus (or 0 if none): ")
            
            record = calculator.add_record(base, bonus)
            print("\n📝 Calculation Results:")
            print(f"Gross Salary: {record.base_salary + record.bonus:.2f}")
            print(f"Tax Deducted: {record.tax:.2f}")
            print(f"Net Salary: {record.net_salary:.2f}")
            
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n📅 Salary History")
            if not calculator.history:
                print("No history available.")
            else:
                for record in calculator.history[-5:]:  # Show last 5 records
                    print(f"{record.date}: Base={record.base_salary:.2f}, "
                          f"Bonus={record.bonus:.2f}, Tax={record.tax:.2f}, "
                          f"Net={record.net_salary:.2f}")
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            months = 12  # Default to 12 months
            try:
                months = int(input("\nEnter number of months for report (default 12): ") or 12)
            except ValueError:
                print("Using default 12 months.")
            
            calculator.generate_report(months)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            calculator.save_history()
            print("\n💾 Data saved. Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()