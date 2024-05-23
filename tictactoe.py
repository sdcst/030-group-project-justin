def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def win(board1, board2, board3):
    # vertical
    for h in range(3):
        if board1[h] == board2[h] == board3[h] and board1[h] == "x":
            return "x"
        elif board1[h] == board2[h] == board3[h] and board1[h] == "o":
            return "o"
    # horizontal
    if board1[0] == board1[1] == board1[2] and board1[0] == "x":
        return "x"
    elif board1[0] == board1[1] == board1[2] and board1[0] == "o":
        return "o"
    elif board2[0] == board2[1] == board2[2] and board2[0] == "x":
        return "x"
    elif board2[0] == board2[1] == board2[2] and board2[0] == "o":
        return "o"
    elif board3[0] == board3[1] == board3[2] and board3[0] == "x":
        return "x"
    elif board3[0] == board3[1] == board3[2] and board3[0] == "o":
        return "o"
    # diagonal
    if board1[0] == board2[1] == board3[2] and board1 == "x":
        return "x"
    elif board1[0] == board2[1] == board3[2] and board1 == "o":
        return "o"
    elif board1[2] == board2[1] == board3[0] and board1[2] == "x":
        return "x"
    elif board1[2] == board2[1] == board3[0] and board1[2] == "o":
        return "o"
    else:
        return None


def games():
    print("Welcome to TicTacToe!!!\nI hope you know how to play the game:)")
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    counter = 1
    name1 = input("Enter first name: ")
    if name1.lower() == "exit":
        return None
    name2 = input("Enter second name: ")
    if name2.lower() == "exit":
        return None
    name = name1
    while win(row1, row2, row3) != "x" and win(row1, row2, row3) != "o":
        if counter % 2 == 1:
            name = name1
        elif counter % 2 == 0:
            name = name2
        print(name + "'s turn")
        print("Current Board: ")
        for i in range(3):
            for j in range(3):
                if i == 0:
                    print("|", row1[j], end="|")
                elif i == 1:
                    print("|", row2[j], end="|")
                elif i == 2:
                    print("|", row3[j], end="|")
            print()
            print("--------")
        row, column = "a", "b"
        #  and not check(row, column, row1, row2, row3)
        while not isint(row) or not isint(column):
            row = input("Enter row: ")
            if row.lower() == "exit":
                return None
            elif not isint(row):
                print("Invalid Input")
                continue
            elif int(row) > 3 or int(row) < 1:
                print("Invalid Input")
                continue
            column = input("Enter column: ")
            if column.lower() == "exit":
                return None
            elif not isint(column):
                print("Invalid Input")
                continue
            elif int(column) > 3 or int(column) < 1:
                print("Invalid Input")
                continue
            row = int(row)
            if row > 3 or row < 1:
                print("Invalid Input")
                continue
        row = int(row) - 1
        column = int(column) - 1
        """

        """
        if row == 0:
            if counter % 2 == 0:
                row1[column] = "x"
            else:
                row1[column] = "o"
        elif row == 1:
            if counter % 2 == 0:
                row2[column] = "x"
            else:
                row2[column] = "o"
        elif row == 2:
            if counter % 2 == 0:
                row3[column] = "x"
            else:
                row3[column] = "o"
        counter += 1
    if win(row1, row2, row3) == "x":
        print(name1 + " won!")
    elif win(row1, row2, row3) == "o":
        print(name2 + " won!")