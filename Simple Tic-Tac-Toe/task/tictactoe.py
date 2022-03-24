state = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
end = False
move = False
turn = 1


def print_board():
    print("---------")
    print("| " + state[0] + " " + state[1] + " " + state[2] + " |")
    print("| " + state[3] + " " + state[4] + " " + state[5] + " |")
    print("| " + state[6] + " " + state[7] + " " + state[8] + " |")
    print("---------")


def check_input(pos):
    global move, turn
    pos_x, pos_y = 0, 0
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    if pos[0] not in numbers or pos[1] not in numbers:
        print("You should enter numbers!")
    else:
        pos_x = int(pos[0])
        pos_y = int(pos[1])

    if pos_x > 3 or pos_x <= 0:
        print("Coordinates should be from 1 or 3!")
    elif pos_y > 3 or pos_y <= 0:
        print("Coordinates should be from 1 or 3!")

    if pos_x == 1:
        if pos_y == 1:
            if state[0] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[0] = "X"
                else:
                    state[0] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 2:
            if state[1] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[1] = "X"
                else:
                    state[1] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 3:
            if state[2] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[2] = "X"
                else:
                    state[2] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
    elif pos_x == 2:
        if pos_y == 1:
            if state[3] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[3] = "X"
                else:
                    state[3] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 2:
            if state[4] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[4] = "X"
                else:
                    state[4] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 3:
            if state[5] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[5] = "X"
                else:
                    state[5] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
    elif pos_x == 3:
        if pos_y == 1:
            if state[6] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[6] = "X"
                else:
                    state[6] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 2:
            if state[7] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[7] = "X"
                else:
                    state[7] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")
        elif pos_y == 3:
            if state[8] not in ["X", "O"]:
                if turn % 2 != 0:
                    state[8] = "X"
                else:
                    state[8] = "O"
                move = True
            else:
                print("This cell is occupied! Choose another one!")


def check_game():
    global state, end
    amount_x = 0
    amount_zero = 0

    for c in state:
        if c == "X":
            amount_x += 1
        elif c == "O":
            amount_zero += 1
    if abs(amount_zero - amount_x) > 1:
        print("Impossible")
    else:
        if state[0] == state[1] == state[2] != " ":
            print(state[0] + " wins")
            end = True
        elif state[3] == state[4] == state[5] != " ":
            print(state[3] + " wins")
            end = True
        elif state[6] == state[7] == state[8] != " ":
            print(state[6] + " wins")
            end = True
        elif state[0] == state[4] == state[8] != " ":
            print(state[0] + " wins")
            end = True
        elif state[2] == state[4] == state[6] != " ":
            print(state[2] + " wins")
            end = True
        elif state[0] == state[3] == state[6] != " ":
            print(state[0] + " wins")
            end = True
        elif state[1] == state[4] == state[7] != " ":
            print(state[1] + " wins")
            end = True
        elif state[2] == state[5] == state[8] != " ":
            print(state[2] + " wins")
            end = True
        elif amount_x + amount_zero == 9:
            print("Draw")


print_board()
while end is not True:
    move = False
    while move is not True:
        check_input(input("Enter the coordinates: ").split())
    print_board()
    check_game()
    turn += 1
    if turn == 10:
        break
