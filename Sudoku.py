# This is a Sudoku puzzle solver that takes a starter board and solves it
# v1.0 text-based default starter board
# v2.0 implement next_empty function which finds next empty cell. Add solve method

# default board
# each array has 9 digits 0-9. Numbers cannot repeat within array or within same row or column across the board
# each array in board represents a 3x3 Sudoku segment
# blank squares represented by 0
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# takes the input Sudoku board and prints it in a default text-based layout
def print_board(b):
    # iterates through each array i in board b for printing
    for i in range(len(b)):

        # prints horizontal dividers every 3rd row to show distinction between arrays
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        # iterates through 0-8 to populate board
        for j in range(len(b[0])):

            # print vertical dividers every 3rd column to show distinction between arrays
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            # prints the elements of board arrays
            if j != 8:
                print(str(b[i][j]) + " ", end="")
            else:
                print(b[i][j])  # prints and goes to new line


# next_empty searches the input board b and returns the row, col of first blank square
def next_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:  # return row, col of first blank square indicated by 0.
                return i, j

    # if no blank squares, return None
    return None


# solve function finds the next empty cell if it exists, and calls check function to test numbers 1-9
# solve function will proceed with first digit that does not break a rule and then proceed to next empty cell
# if suggested number turns out to be incorrect, set cell back to 0 (empty) and try more numbers
def solve(b):
    # find_next represents the row, col of the next empty cell. If next_empty returns None, solve returns True.
    # otherwise, set row, col to find_next and continue with solver
    find_next = next_empty(b)
    if not find_next:  # no empty cells, therefore puzzle is solved
        return True
    else:
        row, col = find_next

    # for loop checks each number 1-9 in the empty cell and runs check function to test validity
    # if check returns True, set empty cell (row, col) to index i
    # if check returns False, iterate to next number and test again
    for i in range(1, 10):
        if check(b, i, (row, col)):
            b[row][col] = i

            # call solve function recursively. Return True if puzzle is solved
            # if solve returns False, set cell back to 0, and iterate to next digit 1-9
            if solve(b):
                return True

            b[row][col] = 0

    return False


# check validates the accuracy of the board b, single-digit number num, and row, col position pos
# b: board
# num: single-digit number 1-9 that function is testing for validity
# pos: (row, col) index where num is cell is being tested
#
# rules: num can only be present once in each row and once in each column, respectively
#        num can only be present once in each 3 x 3 box
#
# returns False if num does breaks any rules in given pos
# returns True otherwise
#
# returns False by default in v2.0
def check(b, num, pos):
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starter board:")
    print_board(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
