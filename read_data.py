from project_data import Project, IV

def read_data() -> list:
  """Reads data from a file

  Returns:
    list: list of all projects as project objects
  """

  # Initialize projects list
  projects = []

  # Read data
  with open('data.txt', 'r') as file:
    lol = file.readlines()
    for line_i in range(len(lol)):
      lol[line_i] = lol[line_i].strip().split('	')

  # Extract lines  
  names_just = lol[0]
  IV_lines = []
  for IV_line_index in range(2, 7):
    IV_lines.append(lol[IV_line_index])
  
  # Create project objects, loops once per project and each run creates and appends a project object
  for i in range(1, len(lol[0]), 2):
    # Prrject indexes
    pi1 = i
    pi2 = i+1
    
    # Read project data
    name = names_just[pi1]
    project_just = float(names_just[pi2])
    IVs = []
    for IV_num in range(1, 6):
      IV_line_index = IV_num - 1
      IV_line = IV_lines[IV_line_index]
      IV_beta = float(IV_line[pi1])
      IV_just = float(IV_line[pi2])
      IVs.append(IV(IV_num, IV_beta, IV_just))
        
    projects.append(Project(name, project_just, IVs))

  return projects
