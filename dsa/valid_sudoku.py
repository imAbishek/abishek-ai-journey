board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

box = {}
for i in range(len(board)):
    seenRow = set()
    seenColumn = set()
    for j in range(len(board[i])):
        key = (i // 3, j // 3)
        print(key)
        if key not in box:
            box[key] = set()
        # print(box)
        row = board[i][j]
        if row != ".":
            if row not in seenRow:
                seenRow.add(row)
            else:
                print('Row')

            if row not in box[key]:
                box[key].add(row)
            else:
                print('Box')
        column = board[j][i]
        if column != ".":
            if column not in seenColumn:
                seenColumn.add(column)
            else:
                print('Column')
print(box)