import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

import math

def get_seat_id(seat):
  bin_seat = seat.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
  return int(bin_seat, 2)

def run():
  with open('../data/prob05.txt') as f:
    max_seat_id = -math.inf
    for line in f.readlines():
      line = line.strip()
      seat_id = get_seat_id(line)
      max_seat_id = max(max_seat_id, seat_id)

  return max_seat_id

if __name__ == '__main__':
  print(run())
