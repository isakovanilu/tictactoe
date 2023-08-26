
def update_matrix3x3(matrix3x3, row, column, value):
    row_len = len(matrix3x3) # row length
    col_len = len(matrix3x3[0]) # column lenght
    if (row >= row_len or column >= col_len) or matrix3x3[row][column] != ' ': # if the coordinates greater than matrix size return the function
        print('Please enter different coordinates')
    else:
        for i in range(row_len): # loop throught rows
            for j in range(col_len): # loop throught columns
                if i == row and j == column: # if row and columns values match for the given coordinates
                    matrix3x3[i][j] = value # assign the new values for those coordinates

    for row in matrix3x3:
        print(" | ".join(row))
        print("-" * 9)
    return matrix3x3

## check the winner
def winner_check(matrix3x3, value):
    for x in range(3):
        if (matrix3x3[x][0] == matrix3x3[x][1] == matrix3x3[x][2] == value) or (matrix3x3[0][x] == matrix3x3[1][x] == matrix3x3[2][x] == value):
            return True
    for y in range(3):
        if (matrix3x3[y][0] == matrix3x3[y][1] == matrix3x3[y][2] == value) or (matrix3x3[0][y] == matrix3x3[1][y] == matrix3x3[2][y] == value):
            return True
    for x in range(0, 3, 2):
        if matrix3x3[x][0] == matrix3x3[1][1] == matrix3x3[2-x][2]:
            return True
    return False

def play():
    value = "X"
    # create a 3x3 matrix
    matrix3x3 = [[' ' for i in range(3)] for j in range(3)] # it will create an empty 3x3 list range(3):0,1,2

    while True:
        row = int(input(f"Player {value}, enter row (0, 1, 2): "))
        column = int(input(f"Player {value}, enter column (0, 1, 2): "))
        update_matrix3x3(matrix3x3, row=row, column=column, value=value)
        if winner_check(matrix3x3, value):
            print(f"Player {value} is winner")
            break

        value = "O" if value == "X" else "X"

play()