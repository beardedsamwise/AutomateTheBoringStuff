def isValidChessBoard(inputBoard):
    # chess board array. note: not a full size board.
    board = ['1h','6c','2g','5h','3e']
    # array of chess pieces. note: only a subset of pieces.
    pieces = ['bking','wqueen','bbishop','bqueen','wking']
    # set variables 
    validSpace = True
    validPiece = True
    # check keys and values are valid / check if board and pieces are valid 
    for k, v in inputBoard.items():
        if not (k in board):
            validSpace = False
            break
        if not (v in pieces):
            validPiece = False
            break
    if validSpace and validPiece:
        print("You have a valid chess board")
    else:
        if not validPiece:
            print("There is a problem with your chess pieces")
        if not validSpace:
            print("There is a problem with your chess board")
    
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 

isValidChessBoard(chessBoard)

