from pygame_draw_library import *
from initialize_pygame import canvas, cnvH, cnvW
from project_data import Project, IV
from read_data import read_data
import pygame
from graph import Graph

def main():
  # Initialization of the program
  print('\n   ### START ###\n')

  # Read data and store in a list
  projects = read_data()
  
  # Create graph
  graph = Graph(projects, canvas)
  
  # Assign FPS a value
  running = True
  while running:
    # Clear screen
    canvas.fill((255, 255, 255))
    
    # Draw and plot
    graph.draw_graph()
    graph.graph_projects()

    # Events
    for event in pygame.event.get():
      keys = pygame.key.get_pressed()
      if event.type == pygame.KEYDOWN:
        # * Key down events
        if event.key ==pygame.K_ESCAPE:
          running = False
        if event.key == pygame.K_s:
          graph.screenshot()
        if event.key == pygame.K_1:
          graph.lines = not graph.lines
        if event.key == pygame.K_2:
          graph.vector_lines = not graph.vector_lines
        if event.key == pygame.K_3:
          graph.arrows = not graph.arrows
        if event.key == pygame.K_p:
          graph.proportional = not graph.proportional
        if event.key == pygame.K_c:
          graph.center_graph()

      # * Mouse events
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if keys[pygame.K_LSHIFT]:
          # * X axis
          
          # Zoom
          if keys[pygame.K_LCTRL]:
            if event.button == 4:
              graph.change_scale('h', True)
            elif event.button == 5:
              graph.change_scale('h', False)
          else:
            # Scroll
            if event.button == 4:  # Scroll up
              graph.scroll('left')
            elif event.button == 5:  # Scroll down
              graph.scroll('right')
            
          
        else:
          # * Y axis
          
          # Zoom
          if keys[pygame.K_LCTRL]:
            if event.button == 4:
              graph.change_scale('v', True)
            elif event.button == 5:
              graph.change_scale('v', False)
          else:
            # Scroll
            if event.button == 4:  # Scroll up
              graph.scroll('down')
            elif event.button == 5:  # Scroll down
              graph.scroll('up')

    #Update display
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__':
  main()
