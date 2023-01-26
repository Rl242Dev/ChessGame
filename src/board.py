board = [
    [[1,80,80], [2,160,80], [3,240,80], [4,320,80], [5,400,80], [6,480,80], [7,560,80], [8,640,80]],
    [[9,80,160], [10,160,160], [11,240,160], [12,320,160], [13,400,160], [14,480,160], [15,560,160], [16,640,80]],
    [[17,80,240], [18,160,140], [19,240,240], [20,320,240], [21,400,240], [22,480,240], [23,560,240], [24,640,240]],
    [[25,80,320], [26,160,320], [27,240,320], [28,320,320], [29,400,320], [30,480,320], [31,560,320], [32,640,320]],
    [[33,80,400], [34,240,400], [35,240,400], [36,320,400], [37,400,400], [38,480,400], [39,560,400], [40,640,400]],
    [[41,80,480], [42,160,480], [43,240,480], [44,320,480], [45,400,480], [46,480,480], [47,560,480], [48,640,480]],
    [[49,80,560], [50,160,560], [51,240,560], [52,320,560], [53,400,560], [54,480,560], [55,560,560], [56,640,560]],
    [[57,80,640], [58,160,640], [59,240,640], [60,320,640], [61,400,640], [62,480,640], [63,560,640], [64,640,640]],
]

#We can give an id and coordinates to each array in the matrix to do a for loop and check when clicked wich cell is clicked and what is the piece 
#on the cell. We can do if X + 79 and Y + 79 are in range of X and Y of the array then it's the good coordinates

#In order the array in the matrix will be created like that (in a function that we can call in main) :
#
# [[ID, X, Y, PieceClass], x7],
#
#row = 0
#column = 0
#for j in range(len(board)):
#    x, y = 80, 80 # test mouse position
#    if board[column][row]['x'] and board[column][row]['y'] == x and y:
#        piece = board[column][row]['piece']
#        print(piece) # Return the piece on the cell
#    else:
#        row = row + 1
#    if row == 7:
#        row = 0
#        column = column + 1 

