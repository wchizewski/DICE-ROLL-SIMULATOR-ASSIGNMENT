# DICE ROLL SIMULATOR ASSIGNMENT

# Main Program Loop
loop = True
while loop:
    # Print menu
    print("MAIN MENU")
    print("1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice 'n' Times")
    print("4: Roll Dice until Snake Eyes")
    print("5: Exit")

    # Get selection from user
    selection = input("Enter Selection (1-5): ")

    # Perform Selection
    if selection == "1":
        print("Roll Dice Once")
    elif selection == "2":
        print("Roll Dice 5 Times")
    elif selection == "3":
        print("Roll Dice 'n' Times")
    elif selection == "4":
        print("Roll Dice until Snake Eyes")
    else:
        print("EXIT")
        loop = False
