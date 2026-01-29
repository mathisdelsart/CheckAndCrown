"""
Game state initialization.
"""
from src.game_state import GameState


def initialize_game() -> GameState:
    """
    Initialize or reset the game to starting position.

    Returns:
        The initialized GameState instance
    """
    game_state = GameState()
    game_state.setup_initial_position()
    return game_state
