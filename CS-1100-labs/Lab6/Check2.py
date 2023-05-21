bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def ok_to_add(row, col, num):
    
    rstart = (row // 3) * 3
    cstart = (col // 3) * 3
    
    
    for i in range(9):
        if bd[row][i] == str(num):
            return False
    for j in range(9):
        if bd[j][col] == str(num):
            return False
    for k in range (rstart, rstart + 3):
        for l in range(cstart, cstart + 3):
            if bd[k][l] == str(num):
                return False
    return True

print(ok_to_add(2,0,6))
print(ok_to_add(1,8,3))
print(ok_to_add(2,9,2))
print(ok_to_add(5,7,1))
print(ok_to_add(3,4,5))
print(ok_to_add(0,8,1))