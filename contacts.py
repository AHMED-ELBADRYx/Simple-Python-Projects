# Contacts

contacts = {}

while True:
    print("\n📞 Contact Manager")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Update a contact")
    print("4. Search a contact")
    print("5. Show all contacts")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        number = input("Enter number: ").strip()
        if name and number:
            contacts[name] = number
            print(f"✅ Added {name}.")
        else:
            print("❌ Name and number cannot be empty.")

    elif choice == "2":
        name = input("Enter name: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"✅ {name} was deleted.")
        else:
            print("❌ Contact not found.")

    elif choice == "3":
        name = input("Enter name: ").strip()
        if name in contacts:
            number = input("Enter new number: ").strip()
            contacts[name] = number
            print(f"✅ Updated {name}.")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        name = input("Enter name: ").strip()
        if name in contacts:
            print(f"Name: {name}")
            print(f"Number: {contacts[name]}")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        if contacts:
            print("\n📜 All Contacts:")
            for name, number in contacts.items():
                print(f"- {name}: {number}")
        else:
            print("📭 No contacts yet.")

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select from 1-6.")