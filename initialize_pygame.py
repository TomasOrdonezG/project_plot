#import and initialize
import pygame
pygame.init()

#create screen/canvas
canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_info = pygame.display.Info()
cnvW = screen_info.current_w
cnvH = screen_info.current_h
pygame.display.set_caption("data thing for dad")