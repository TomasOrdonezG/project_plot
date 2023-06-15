from initialize_pygame import cnvH, cnvW
import pygame
from pygame_draw_library import *
from project_data import Project, IV
import math, os

class Graph:
  SCREENSHOT_DIR = 'screenshots'
  
  # ! INITIALIZATION
  def __init__(self, projects: list[Project], canvas) -> None:
    self.projects = projects
    self.canvas = canvas
    
    self.top = 100
    self.bottom = -100
    self.right = 100
    self.left = -100

    w_percentage = 0.8
    h_percentage = 0.8
    self.screen_x = ((1 - w_percentage) / 2) * cnvW
    self.screen_y = ((1 - h_percentage) / 2) * cnvH
    self.screen_w = w_percentage * cnvW
    self.screen_h = h_percentage * cnvH
    self.update_attributes()
    
    # Stylings
    self.lines = False
    self.vector_lines = False
    self.arrows = True
    self.proportional = True
    self.grid_lines = False
    
    self.center_graph()

  def update_attributes(self):
    '''Updates all the position and dimension attributes'''
    # Position and dimensions of the plane, top left corner's position
    self.width = abs(self.right - self.left)
    self.height = abs(self.bottom - self.top)
    
    self.screen_left = self.screen_x
    self.screen_right = self.screen_x + self.screen_w
    self.screen_top = self.screen_y
    self.screen_bottom = self.screen_y + self.screen_h
    if self.width != 0:
      self.pixels_per_x = self.screen_w / self.width
    if self.width != 0:
      self.pixels_per_y = self.screen_h / self.height
    
    self.x_axis_y_pos = self.screen_y + (self.pixels_per_y * self.top)  # The y value in the screen that corresponds to the x-axis
    self.y_axis_x_pos = self.screen_x - (self.pixels_per_x * self.left)  # The x value in the screen that corresponds to the y-axis

  # ! ACTIONS
  def scroll(self, dir: str):
    '''Scrolls the graph'''
    if dir == 'up' and self.bottom > -100:
      self.top -= 1
      self.bottom -= 1
    elif dir == 'down' and self.top < 100:
      self.top += 1
      self.bottom += 1
    elif dir == 'right' and self.left > -100:
      self.right -= 1
      self.left -= 1
    elif dir == 'left' and self.right < 100:
      self.right += 1
      self.left += 1
    self.update_attributes()

  def screenshot(self):
    '''Screenshots the graph'''
    if not os.path.exists(Graph.SCREENSHOT_DIR):
      os.makedirs(Graph.SCREENSHOT_DIR)
      i = 1
    else:
      if len(os.listdir(Graph.SCREENSHOT_DIR)) == 0:
        i = 1
      else:
        last_file = os.listdir(Graph.SCREENSHOT_DIR)[-1]
        Vi = last_file.index('V')
        i = int(last_file[Vi+1:-4]) + 1
    pygame.image.save(self.canvas, os.path.join(Graph.SCREENSHOT_DIR, f"plot_V{i}.png"))

  def change_scale(self, direction: str, zoom_in: bool):
    if zoom_in:
      amount = -1
    else:
      amount = 1
    
    # Y
    if direction == 'h':
      self.right += amount
      self.left -= amount
    elif direction == 'v':
      self.top += amount
      self.bottom -= amount
      
    # Fix borders
    if self.top > 100:
      self.top = 100
    elif self.top < -100:
      self.top = -100
    if self.bottom > 100:
      self.bottom = 100
    elif self.bottom < -100:
      self.bottom = -100
    if self.right > 100:
      self.right = 100
    elif self.right < -100:
      self.right = -100
    if self.left > 100:
      self.left = 100
    elif self.left < -100:
      self.left = -100
      
    if self.top <= self.bottom + 2:
      self.top = self.top + 1
      self.bottom = self.bottom - 1
    if self.right <= self.left + 2:
      self.right = self.right + 1
      self.left = self.left - 1
      
    self.update_attributes()

  def center_graph(self):
    self.top = max([project.just for project in self.projects]) + 10
    self.bottom = min([project.just for project in self.projects]) - 10
    self.right = max([anIV.just for project in self.projects for anIV in project.IVs]) + 10
    self.left = min([anIV.just for project in self.projects for anIV in project.IVs]) - 10
    self.update_attributes()
  
  # ! CONVERSION
  def pos_screen(self, plane_x: float, plane_y: float) -> tuple[float]:
    """Takes grid pos and returns a screen pos

    Args:
        grid_x (float): grid x
        grid_y (float): grid y

    Returns:
        tuple: screen x and screen y
    """
    y = self.x_axis_y_pos - (self.pixels_per_y * plane_y)
    x = self.y_axis_x_pos + (self.pixels_per_x * plane_x)
    return x, y    

  # ! DRAW
  def draw_graph(self):
    # Draw plane
    draw_bordered_rectangle(self.screen_x, self.screen_y, self.screen_w, self.screen_h, WHITE, BLACK, 2)
    self.draw_grid()
    
    # Draw zero lines
    if self.top > 0 and self.bottom < 0:
      draw_line(self.screen_left, self.x_axis_y_pos, self.screen_right - 3, self.x_axis_y_pos, BLACK, 2)
    if self.right > 0 and self.left < 0:
      draw_line(self.y_axis_x_pos, self.screen_top, self.y_axis_x_pos, self.screen_bottom, BLACK, 2)
    
    # Info
    self.draw_info()

  def draw_grid(self):
    '''Grid styling'''
    if self.grid_lines:
      for x in range(int(self.left), int(self.right)):
        if x % 5 == 0:
          x = int(x * self.pixels_per_x) + self.screen_x
          draw_line(x, self.screen_bottom, x, self.screen_top + 3, LIGHT_GRAY, 1)
        for y in range(int(self.bottom), int(self.top)):
          if y % 5 == 0:
            y = int(y * self.pixels_per_y) + self.screen_y
            draw_line(self.screen_left, y, self.screen_right - 3, y, LIGHT_GRAY, 1)

  def draw_info(self):
    '''Info on the graph'''
    font_h = int(cnvH / 20)
    
    # * Axis numbers
    draw_text(str(math.floor(self.left)), self.screen_x - 35, self.screen_y - font_h, font_h, BLACK)
    draw_text(str(math.floor(self.right)), self.screen_x + self.screen_w - 35, self.screen_y - font_h, font_h, BLACK)
    draw_text(str(math.floor(self.top)), self.screen_x + self.screen_w + 35, self.screen_y, font_h, BLACK)
    draw_text(str(math.floor(self.bottom)), self.screen_x + self.screen_w + 35, self.screen_y + self.screen_h - font_h, font_h, BLACK)

  def graph_projects(self):
    largest_IV_r = 0
    projects = sorted(self.projects, key=lambda a_project: abs(max([abs(anIV.beta) for anIV in a_project.IVs])), reverse=True)
    for project in projects:
      if project.name == 'p1':
        colour = (255, 8, 232)
      else:
        colour = BLACK
      
      # Extra lines
      if self.lines and project.IVs[0].in_grid:
        _, y = self.pos_screen(0, project.just)
        draw_line(self.screen_left, y, self.screen_right, y, LIGHT_GRAY, 1);
      if self.vector_lines:
        sorted_IVs_just = sorted(project.IVs, key=lambda anIV: anIV.just)
        for i in range(len(sorted_IVs_just) - 1):
          if sorted_IVs_just[i].in_grid:
            # Get coords
            y1up = self.pos_screen(1, project.just)[1] + abs(sorted_IVs_just[i].beta) * (cnvH / 10)
            y2up = self.pos_screen(1, project.just)[1] + abs(sorted_IVs_just[i+1].beta) * (cnvH / 10)
            y1down = self.pos_screen(1, project.just)[1] - abs(sorted_IVs_just[i].beta) * (cnvH / 10)
            y2down = self.pos_screen(1, project.just)[1] - abs(sorted_IVs_just[i+1].beta) * (cnvH / 10)
            x1 = self.pos_screen(sorted_IVs_just[i].just, 1)[0]
            x2 = self.pos_screen(sorted_IVs_just[i+1].just, 1)[0]

            # Draw lines
            draw_line(x1, y1up, x2, y2up, colour, 2)
            draw_line(x1, y1down, x2, y2down, colour, 2)

      # Draw IVs, sort first
      IVs = sorted(project.IVs, key=lambda anIV: abs(anIV.beta), reverse=True)
      for pIV in IVs:
        x, y = self.pos_screen(pIV.just, project.just)
        beta = abs(pIV.beta) * (cnvH / 10)
        if beta > largest_IV_r:
          largest_IV_r = beta

          
        if pIV.in_grid:
          draw_bordered_circle(x, y, beta, pIV.colour, colour, 2)

      threshhold = largest_IV_r * 0.3
      for pIV in project.IVs:
        # Arrows          
        if self.arrows:
          r = pIV.beta * (cnvH / 10)
          size = r
          if abs(r) > threshhold:
            x, y = self.pos_screen(pIV.just, project.just)
          else:
            x, y = self.pos_screen(pIV.just, project.just)
            y += size
            if not self.proportional:
              size = threshhold * (size / abs(size))
                
          if pIV.in_grid:
            draw_arrow((x, y), (x, y-size), DARK_GRAY, 1)
       
        # Update Visibility
        if project.just < self.top and project.just > self.bottom and pIV.just < self.right and pIV.just > self.left:
          pIV.in_grid = True
        else:
          pIV.in_grid = False