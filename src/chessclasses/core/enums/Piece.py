import enum

__all__ = ["Piece"]

class Piece(enum.IntEnum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6
    

    
