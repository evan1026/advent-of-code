import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

import math

class Instruction:
  def __init__(self, inst, value):
    self.inst = inst
    self.value = value

def run():
  instructions = []
  with open('../data/prob12.txt') as f:
    for line in f.readlines():
      line = line.strip()
      instructions.append(Instruction(line[0], int(line[1:])))

  direction = 0
  pos = [0, 0]
  for instruction in instructions:
    if instruction.inst == 'N':
      pos[1] += instruction.value
    elif instruction.inst == 'S':
      pos[1] -= instruction.value
    elif instruction.inst == 'E':
      pos[0] += instruction.value
    elif instruction.inst == 'W':
      pos[0] -= instruction.value
    elif instruction.inst == 'R':
      direction = (direction - instruction.value) % 360
    elif instruction.inst == 'L':
      direction = (direction + instruction.value) % 360
    elif instruction.inst == 'F':
      rads = (direction / 180) * math.pi
      pos[0] += math.cos(rads) * instruction.value
      pos[1] += math.sin(rads) * instruction.value

  manhattan_distance = abs(round(pos[0])) + abs(round(pos[1]))
  return manhattan_distance


if __name__ == '__main__':
  print(run())
