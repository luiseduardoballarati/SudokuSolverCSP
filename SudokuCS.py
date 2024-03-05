# check the rows
def checkRows(board, row, num):
    if num in board[row]:
        return False
    return True

# check the columns
def checkColumns(board, column, num):
    for row in range(len(board)):
        if num == board[row][column]:
            return False
    return True

# check the unit 3x3
def checkUnit(board, row, col, num):
   for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return False
   return True

# check if place that number is valid
def checkMove(board, row, col, num):
    if checkRows(board, row, num) and checkColumns(board, col, num) and checkUnit(board, row - row % 3, col - col % 3, num):
        return True
    else:
        return False

# Find the fist empty cell
def emptyCell(board):
    for r in range(0, len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return r,c
    return None

# Input the numbers on empty cells
def inputNumberOnEmptyCell(board, row, col):
    # Try numbers from 1 to 9
    for n in range(1, 10):
        if checkMove(board, row, col, n):
            # If the number is valid, assign it to the cell
            board[row][col] = n

            # Recursively call the function for the next empty cell
            next_cell = emptyCell(board)
            if next_cell is None:
                return True  # Base case: board filled successfully
            else:
                next_row, next_col = next_cell
                if inputNumberOnEmptyCell(board, next_row, next_col):
                    return True  # If a solution is found, return True

            # If the next cell couldn't be filled with a valid number, backtrack
            board[row][col] = 0

    return False  # If no valid number can be assigned, return False

# Solve the Sudoku boards or output that it does not have a solution
def solver(board):
    cells = emptyCell(board)

    if cells is None:
        return True  # Base case: board filled successfully

    else:
        r, c = cells
        if inputNumberOnEmptyCell(board, r, c):
            return True  # If a solution is found, return True
        else:
            return False  # If no solution is found, return False

# Test the solver
if solver(board):
    print("Sudoku solved successfully:")
    for row in board:
        print(row)
else:
    print("No solution exists for this Sudoku.")
