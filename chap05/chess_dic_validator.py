import sys
import pprint

def main() -> int:
    chess_board = {
        '1h': 'bking', '6c': 'wqueen',
        '2g': 'bbishop', '5h': 'bqueen',
        '3e': 'wking',
    }

    print('Chess board:')
    pprint.pprint(chess_board)
    print()

    if is_valid_chessboard(chess_board):
        print('This is a valid chessboard.')
    else:
        print('This is an invalid chessboard.')

    return 0

def is_valid_chessboard(chess_board: dict) -> bool:
    count_pieces = {}
    for piece in chess_board.values():
        count_pieces.setdefault(piece, 0)
        count_pieces[piece] += 1

    # check for valid number of kings and queens
    if (
        count_pieces.get('bking', 0) > 1
        or count_pieces.get('wking', 0) > 1
        or count_pieces.get('wqueen', 0) > 1
        or count_pieces.get('bqueen', 0) > 1
    ):
        print('~> Invalid number of kings/queens.')
        print(
            f"  ~> Black kings:  {count_pieces.get('bking', 0)}\n"
            f"  ~> White Kings:  {count_pieces.get('wking', 0)}\n"
            f"  ~> Black queens: {count_pieces.get('bqueen', 0)}\n"
            f"  ~> White queens: {count_pieces.get('wqueen', 0)}"
        )
        return False

    # check for valid names
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for piece in chess_board.values():
        if piece[0] != 'w' and piece[0] != 'b':
            print(f'~> Invalid piece name: {piece}')
            return False
        if piece[1:] not in valid_pieces:
            print(f'~> Invalid piece name: {piece}')
            return False

    # check for correct number of pieces for each player
    white_pieces_count = 0
    black_pieces_count = 0
    for piece, count in count_pieces.items():
        if piece.startswith('b'):
            black_pieces_count += 1
        elif piece.startswith('w'):
            white_pieces_count += 1
    if white_pieces_count > 16 or black_pieces_count > 16:
        print('~> Invalid number of pieces for either black or white.')
        print(f'  ~> black total pieces: {black_pieces_count}')
        print(f'  ~> white total pieces: {white_pieces_count}')
        return False

    # check for valid positions
    valid_positions = [str(n) + c for n in range(1, 9) for c in 'abcdefgh']
    for pos in chess_board.keys():
        if pos not in valid_positions:
            print(
                f'~> Invalid position for piece '
                f'`{chess_board.get(pos)}`: {pos}'
            )
            return False

    return True

if __name__ == '__main__':
    sys.exit(main())
