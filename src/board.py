board = [
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
]

#We can give an id and coordinates to each array in the matrix to do a for loop and check when clicked wich cell is clicked and what is the piece 
#on the cell

#In order the array in the matrix will be created like that :
#
# [[ID, X, Y, PieceClass], x7],


row = 0
column = 0
for j in range(len(board)):
    x, y = 80, 80 # test mouse position
    if board[column][row]['x'] and board[column][row]['y'] == x and y:
        piece = board[column][row]['piece']
        print(piece) # Return the piece on the cell
    else:
        row = row + 1
    if row == 7:
        row = 0
        column = column + 1 

