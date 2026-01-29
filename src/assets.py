import pygame
from src.configs import *

class Asset:
    
    def __init__(self,link_image, dimension):
        self.link_image = link_image
        self.dimension = dimension

    def load_image(self):
        """
        Load the image and transform it with the right dimension
        :return: the image load and transformed
        """
        image = pygame.image.load(self.link_image).convert_alpha()
        image = pygame.transform.scale(image, self.dimension)
        return image

# Black pieces images
black_king_image = Asset("assets/pieces/bK.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
black_queen_image = Asset("assets/pieces/bQ.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
black_rook_image = Asset("assets/pieces/bR.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
black_bishop_image = Asset("assets/pieces/bB.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
black_knight_image = Asset("assets/pieces/bKN.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
black_pawn_image = Asset("assets/pieces/bP.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()

# White pieces images
white_king_image = Asset("assets/pieces/wK.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
white_queen_image = Asset("assets/pieces/wQ.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
white_rook_image = Asset("assets/pieces/wR.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
white_bishop_image = Asset("assets/pieces/wB.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
white_knight_image = Asset("assets/pieces/wKN.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()
white_pawn_image = Asset("assets/pieces/wP.png", (SIZE_SQUARE, SIZE_SQUARE)).load_image()

# Music sounds
pygame.mixer.init()
move_sound = pygame.mixer.Sound("assets/sounds/move-sound.mp3")
capture_sound = pygame.mixer.Sound("assets/sounds/capture-sound.mp3")
castling_sound = pygame.mixer.Sound("assets/sounds/castling-sound.mp3")
check_sound = pygame.mixer.Sound("assets/sounds/check-sound.mp3")
game_start_sound = pygame.mixer.Sound("assets/sounds/game_start-sound.mp3")
checkmate_sound = pygame.mixer.Sound("assets/sounds/checkmate-sound.mp3")
stalemate_sound = pygame.mixer.Sound("assets/sounds/stalemate-sound.mp3")