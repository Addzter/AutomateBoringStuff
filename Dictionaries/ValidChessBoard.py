# {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
# '5h': 'bqueen', '3e': 'wking'}

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


# Takes a dictionary chessboard and checks if it's valid
def isValidChessBoard(board):
    bking_count = 0
    wking_count = 0
    white_total = 0
    black_total = 0
    bpawn_count = 0
    wpawn_count = 0

    allowed_pieces = ['wking', 'wqueen', 'wrook', 'wbishop', 'wknight', 'wpawn', 'bking', 'bqueen', 'brook', 'bbishop', 'bknight', 'bpawn']

    allowed_spaces = [
        '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a',
        '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
        '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
        '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
        '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
        '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
        '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
        '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h']

    # checks that only 2 Kings
    for k, v in board.items():
        if v == 'bking':
            bking_count += 1
        elif v == 'wking':
            wking_count += 1

    if bking_count > 1 or wking_count > 1:
        print('White or Black has more than 1 King!')
        return False

    # checks that no more than 8 pawns each side
    for k, v in board.items():
        if v == 'bpawn':
            bpawn_count += 1
        elif v == 'wpawn':
            wpawn_count += 1

    if bpawn_count > 8 or wpawn_count > 8:
        print('White or Black or has more than 8 Pawns!')
        return False

    # Creates total and ensures no more than 16 per colour
    for v in board.values():
        if v[0] == 'b':
            black_total += 1
        elif v[0] == 'w':
            white_total += 1

    if black_total > 16 or white_total > 16:
        print('White or Black has more than 16 pieces!')
        return False

    # Must be a valid piece name (pawn, knight, rook etc.) and start with w/b
    for v in board.values():
        if v not in allowed_pieces:
            print(f'{v} is not a valid chess piece!')
            print('Pieces must be format: "(w/b)king')
            return False

    for k in board.keys():
        if k not in allowed_spaces:
            print(f'{k} is not a valid chess square. (1a - 8h) accepted.')
            return False

    return True


print(isValidChessBoard(chessBoard))
