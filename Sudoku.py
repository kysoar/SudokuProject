# This is a Sudoku puzzle solver that takes a starter board and solves it
# v1.0 text-based solution with 1 default board

# default board
# each array has 9 digits 0-9. Numbers cannot repeat within array or within same row or column across the board
# each array in board represents a 3x3 Sudoku segment
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# takes the input Sudoku board and prints it in a default text-based layout
def print_board(b):

    for i in range(len(b)):

        # prints horizontal dividers every 3rd row to show distinction between arrays
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        # iterates through 0-8 to populate board
        for j in range(len(b[0])):

            # print vertical dividers every 3rd column to show distinction between arrays
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j != 8:
                print(str(b[i][j]) + " ", end="")
            else:
                print(b[i][j])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starter board:")
    print_board(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
