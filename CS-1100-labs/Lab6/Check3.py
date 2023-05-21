from lab06_util import read_sudoku

def ok_to_add(row, col, num, board):
    
    rstart = (row // 3) * 3
    cstart = (col // 3) * 3
    
    
    for i in range(9):
        if board[row][i] == str(num):
            return False
    for j in range(9):
        if board[j][col] == str(num):
            return False
    for k in range (rstart, rstart + 3):
        for l in range(cstart, cstart + 3):
            if board[k][l] == str(num):
                return False
    return True

def verify_board(board_verify):
    for i in range(0, 9):
        for j in range(0, 9):
            save = board_verify[i][j]
            board_verify[i][j] = '.'
            if ok_to_add(i, j, save, board_verify) == False:
                return False
            board_verify[i][j] = save
    return True

def print_bd(board_print):
    print ('-' * 25)
    for i in range(len(board_print)):
        line = '| '
        for j in range(len(board_print[0])):
            if j == 3 or j == 6:
                line = line + '| '
            line = line + str(board_print[i][j]) + ' '
        line = line + '|'
        print(line)
        if i == 2 or i == 5:
            print('-' * 25)
    print ('-' * 25)

fname = input("Please enter a file name ==> ")
bd = read_sudoku(fname)
print_bd(bd)

while verify_board(bd) != True:
    r = int(input('Enter a row to modify: '))
    c = int(input('Enter a col to modify: '))
    n = int(input('Enter a number to add: '))
    if ok_to_add(r, c, n, bd):
        bd[r][c] = n
    print_bd(bd)

