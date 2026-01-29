import math
import pygame
from src.configs import *

class Button:

    def __init__(self, screen, size, center_location):
        self.screen = screen
        self.size = size
        self.center_location = center_location
        self.rect = pygame.Rect(
            center_location[0] - size / 2,
            center_location[1] - size / 2,
            size,
            size
        )
    
    def checkCollision(self, pos_mouse):
        # Use rect collision for better click detection
        return self.rect.collidepoint(pos_mouse)

    def draw_background(self, is_hovered=False):
        """Draw modern button background with shadow and border."""
        # Shadow (more pronounced)
        shadow_rect = self.rect.copy()
        shadow_rect.x += 3
        shadow_rect.y += 3
        pygame.draw.rect(self.screen, (0, 0, 0, 180), shadow_rect, border_radius=10)
        
        # Background with hover effect (darker, more contrast)
        bg_color = (65, 65, 65) if is_hovered else (45, 45, 45)
        pygame.draw.rect(self.screen, bg_color, self.rect, border_radius=10)
        
        # Border (gold - more visible)
        border_color = (220, 190, 130) if is_hovered else (185, 155, 95)
        border_width = 3 if is_hovered else 2
        pygame.draw.rect(self.screen, border_color, self.rect, width=border_width, border_radius=10)

    def displayButton(self):
        self.draw_background()
    

class Sound_Button(Button):

    def __init__(self, screen, size, center_location):
        super().__init__(screen, size, center_location)
        self.sound_on = True

    def changeButton(self):
        self.sound_on = not self.sound_on
    
    def _draw_aa_arc(self, cx, cy, radius, start_angle, end_angle, color, thickness=2):
        """Draw an anti-aliased arc using small line segments."""
        num_segments = max(20, int(radius * 2))
        points = []
        for i in range(num_segments + 1):
            angle = start_angle + (end_angle - start_angle) * i / num_segments
            x = cx + radius * math.cos(angle)
            y = cy - radius * math.sin(angle)
            points.append((x, y))

        if len(points) >= 2:
            pygame.draw.lines(self.screen, color, False, points, thickness)

    def draw_sound_icon(self):
        """Draw an ultra-modern, refined speaker icon."""
        cx, cy = self.center_location

        # Shift icon slightly left to make room for waves
        icon_offset = -4
        speaker_cx = cx + icon_offset

        if self.sound_on:
            # Modern speaker cone with smooth gradient look
            # Base trapezoid (larger and more defined)
            speaker_base = [
                (speaker_cx - 10, cy - 6),
                (speaker_cx - 10, cy + 6),
                (speaker_cx, cy + 9),
                (speaker_cx, cy - 9)
            ]
            # Fill with white/light gray
            pygame.draw.polygon(self.screen, (255, 255, 255), speaker_base)
            # Gold outline
            pygame.draw.polygon(self.screen, (200, 170, 110), speaker_base, 2)

            # Speaker body/box with 3D effect
            box_rect = pygame.Rect(speaker_cx - 15, cy - 6, 6, 12)
            # Main box
            pygame.draw.rect(self.screen, (245, 245, 245), box_rect)
            # Inner shadow for depth
            pygame.draw.rect(self.screen, (220, 220, 220), (speaker_cx - 14, cy - 5, 4, 10))
            # Gold outline
            pygame.draw.rect(self.screen, (200, 170, 110), box_rect, 2)

            # Sound waves - smaller radii to fit in button frame
            # Using anti-aliased drawing method
            wave_cx = speaker_cx + 2
            wave_data = [
                (7, (120, 230, 120), 3),   # Closest - brightest green
                (12, (100, 210, 100), 2),  # Mid
                (17, (80, 190, 80), 2),    # Far
            ]

            for radius, color, thickness in wave_data:
                # Draw arc from -45° to +45° (in radians: -π/4 to π/4)
                self._draw_aa_arc(wave_cx, cy, radius, -0.65, 0.65, color, thickness)
                
        else:
            # Muted speaker - monochrome with red X
            speaker_base = [
                (speaker_cx - 10, cy - 6),
                (speaker_cx - 10, cy + 6),
                (speaker_cx, cy + 9),
                (speaker_cx, cy - 9)
            ]
            # Gray fill
            pygame.draw.polygon(self.screen, (130, 130, 130), speaker_base)
            # Dark outline
            pygame.draw.polygon(self.screen, (80, 80, 80), speaker_base, 2)

            # Speaker box
            box_rect = pygame.Rect(speaker_cx - 15, cy - 6, 6, 12)
            pygame.draw.rect(self.screen, (120, 120, 120), box_rect)
            pygame.draw.rect(self.screen, (90, 90, 90), (speaker_cx - 14, cy - 5, 4, 10))
            pygame.draw.rect(self.screen, (80, 80, 80), box_rect, 2)

            # Modern X mark - positioned further right to avoid speaker
            x_cx = speaker_cx + 10  # Moved further right
            x_glow = (180, 50, 50)
            x_bright = (240, 60, 60)

            # Glow/shadow layer
            pygame.draw.line(self.screen, x_glow, (x_cx - 5, cy - 6), (x_cx + 5, cy + 6), 4)
            pygame.draw.line(self.screen, x_glow, (x_cx - 5, cy + 6), (x_cx + 5, cy - 6), 4)

            # Bright main X
            pygame.draw.line(self.screen, x_bright, (x_cx - 4, cy - 5), (x_cx + 4, cy + 5), 3)
            pygame.draw.line(self.screen, x_bright, (x_cx - 4, cy + 5), (x_cx + 4, cy - 5), 3)

    def displayButton(self):
        self.draw_background()
        self.draw_sound_icon()
    
    def displayButtonWithLabel(self, is_hovered=False):
        """Display button with modern styling and label."""
        self.draw_background(is_hovered)
        self.draw_sound_icon()
        
        # Label below button with better typography
        font = pygame.font.Font(None, 22)
        label = "SOUND: ON" if self.sound_on else "SOUND: OFF"
        color = (130, 230, 130) if self.sound_on else (230, 90, 90)
        text = font.render(label, True, color)
        text_rect = text.get_rect(center=(self.center_location[0], self.center_location[1] + self.size // 2 + 18))
        self.screen.blit(text, text_rect)
    
    def buttonUpdateClick(self, initial_pos_mouse):
        if self.checkCollision(initial_pos_mouse):
            self.changeButton()

    def activateFunctionButton(self, pos_mouse):
        if self.checkCollision(pos_mouse) and not pygame.mouse.get_pressed()[0]:
            self.displayButton()


class BoardColor_Button(Button):

    def __init__(self, screen, size, center_location):
        super().__init__(screen, size, center_location)
        self.mod_board = "blue_mod"

    def changeColorBoard(self):
        if self.mod_board == "brown_mod":
            self.mod_board = "blue_mod"
        elif self.mod_board == "blue_mod":
            self.mod_board = "green_mod"
        else:
            self.mod_board = "brown_mod"
    
    def draw_palette_icon(self):
        """Draw an ultra-clean chess board pattern icon."""
        cx, cy = self.center_location
        
        # Enhanced color schemes with better contrast
        colors = {
            "brown_mod": [(90, 60, 30), (245, 220, 185)],
            "blue_mod": [(50, 85, 200), (170, 205, 245)],
            "green_mod": [(70, 110, 50), (175, 220, 155)]
        }
        
        theme_colors = colors.get(self.mod_board, colors["blue_mod"])
        
        # Larger board pattern (2x2 squares) with more spacing
        square_size = 10
        
        # Subtle shadow behind for depth
        shadow_offset = 2
        for i in range(2):
            for j in range(2):
                x = cx - square_size + (j * square_size) + shadow_offset
                y = cy - square_size + (i * square_size) + shadow_offset
                pygame.draw.rect(self.screen, (15, 15, 15), (x, y, square_size, square_size))
        
        # Draw elegant board pattern
        # Top-left (dark)
        pygame.draw.rect(self.screen, theme_colors[0], 
                        (cx - square_size, cy - square_size, square_size, square_size))
        pygame.draw.rect(self.screen, (200, 170, 110), 
                        (cx - square_size, cy - square_size, square_size, square_size), 2)
        
        # Top-right (light)
        pygame.draw.rect(self.screen, theme_colors[1], 
                        (cx, cy - square_size, square_size, square_size))
        pygame.draw.rect(self.screen, (200, 170, 110), 
                        (cx, cy - square_size, square_size, square_size), 2)
        
        # Bottom-left (light)
        pygame.draw.rect(self.screen, theme_colors[1], 
                        (cx - square_size, cy, square_size, square_size))
        pygame.draw.rect(self.screen, (200, 170, 110), 
                        (cx - square_size, cy, square_size, square_size), 2)
        
        # Bottom-right (dark)
        pygame.draw.rect(self.screen, theme_colors[0], 
                        (cx, cy, square_size, square_size))
        pygame.draw.rect(self.screen, (200, 170, 110), 
                        (cx, cy, square_size, square_size), 2)
        
        # Top-right square (light)
        pygame.draw.rect(self.screen, theme_colors[1], 
                        (cx, cy - square_size, square_size, square_size))
        pygame.draw.rect(self.screen, (185, 155, 95), 
                        (cx, cy - square_size, square_size, square_size), 1)
        
        # Bottom-left square (light)
        pygame.draw.rect(self.screen, theme_colors[1], 
                        (cx - square_size, cy, square_size, square_size))
        pygame.draw.rect(self.screen, (185, 155, 95), 
                        (cx - square_size, cy, square_size, square_size), 1)
        
        # Bottom-right square (dark)
        pygame.draw.rect(self.screen, theme_colors[0], 
                        (cx, cy, square_size, square_size))
        pygame.draw.rect(self.screen, (185, 155, 95), 
                        (cx, cy, square_size, square_size), 1)
    
    def displayButton(self):
        self.draw_background()
        self.draw_palette_icon()
    
    def buttonUpdateClick(self, initial_pos_mouse):
        if self.checkCollision(initial_pos_mouse):
            self.changeColorBoard()

    def activateFunctionButton(self, pos_mouse):
        if self.checkCollision(pos_mouse) and not pygame.mouse.get_pressed()[0]:
            self.displayButton()
    
    def displayButtonWithLabel(self, is_hovered=False):
        """Display button with modern styling and label."""
        self.draw_background(is_hovered)
        self.draw_palette_icon()
        
        # Label below button with better typography
        font = pygame.font.Font(None, 22)
        label_text = {"brown_mod": "BROWN", "blue_mod": "BLUE", "green_mod": "GREEN"}
        label = f"THEME: {label_text.get(self.mod_board, 'BLUE')}"
        text = font.render(label, True, (230, 230, 230))
        text_rect = text.get_rect(center=(self.center_location[0], self.center_location[1] + self.size // 2 + 18))
        self.screen.blit(text, text_rect)