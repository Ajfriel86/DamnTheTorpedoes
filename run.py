""" 
Python code for Battle Ship Game Called - Damn Those Torpedos!!!
"""
from random import randint

comp_board = []
player_board = []


def game_begin():
    print("Damn The Torpedos!!!")
    print("Game rules are as follows:")
    print("i) Destroy your opponets ships.")
    print("ii) Each row uses a coordinate system of (0,9) there are ten rows.")
    print("iii) Inputs must use numbers between(0,7) for both the row andn the column. \
        Begining at (0, 0).")
    print("iv) Enjoy yourself.")


game_begin()


"""
Comments
"""
for x in range(8):
    comp_board.append(["~"] * 8)


def comp_board_app(comp_board):
    for grid in comp_board:
        print(" ".join(grid))

    """
    Comments
    """


def rand_row(comp_board):
    return round(randint(0, len(comp_board) - 1))


def rand_col(comp_board):
    return randint(0, len(comp_board[0]) - 1)


rand_col(comp_board)


rand_row(comp_board)


"""
Comments
"""

comp_row = rand_row(comp_board)
comp_col = rand_col(comp_board)


"""
Comments
"""

for y in range(8):
    player_board.append(["~"] * 8)


def player_board_app(player_board):
    for grids in player:
        print(" ".join(grids))


"""
Comments
"""


def game(comp_board, comp_col, comp_row, comp_board_app, player_board):

    player_destroyed = 0
    comp_destroyed = 0

    players_name = input("Please enter your name: ")
    print(f"Welcome to War {players_name}.")

    player_row = int(input("Choose your ships row: ")
    player_col = int(input("Choose your ships column: "))
    if (player_row < 0 or player_row > 7) or (player_col < 0 or player_col > 7):
        print("You're way off course solider!!!")
        print("Choose between 0 and 7")
        player_row = int(input("Choose your ships row: ")
        player_col = int(input("Choose your ships column: "))
    else:
        player_board[player_row][player_col] = "#"


for attempt in range(30):
    print("attempt", attempt +1)

    guess_row = int(input("Guess your opponents row: "))
    guess_col = int(input("Guess your opponents column: "))
    print(f"Our target is ({guess_row},{guess_col}) FIRE!!!")

    
