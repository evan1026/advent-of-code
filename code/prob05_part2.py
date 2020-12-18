import os
os.chdir(os.path.dirname(__file__))

def get_seat_id(seat):
  bin_seat = seat.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
  return int(bin_seat, 2)

def run():
  with open('../data/prob05.txt') as f:
    seen = set()
    for line in f.readlines():
      line = line.strip()
      seat_id = get_seat_id(line)
      seen.add(seat_id)

  for i in range(1024):
    if not i in seen and i + 1 in seen and i - 1 in seen:
        return i

if __name__ == '__main__':
  print(run())
