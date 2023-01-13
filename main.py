# DICE ROLL SIMULATOR ASSIGNMENT

# Import Random
import random

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
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        diceSum = int(dice1) + int(dice2)
        print(str(dice1) + "," + str(dice2) + " (sum: " + str(diceSum) + ")")
    elif selection == "2":
        print("Roll Dice 5 Times")
        n = 1
        while n <= 5:
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            diceSum = int(dice1) + int(dice2)
            print(str(dice1) + "," + str(dice2) + " (sum: " + str(diceSum) + ")")
            n += 1
    elif selection == "3":
        print("Roll Dice 'n' Times")
        n = int(input("How many rolls would you like? "))
        for n in range(n):
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            diceSum = int(dice1) + int(dice2)
            print(str(dice1) + "," + str(dice2) + " (sum: " + str(diceSum) + ")")
    elif selection == "4":
        print("Roll Dice until Snake Eyes")
        tries = 0
        snakeEyes = False
        while snakeEyes == False:
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            diceSum = int(dice1) + int(dice2)
            print(str(dice1) + "," + str(dice2) + " (sum: " + str(diceSum) + ")")
            tries += 1
            if dice1 == 1 and dice2 == 1:
                snakeEyes = True
                print("SNAKE EYES! It took " + str(tries) + " rolls to get snake eyes.")
    else:
        print("EXIT")
        print("BYE!")
        loop = False
