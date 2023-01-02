#!/usr/bin/python3

N = 8 # size of the chessboard

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(row, col):
# check if there is a queen in the same column
for i in range(row):
if board[i][col] == 1:
return False

# check if there is a queen in the top-left diagonal
i, j = row, col
while i >= 0 and j >= 0:
    if board[i][j] == 1:
        return False
    i -= 1
    j -= 1

# check if there is a queen in the top-right diagonal
i, j = row, col
while i >= 0 and j < N:
    if board[i][j] == 1:
        return False
    i -= 1
    j += 1

return True

def solve(row):
# base case: if all queens are placed, return True
if row == N:
return True

# try to place a queen in each column of the current row
for col in range(N):
    if is_safe(row, col):
        # place the queen and move on to the next row
        board[row][col] = 1
        if solve(row+1):
            return True

        # backtrack: remove the queen and try a different column
        board[row][col] = 0

return False

if solve(0):
for row in board:
print(row)
else:
print("Solution not found")
