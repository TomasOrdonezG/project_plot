import pygame
from initialize_pygame import canvas, cnvH

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 150, 0)
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (20, 20, 20)

def draw_square(x, y, side, color):
    pygame.draw.rect(canvas, color, (x, y, side, side))

def draw_rectangle(x, y, width, height, color):
    pygame.draw.rect(canvas, color, (x, y, width, height))

def draw_bordered_rectangle(x, y, width, height, fill_colour, border_color, border_size):
    draw_rectangle(x, y, width, height, fill_colour)
    pygame.draw.rect(canvas, border_color, (x, y, width, height), border_size)

def draw_circle(x, y, radius, color):
    pygame.draw.circle(canvas, color, (x, y), radius)

def draw_bordered_circle(x, y, radius, fill_color, border_color, border_size):
    if radius != 0:
        pygame.draw.circle(canvas, border_color, (x, y), radius + (border_size * 0.9), border_size)
        draw_circle(x, y, radius, fill_color)

def draw_line(x1, y1, x2, y2, color, size):
    pygame.draw.line(canvas, color, (x1, y1), (x2, y2), size)

def draw_text(text, x, y, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    canvas.blit(text_surface, (x, y))

def draw_arrow(start_pos, end_pos, color, thickness=1):
    pygame.draw.line(canvas, color, start_pos, end_pos, thickness)
    line_length = abs(start_pos[1] - end_pos[1])
    arrow_head_size = line_length * 0.15
    if end_pos[1] < start_pos[1]:  # Upward arrow
        pygame.draw.polygon(canvas, color, [
            (end_pos[0] - (arrow_head_size/1.7), end_pos[1] + (arrow_head_size)),
            (end_pos[0] + (arrow_head_size/1.7), end_pos[1] + (arrow_head_size)),
            (end_pos[0], end_pos[1])
        ])
    else:  # Downward arrow
        pygame.draw.polygon(canvas, color, [
            (end_pos[0] - (arrow_head_size/1.7), end_pos[1] - (arrow_head_size)),
            (end_pos[0] + (arrow_head_size/1.7), end_pos[1] - (arrow_head_size)),
            (end_pos[0], end_pos[1])
        ])