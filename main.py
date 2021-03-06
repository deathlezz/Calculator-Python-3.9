# Simple calculator
# Python 3.9.1
# Created by deathlezz
# Date 24.01.2021



# Say hi
print(" ")
print("* Welcome to calculator *")
print(" ")
print("Select operation:")
print("[1] Add / [2] Subtract / [3] Multiply / [4] Divide")
print(" ")

while True:

    # Create operation choice
    choice = input("Enter your choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

        try:
            num1 = round(float(input("Enter first number: ")), 2)

        except ValueError:
            print('# Enter numbers only')
            print('')
            continue

        try:
            num2 = round(float(input("Enter second number: ")), 2)

        except ValueError:
            print('# Enter numbers only')
            print('')
            continue

        if choice == '1':
            print("Solution:", num1, "+", num2, "=", round((num1 + num2), 2))
            print('')

        elif choice == '2':
            print("Solution:", num1, "-", num2, "=", round((num1 - num2), 2))
            print('')

        elif choice == '3':
            print("Solution:", num1, "x", num2, "=", round((num1 * num2), 2))
            print('')

        elif choice == '4':
            print("Solution:", num1, ":", num2, "=", round((num1 / num2), 2))
            print('')

        # There can be 'break' if you want to stop a loop

    else:
        print("# Enter number from 1 to 4")
        print('')