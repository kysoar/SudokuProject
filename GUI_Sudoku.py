import pygame
from solver import solve, valid
import time
pygame.font.init()


class Grid:
    # default board
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


    # __init__
    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        # initializes all cubes for each i, j index in rows, columns
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)]
        self.model = None
        self.selected = None

    # update
    def update(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range (self.rows)]

    # place
    def place(self, val):
        # row = row of selected cell
        # col = column of selected cell
        row, col = self.selected

        # if selected cell = 0 (blank), set cell to val
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update()
                return False


    # sketch
    def sketch(selfself, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)
        

    # draw
    # draws the grid outline
    # gap = width of grid / number of columns (9)
    # thickness = thickness of grid line
    # win = surface to draw on
    def draw(self, win):
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4 # bold line to separate blocks of 9 cubes
            else:
                thickness = 1 # thin lines for all other lines in grid

            # draw column lines
            # line(surface, color, start_pos, end_pos, width)
            # (0, 0, 0) =
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thickness)
            #draw row lines
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)

    # select
    def select(self, row, col):
        # deselect all cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        # select row, col cell
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    # clear
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    # click


    # is_finished
    # iterates through all cells in cubes and returns false if the value is 0
    # if there are no 0 values, return true, meaning the puzzle is finished
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

class Cube:

    rows = 9
    columns = 9

    # __init__
    # value = numeric value in cell
    # row, column = position of cell
    # width, height = dimensions of cell
    # selected = boolean whether cell is clicked by user
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width
        self. height = height
        self.selected = False # cell is not selected when initialized

    # draw

# redraw_window

# format_time

def main()

#main()
#pygame.quit
