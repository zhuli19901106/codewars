from math import sqrt

# https://www.codewars.com/kata/hard-sudoku-solver/train/python
'''
This kata is a harder version of http://www.codewars.com/kata/sudoku-solver/python made by @pineappleclock

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "insane" and can have multiple solutions. It will probably require some sort of brute force.

Consider applying algorithm with

Hidden Candidates http://www.sudokuwiki.org/Hidden_Candidates
Naked-pairs/triples/quads http://www.sudokuwiki.org/Naked_Candidates
Intersection removal http://www.sudokuwiki.org/Intersection_Removal
Brute Force
For Sudoku rules, see the Wikipedia : http://www.wikiwand.com/en/Sudoku

Used puzzle from : http://www.extremesudoku.info/sudoku.html

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve(puzzle)
'''

def generate_matrix(n, m, val):
    return [[val for j in xrange(m)] for i in xrange(n)]

n = 0
row_record = 0
col_record = 0
block_record = 0
suc = False
nr = 0
pos = 0

def dfs(board):
    global n, nr, row_record, col_record, block_record, suc, pos

    if suc:
        return
    if len(pos) == 0:
        suc = True
        return
    i, j = pos.pop()
    for k in xrange(n):
        if row_record[i][k] or col_record[j][k] or block_record[i / nr * nr + j / nr][k]:
            continue
        board[i][j] = k + 1
        row_record[i][k] = True
        col_record[j][k] = True
        block_record[i / nr * nr + j / nr][k] = True

        dfs(board)
        if suc:
            return

        block_record[i / nr * nr + j / nr][k] = False
        col_record[j][k] = False
        row_record[i][k] = False
        board[i][j] = 0
    pos.append((i, j))

def solve(board):
    global n, nr, row_record, col_record, block_record, suc, pos

    n = len(board)
    if n == 0:
        return board
    nr = int(sqrt(n))

    row_record = generate_matrix(n, n, False)
    col_record = generate_matrix(n, n, False)
    block_record = generate_matrix(n, n, False)
    suc = False

    for i in xrange(n):
        for j in xrange(n):
            if board[i][j] == 0:
                continue
            row_record[i][board[i][j] - 1] = True
            col_record[j][board[i][j] - 1] = True
            block_record[i / nr * nr + j / nr][board[i][j] - 1] = True

    pos = []
    for i in xrange(n):
        for j in xrange(n):
            if board[i][j] != 0:
                continue
            pos.append((i, j))
    suc = False
    dfs(board)

    return board if suc else []
