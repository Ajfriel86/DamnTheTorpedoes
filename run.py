from random import randint


"""
For the players and computers board I created
an empty array to hold the siymbols which dictated
what is happening on the board
"""

comp_board = []
player_board = []

"""
The following function is triggered at the start of the game
It prints out the rules to show players how the games works
"""


def game_begin():
    print("Damn The Torpedos!!!")
    print("Game rules are as follows:")
    print("i) Destroy your opponets ships.")
    print("ii) Each row uses a coordinate system of (0,9) there are ten rows.")
    print("iii) Inputs must use numbers between(0,7) for both the row and "
          "the column. Begining at (0, 0).")
    print("iv) Water is represented by ~. Misses are represented by X. "
          "Hits are represented by # and your ship is represented by S.")
    print("v) You ten attempts to destroy the enemy target.")
    print("vi) Enjoy yourself.")


game_begin()

"""
The following for loop creates an arrary of 8 rows
It then populates this array with ~ which represents water
"""

for x in range(8):
    comp_board.append(["~"] * 8)

"""
The following fuction removes the [] from the for loop array above
"""


def comp_board_app(comp_board):
    for grid in comp_board:
        print(" ".join(grid))


"""
The following two fuctions pick a random loction within the (0,7) range
for both rows and columns
"""


def rand_row(comp_board):
    return round(randint(0, len(comp_board) - 1))


def rand_col(comp_board):
    return randint(0, len(comp_board[0]) - 1)


"""
The varibales below are the varibles used to store the computers ship
"""

comp_row = rand_row(comp_board)
comp_col = rand_col(comp_board)


"""
The following for loop creates the players board
the same way the computers board was created
"""

for y in range(8):
    player_board.append(["~"] * 8)

"""
This function removes the [] from the players board
"""


def player_board_app(player_board):
    for grids in player_board:
        print(" ".join(grids))


"""
The following function 'game' is the main controls for this game
all game tasks are carried out in this funtion
"""


def game(comp_board, comp_col, comp_row, comp_board_app, player_board):

    """
    These varibles stores the number of ships
    on the players and computerts board
    """
    player_destroyed = 0
    comp_destroyed = 0

    """
    This varible asks for the users name, stores it
    and then reads it back to them with a welcome mnessagw
    """
    players_name = input("Please enter your name: \n")
    print(f"Welcome to War {players_name}.")
    """
    Varibles that store the players ship row and coloum
    """
    player_ships = set()
    
    while len(player_ships) < 3:
        print("$$$$$$$$")
        print(player_ships)
        player_row = int(input("Choose your ships row: \n"))
        player_col = int(input("Choose your ships column: \n"))
        """
        If statement to see that the players selects the correct
        coordinates within the board to place their ship
        """
        if (player_row < 0 or player_row > 7) \
                or (player_col < 0 or player_col > 7):
            print("You\'re way off course solider!!!")
            print("Choose between 0 and 7")
        elif (player_row, player_col) in player_ships: 
            print("Already a ship here")
        else:
            player_ships.add((player_row, player_col))
            player_board[player_row][player_col] = "S"
    """
    for loop that gives the player 10 attempts at guessing
    the computers ship coordinates
    """
    for attempt in range(10):
        print("attempt", attempt + 1)
        player_guess_row = int(input("Guess your opponents row: \n"))
        player_guess_col = int(input("Guess your opponents column: \n"))
        print(f"Our target is ({player_guess_row},{player_guess_col}) FIRE!!!")
        """
        Below are the varibles which the comuters uses to guess the players
        coordinates of thier ship
        """
        comp_guess_row = round(randint(0, len(player_board)-1))
        comp_guess_col = round(randint(0, len(player_board)-1))

        """
        The if statement below checks the coordinates that were given
        to see if the choice hits, misses, or if its been previously hit
        It then goes on to check and remove 1 from either the players
        or computers board if the ship was hit

        """
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

        """
        Here the varbiles are used to update both boards
        for the player and computer
        """

        print("The Enemies Board")
        comp_board_app(comp_board)
        print(f"{players_name} board")
        player_board_app(player_board)

        """
        Here the if statement checks the number of attempts
        9 here represents 10, as te game starts at 0.
        if attempts = 10, game is over.
        if a computers ship is destyroyed print messgae.
        if players ship is destroyed print message.
        """

        if attempt == 9:
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


"""
This is the game function being called to play the game
"""
game(comp_board, comp_col, comp_row, comp_board_app, player_board)
