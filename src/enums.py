"""
Enumerations for the Chess game.
Provides type safety and replaces magic numbers.
"""
from enum import Enum, IntEnum


class Color(IntEnum):
    """
    Piece colors using IntEnum for backward compatibility.
    WHITE = 1, BLACK = -1 maintains existing arithmetic (e.g., -self.color for opponent)
    """
    WHITE = 1
    BLACK = -1


class MoveType(Enum):
    """
    Types of moves that can be made, used for sound effects and game state.
    """
    MOVE = "move"
    CAPTURE = "capture"
    CHECK = "check"
    CASTLING = "castling"
    CHECKMATE = "checkmate"
    STALEMATE = "stalemate"
    EN_PASSANT = "en_passant"
    PROMOTION = "promotion"


class PieceType(Enum):
    """
    Types of chess pieces.
    """
    PAWN = "pawn"
    KNIGHT = "knight"
    BISHOP = "bishop"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"
