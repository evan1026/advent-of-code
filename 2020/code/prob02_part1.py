import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

def run():
  with open('../data/prob02.txt') as f:
    valid_count = 0
    for line in f.readlines():
      if line.strip():
        count, letter, password = line.split()

        min_count, max_count = count.split("-")
        min_count = int(min_count)
        max_count = int(max_count)

        letter = letter[:-1]

        count = 0
        for char in password:
          if char == letter:
            count += 1
        if min_count <= count <= max_count:
          valid_count += 1
    return valid_count

if __name__ == '__main__':
  print(run())
