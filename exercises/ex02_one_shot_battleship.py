"""One Shot Battleship"""
 
__author__ = "730477602"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_choice: int = int(input("Guess a row: "))

while row_choice < 1 or row_choice > grid_size:
    row_choice = int(input("The grid is only 4 by 4. Try again: "))

column_choice: int = int(input("Guess a column: "))

while column_choice < 1 or column_choice > grid_size:
    column_choice = int(input("The grid is only 4 by 4. Try again: "))  

result: str = ""

if row_choice == secret_row and column_choice == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

row_counter: int = 1

while row_counter <= grid_size:
    row_string: str = ""
    column_counter = 1
    if row_choice == row_counter:
        while column_counter <= grid_size:
            if column_choice == column_counter:
                row_string += result
            else:
                row_string += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            row_string += BLUE_BOX
            column_counter += 1
    print(row_string)
    row_counter += 1

if row_choice == 3 and column_choice == 2:
    print("Hit!")
elif row_choice == secret_row:
    print("Close! Correct row, wrong column.")
elif column_choice == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")



