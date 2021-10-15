from random import randint

# For the players and computers board I created
# an empty list to hold the symbols which dictated
# what is happening on the board

NUM_SHIPS = 8

comp_board = []
player_board = []


def game_rules():

    """
    This function is triggered at the start of the game
    It prints out the rules to show players how the games works
    """

    print("Damn The Torpedo’s!!!")
    print("Game rules are as follows:")
    print("i) Destroy your enemies ships.")
    print("ii) Each row uses a coordinate system of (0,9) there are ten rows.")
    print("iii) Inputs must use numbers between(0,7) for both the row and "
          "the column. Beginning at (0, 0).")
    print("iv) Water is represented by ~. Misses are represented by X. "
          "Hits are represented by # and your ship is represented by S.")
    print("v) You ten attempts to destroy the enemy target.")
    print("vi) Enjoy yourself.")

# The following for loop creates an list of 8 rows
# It then populates this array with ~ which represents water


for x in range(8):
    comp_board.append(["~"] * 8)
    player_board.append(["~"] * 8)


def comp_board_app(c_board):
    """
    This function removes the [] from the list in comps board
    """
    for grid in c_board:
        print(" ".join(grid))


comp_board_app(comp_board)


def rand_row(c_board):
    """
    This function picks a random row
    """
    return round(randint(0, len(c_board) - 1))


rand_row(comp_board)


def rand_col(c_board):
    """
    This function picks a random column
    """
    return randint(0, len(c_board[0]) - 1)


def player_board_app(p_board):
    """
    This function removes the [] from the list in players board
    """
    for grids in p_board:
        print(" ".join(grids))


def main():
    """
    This is the main function of the game where all tasks are carried out
    """
    game_rules()

    comp_row = rand_row(comp_board)
    comp_col = rand_col(comp_board)
    player_destroyed = 0
    comp_destroyed = 0
    players_name = input("Please enter your name: \n")
    print(f"Welcome to War {players_name}.")
    player_ships = set()
    # this varible is number of successfull goes
    g_number = 0
    while len(player_ships) < NUM_SHIPS:
        player_row = input("Choose your ships row: \n")
        player_col = input("Choose your ships column: \n")

        # this checks if the row and column entered are digits
        if player_col.isdigit() and player_row.isdigit():
            player_col = int(player_col)
            player_row = int(player_row)
            # this checks to see if the user entered numbers
            # within the boards scope
            # if they have an S is placed on the board for a ships palce
            if (player_row < 0 or player_row > 7) \
                    or (player_col < 0 or player_col > 7):
                print("You\'re way off course solider!!!")
                print("Choose between 0 and 7")
            elif (player_row, player_col) in player_ships:
                print("Already a ship here")
            else:
                player_ships.add((player_row, player_col))
                player_board[player_row][player_col] = "S"
                # if a user enters the correct enteries
                # their number of goes is incremented
                g_number = g_number + 1
                print("Success - go completed: ", g_number)
        else:
            # if the user does not enter a
            # number this error message is displayed
            print("One of these is not a digit - Try again!!!"
                  " You are on go number: ", g_number)
    for attempt in range(10):
        print("Attempt", attempt + 1)
        player_guess_row = int(input("Guess the enemies row: \n"))
        player_guess_col = int(input("Guess the enemies column: \n"))
        print(f"Our target is ({player_guess_row},{player_guess_col}) FIRE!!!")

        comp_guess_row = round(randint(0, len(player_board)-1))
        comp_guess_col = round(randint(0, len(player_board)-1))

        if (player_guess_row < int(0) or player_guess_row > int(7)) or  \
                (player_guess_col < 0 or player_guess_col > 7):
            print("You\'re way off course solider!!!")
        elif player_board[player_guess_row][player_guess_col] == "#":
            print("Destroyed already solider!!")
        elif (player_guess_row == comp_row and player_guess_col == comp_col):
            print("Direct HIT!")
            player_board[player_guess_row][player_guess_col] = "#"
            comp_destroyed += 1
        else:
            if (player_guess_row < 0 or player_guess_row < 7) or\
                    (player_guess_col < 0 or player_guess_col < 7):
                print("You\'re way off course solider!!!")
            elif player_board[player_guess_row][player_guess_col] == "X":
                print("Destroyed already solider!!")
            else:
                print("Swing and a miss...")

        if comp_guess_row == player_row and comp_guess_col == player_col:
            player_board[comp_guess_row][comp_guess_col] = "#"
            print("The enemy has stuck your vessel")
            player_destroyed += 1
        else:
            player_board[comp_guess_row][comp_guess_col] = "X"
            print("Enemy: Swing and a miss...")

        print("The Enemies Board")
        comp_board_app(comp_board)
        print(f"\n{players_name}\'s board")
        player_board_app(player_board)

        if attempt == 9:
            print("Damn the lack of torpedoes... GAME OVER!")
            break
        else:
            print("Reloading torpedoes")
        if comp_destroyed == 1:
            print("The enemy has been obliterated")
            break

        if player_destroyed == 1:
            print("The enemy has won.... GAME OVER!")
            break

# This is the game function being called to play the game


player_board_app(player_board)
rand_col(comp_board)
comp_board_app(comp_board)
rand_col(comp_board)
rand_row(comp_board)

main()
