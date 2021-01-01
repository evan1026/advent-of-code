import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

import math
from functools import reduce

class ModVal:
  def __init__(self, value, mod):
    self.rem = value % mod
    self.mod = mod

def chinese_remainder_theorem(vals):
  big_n = reduce(lambda val1, val2: val1 * val2, [val.mod for val in vals])

  running_sum = 0
  for i in range(len(vals)):
    y_val = big_n // vals[i].mod
    z_val = modular_inverse(y_val, vals[i].mod)
    product = vals[i].rem * y_val * z_val
    running_sum += product

  return running_sum % big_n

def modular_inverse(value, mod):
  g, x, y = egcd(value, mod)
  if g != 1:
    raise Exception('Cannot compute modular inverse')
  else:
    return x % mod

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def run():
  with open('../data/prob13.txt') as f:
    lines = f.readlines()
    timestamp = int(lines[0].strip())
    bus_raw_vals = lines[1].strip().split(',')
    busses = [ModVal(-i, int(bus_raw_vals[i])) for i in range(len(bus_raw_vals)) if bus_raw_vals[i] != 'x']

  return chinese_remainder_theorem(busses)


if __name__ == '__main__':
  print(run())
