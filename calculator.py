# Simple calculator program in Python

while True:
    try:
        fnumber = int(input("First number: "))
        snumber = int(input("Second number: "))
        arithmetic_operation = input("The arithmetic operation (+ - * /): ")

        if arithmetic_operation == "+":
            result = fnumber + snumber
        elif arithmetic_operation == "-":
            result = fnumber - snumber
        elif arithmetic_operation == "*":
            result = fnumber * snumber
        elif arithmetic_operation == "/":
            if snumber == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = fnumber / snumber
        else:
            print("Error: Invalid operation.")
            continue # continue to the next iteration

        print("Result:", result)
        break # exit the loop after successful calculation

    except ValueError:
        print("Error: Please enter valid numbers.")