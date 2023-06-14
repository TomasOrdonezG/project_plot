from pygame_draw_library import BLUE, GREEN, RED, ORANGE, WHITE

class IV:
  def __init__(self, number: int, beta: float, var_just: float) -> None:
    self.number = number
    self.beta = beta
    self.just = var_just
    self.colour = [BLUE, GREEN, RED, ORANGE, WHITE][self.number - 1]
    self.in_grid = True
  
  def __str__(self):
    return '%2.2f  %2.2f' % (self.beta, self.just)

class Project:
  def __init__(self, name: str, project_just: float, IVs: list[IV]) -> None:
    self.name = name
    self.just = project_just
    self.IVs = IVs
  
  # def get_IV(self, n: int) -> IV:
  #   '''Gets the IV variable by its number'''
  #   return self.IVs[n - 1]
  
  def __str__(self) -> str:
    return f'\n Name: {self.name}  Just: {self.just}\n\nName  Beta  Just\nIV1: {self.IV1}\nIV2: {self.IV2}\nIV3: {self.IV3}\nIV4: {self.IV4}\nIV5: {self.IV5}\n'
