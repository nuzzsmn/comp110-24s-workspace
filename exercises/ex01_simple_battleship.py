"""One Shot Battleship"""
 
__author__ = "730477602"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

user_1_choice: int = int((input("Pick a secret boat location between 1 and 4: ")))

if user_1_choice < 1:
    print("Error! " + str(user_1_choice) + " too low!")
    exit()
if user_1_choice > 4:
    print("Error! " + str(user_1_choice) + " too high!")
    exit()

user_2_choice: int = int((input("Guess a number between 1 and 4: ")))

if user_2_choice < 1:
    print("Error! " + str(user_2_choice) + " too low!")
    exit()
if user_2_choice > 4:
    print("Error! " + str(user_2_choice) + " too high!")
    exit()

result: str = ""
concatination: str = ""

if user_1_choice == user_2_choice:
    result = RED_BOX
else:
    result = WHITE_BOX
if user_1_choice == user_2_choice:
    if user_2_choice == 1:
        concatination = result + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(concatination)
    if user_2_choice == 2:
        concatination = BLUE_BOX + result + BLUE_BOX + BLUE_BOX
        print(concatination)
    if user_2_choice == 3:
        concatination = BLUE_BOX + BLUE_BOX + result + BLUE_BOX
        print(concatination)
    if user_2_choice == 4:
        concatination = BLUE_BOX + BLUE_BOX + BLUE_BOX + result
        print(concatination)
    print("Correct! You hit the ship.")
else:
    if user_2_choice == 1:
        concatination = result + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(concatination)
    if user_2_choice == 2:
        concatination = BLUE_BOX + result + BLUE_BOX + BLUE_BOX
        print(concatination)   
    if user_2_choice == 3:
        concatination = BLUE_BOX + BLUE_BOX + result + BLUE_BOX
        print(concatination)
    if user_2_choice == 4:
        concatination = BLUE_BOX + BLUE_BOX + BLUE_BOX + result
        print(concatination)
    print("Incorrect! You missed the ship.")
