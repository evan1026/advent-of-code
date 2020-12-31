import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

import math

class Instruction:
  def __init__(self, inst, value):
    self.inst = inst
    self.value = value

def rotate_vector(vec, deg):
  new_vec = vec[:]
  rads = deg / 180 * math.pi
  cos_val = math.cos(rads)
  sin_val = math.sin(rads)
  new_vec[0] = cos_val * vec[0] - sin_val * vec[1]
  new_vec[1] = sin_val * vec[0] + cos_val * vec[1]
  return new_vec

def run():
  instructions = []
  with open('../data/prob12.txt') as f:
    for line in f.readlines():
      line = line.strip()
      instructions.append(Instruction(line[0], int(line[1:])))

  pos = [0, 0]
  waypoint_pos = [10, 1]
  for instruction in instructions:
    if instruction.inst == 'N':
      waypoint_pos[1] += instruction.value
    elif instruction.inst == 'S':
      waypoint_pos[1] -= instruction.value
    elif instruction.inst == 'E':
      waypoint_pos[0] += instruction.value
    elif instruction.inst == 'W':
      waypoint_pos[0] -= instruction.value
    elif instruction.inst == 'R':
      waypoint_pos = rotate_vector(waypoint_pos, -instruction.value)
    elif instruction.inst == 'L':
      waypoint_pos = rotate_vector(waypoint_pos, instruction.value)
    elif instruction.inst == 'F':
      pos[0] += waypoint_pos[0] * instruction.value
      pos[1] += waypoint_pos[1] * instruction.value

  manhattan_distance = abs(round(pos[0])) + abs(round(pos[1]))
  return manhattan_distance

if __name__ == '__main__':
  print(run())
