print("1. Add \n"
      "2. Subtract \n"
      "3. Divide \n"
      "4. Multiply")

operation = int(input("Enter an operation : "))

a = int(input("Enter a number : "))
b = int(input("Enter a second number : "))


if operation == 1:
    print(a + b)

elif operation == 2:
    print(a - b)

elif operation == 3:
    print(a / b)

elif operation == 4:
    print(a * b)

else:
    print("Invalid Input.")
