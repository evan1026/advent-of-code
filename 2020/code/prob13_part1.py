import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

import math

def run():
  with open('../data/prob13.txt') as f:
    lines = f.readlines()
    timestamp = int(lines[0].strip())
    busses = [int(x) for x in lines[1].strip().split(',') if x != 'x']

  best_bus = (-1, math.inf)
  for bus in busses:
    wait_time = bus - (timestamp % bus)
    if wait_time < best_bus[1]:
      best_bus = (bus, wait_time)

  return best_bus[0] * best_bus[1]


if __name__ == '__main__':
  print(run())
