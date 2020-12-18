import os
os.chdir(os.path.dirname(__file__))

def run():
  with open('../data/prob02.txt') as f:
    valid_count = 0
    for line in f.readlines():
      if line.strip():
        positions, letter, password = line.split()

        pos1, pos2 = positions.split("-")
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1

        letter = letter[:-1]

        if (password[pos1] == letter) != (password[pos2] == letter):  # not equal is effectively xor
          valid_count += 1
    return valid_count

if __name__ == '__main__':
  print(run())
