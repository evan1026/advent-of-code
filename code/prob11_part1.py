import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

# TODO needs optimization

EMPTY = 0
OCCUP = 1
FLOOR = 2

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
  for new_i in [i - 1, i, i + 1]:
    for new_j in [j - 1, j, j + 1]:
      if (new_i != i or new_j != j) and new_i >= 0 and new_j >= 0 and new_i < len(seats) and new_j < len(seats[i]) and seats[new_i][new_j] == OCCUP:
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
          elif seats[i][j] == OCCUP and num_adj >= 4:
            seats[i][j] = EMPTY
            changed = True

  count = 0
  for row in seats:
    for seat in row:
      if seat == OCCUP:
        count += 1
  return count

if __name__ == '__main__':
  print(run())
