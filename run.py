from random import randint

comp_board = []
player_board = []


def game_begin():
    print("Damn The Torpedos!!!")
    print("Game rules are as follows:")
    print("i) Destroy your opponets ships.")
    print("ii) Each row uses a coordinate system of (0,9) there are ten rows.")
    print("iii) Inputs must use numbers between(0,7) for both the row and\
        the column. Begining at (0, 0).")
    print("iv) Water is represented by ~. Misses are \nrepresented by X.\
        Hits are represented by # and your ship is represented by S")
    print("v) You ten attempts to destroy the enemy target.")
    print("vi) Enjoy yourself.")


game_begin()

for x in range(8):
    comp_board.append(["~"] * 8)


def comp_board_app(comp_board):
    for grid in comp_board:
        print(" ".join(grid))


def rand_row(comp_board):
    return round(randint(0, len(comp_board) - 1))


def rand_col(comp_board):
    return randint(0, len(comp_board[0]) - 1)


rand_col(comp_board)
rand_row(comp_board)

comp_row = rand_row(comp_board)
comp_col = rand_col(comp_board)


"""
Comments
"""

for y in range(8):
    player_board.append(["~"] * 8)


def player_board_app(player_board):
    for grids in player_board:
        print(" ".join(grids))


"""
Comments
"""


def game(comp_board, comp_col, comp_row, comp_board_app, player_board):

    player_destroyed = 0
    comp_destroyed = 0

    players_name = input("Please enter your name: \n")
    print(f"Welcome to War {players_name}.")

    player_row = int(input("Choose your ships row: \n"))
    player_col = int(input("Choose your ships column: \n"))
    if (player_row < int(0) or player_row > int(7)) \
            or (player_col < int(0) or player_col > int(7)):
        print("You\'re way off course solider!!!")
        print("Choose between 0 and 7")
        player_row = int(input("Choose your ships row: \n"))
        player_col = int(input("Choose your ships column: \n"))
    else:
        player_board[player_row][player_col] = "S"

    for attempt in range(10):
        print("attempt", attempt + 1)
        player_guess_row = int(input("Guess your opponents row: \n"))
        player_guess_col = int(input("Guess your opponents column: \n"))
        print(f"Our target is ({player_guess_row},{player_guess_col}) FIRE!!!")

        comp_guess_row = round(randint(0, len(player_board)-1))
        comp_guess_col = round(randint(0, len(player_board)-1))

        if (player_guess_row < int(0) or player_guess_row > int(7)) or  \
                (player_guess_col < 0 or player_guess_col > 7):
            print("You\'re way off course solider!!!")
        elif (player_board[player_guess_row][player_guess_col] == "#"):
            print("Destroyed already solider!!")
        elif player_guess_row == comp_row and player_guess_col == comp_col:
            print("Direct HIT!")
            player_board[player_guess_row][player_guess_col] = "#"
            comp_destroyed += 1
        else:
            if (player_guess_row < 0 or player_guess_row < 7) or\
                    (player_guess_col < 0 or player_guess_col < 7):
                print("You\'re way off course solider!!!")
            elif (player_board[player_guess_row][player_guess_col] == "X"):
                print("Destroyed already solider!!")
            else:
                print("Swing and a miss...")

        if comp_guess_row == player_row and comp_guess_col == player_col:
            player_board[comp_guess_row][comp_guess_col] = "#"
            print("The enemy has stuck your vessal")
            player_destroyed += 1
        else:
            player_board[comp_guess_row][comp_guess_col] = "X"
            print("Enemy: Swing and a miss...")

        print("Oponants Board")
        comp_board_app(comp_board)
        print(f"{players_name} board")
        player_board_app(player_board)

        if attempt == 29:
            print("Damn the lack of torpedos... GAME OVER!")
            break
        else:
            print("Reloading torpedos")
        if comp_destroyed == 1:
            print("The enemy has been oblitarated")
            break

        if player_destroyed == 1:
            print("The enemy has won.... GAME OVER!")
            break


game(comp_board, comp_col, comp_row, comp_board_app, player_board)