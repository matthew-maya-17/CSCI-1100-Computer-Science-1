bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])

print ('-' * 25)
for i in range(len(bd)):
    line = '| '
    for j in range(len(bd[0])):
        if j == 3 or j == 6:
            line = line + '| '
        line = line + bd[i][j] + ' '
    line = line + '|'
    print(line)
    if i == 2 or i == 5:
        print('-' * 25)
print ('-' * 25)