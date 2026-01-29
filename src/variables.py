"""
Backward compatibility layer for global state access.
Maintained for IA.py compatibility - DO NOT REMOVE these global variables.

This module provides the same interface as before (board_pieces, list_white_pieces,
list_black_pieces) but now backed by a GameState instance.
"""
from src.game_state import GameState

# Singleton game state instance
_game_state: GameState = None


def get_game_state() -> GameState:
    """Get the current game state, creating it if necessary."""
    global _game_state
    if _game_state is None:
        _game_state = GameState()
    return _game_state


def set_game_state(new_state: GameState) -> None:
    """Set a new game state (used for testing or reset)."""
    global _game_state, board_pieces, list_white_pieces, list_black_pieces
    _game_state = new_state
    # Update global references to point to new state's data
    board_pieces = _game_state.board
    list_white_pieces = _game_state._white_pieces
    list_black_pieces = _game_state._black_pieces


def initialize_game() -> GameState:
    """
    Initialize or reset the game to starting position.
    Updates global variables for backward compatibility.

    Returns:
        The initialized GameState instance
    """
    global _game_state, board_pieces, list_white_pieces, list_black_pieces

    _game_state = GameState()
    _game_state.setup_initial_position()

    # These global references are used by IA.py and other modules
    board_pieces = _game_state.board
    list_white_pieces = _game_state._white_pieces
    list_black_pieces = _game_state._black_pieces

    return _game_state


# Initialize on module load for backward compatibility with existing code
# This creates the initial board state when the module is first imported
_game_state = GameState()
_game_state.setup_initial_position()

# Global variables for backward compatibility with IA.py
# These MUST remain accessible as module-level variables
board_pieces = _game_state.board
list_white_pieces = _game_state._white_pieces
list_black_pieces = _game_state._black_pieces
