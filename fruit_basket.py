# Fruit basket 

def get_positive_number(prompt):
    """Get a positive number from user"""
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("❗ Number must be greater than zero!")
                continue
            return num
        except ValueError:
            print("❗ Invalid number. Please enter a whole number!")

def get_non_empty_string(prompt):
    """Get non-empty string from user"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❗ Field cannot be empty!")

def get_positive_float(prompt):
    """Get positive float from user"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❗ Value cannot be negative!")
                continue
            return value
        except ValueError:
            print("❗ Invalid value. Please enter a number!")

def display_items(items, prices):
    """Display items and prices"""
    print("\n🛒 Your Fruit Basket:")
    for i, (item, price) in enumerate(zip(items, prices), 1):
        print(f"{i}. {item}: 💲{price:.2f}")

def calculate_total(prices):
    """Calculate total price"""
    total = sum(prices)
    print(f"\n💰 Total Price: 💲{total:.2f}")
    return total

def check_affordability(total):
    """Check if user can afford the items"""
    money = get_positive_float("\nHow much money do you have? 💲 ")
    
    if money > total:
        print(f"🎉 You can buy all items! You'll have 💲{money - total:.2f} left.")
    elif money < total:
        print(f"⚠ You can't buy all items. You need 💲{total - money:.2f} more.")
    else:
        print("✨ You have the exact amount needed!")

def main():
    print("\n🌟 Fruit Basket Manager 🌟")
    
    # Get number of items
    num_items = get_positive_number("How many items do you have? ")
    
    items = []
    prices = []
    
    print("\nLet's enter your items:")
    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        item = get_non_empty_string("What is the item name? ")
        price = get_positive_float("What is the price? 💲 ")
        
        items.append(item)
        prices.append(price)
    
    # Display items
    if input("\nDo you want to see your items? (yes/no) ").strip().lower() in ["yes", "y"]:
        display_items(items, prices)
        
        # Display total price
        if input("\nDo you want to see the total price? (yes/no) ").strip().lower() in ["yes", "y"]:
            total = calculate_total(prices)
            check_affordability(total)
        else:
            print("\nOkay, won't show prices.")
    else:
        print("\nOkay, won't show items.")
    
    print("\nThank you for using the Fruit Basket Manager! 🍎🍌🍊")

if __name__== "__main__":
    main()