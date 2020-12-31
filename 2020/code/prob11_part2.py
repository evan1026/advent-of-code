import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

# TODO needs optimization

EMPTY = 0
OCCUP = 1
FLOOR = 2

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def seats_to_string(seats):
  out = ''
  for row in seats:
    for seat in row:
      if seat == EMPTY:
        out += 'L'
      elif seat == OCCUP:
        out += '#'
      else:
        out += '.'
    out += '\n'
  return out

def get_num_adjacent_occupied(seats, i, j):
  count = 0
  for  direction in directions:
    new_i = i + direction[0]
    new_j = j + direction[1]
    while new_i >= 0 and new_j >= 0 and new_i < len(seats) and new_j < len(seats[i]) and seats[new_i][new_j] == FLOOR:
      new_i += direction[0]
      new_j += direction[1]

    if new_i >= 0 and new_j >= 0 and new_i < len(seats) and new_j < len(seats[i]) and seats[new_i][new_j] == OCCUP:
      count += 1

  return count

def run():
  seats = []
  with open('../data/prob11.txt') as f:
    for line in f.readlines():
      this_row = []
      line = line.strip()
      for char in line:
        if char == 'L':
          this_row.append(EMPTY)
        elif char == '#':
          this_row.append(OCCUP)
        elif char == '.':
          this_row.append(FLOOR)
      seats.append(this_row)

  changed = True
  while changed:
    prev_seats = [row[:] for row in seats]
    changed = False

    for i in range(len(seats)):
      for j in range(len(seats[i])):
        if seats[i][j] != FLOOR:
          num_adj = get_num_adjacent_occupied(prev_seats, i, j)
          if seats[i][j] == EMPTY and num_adj == 0:
            seats[i][j] = OCCUP
            changed = True
          elif seats[i][j] == OCCUP and num_adj >= 5:
            changed = True
            seats[i][j] = EMPTY

  count = 0
  for row in seats:
    for seat in row:
      if seat == OCCUP:
        count += 1
  return count

if __name__ == '__main__':
  print(run())
