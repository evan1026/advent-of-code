import os
os.chdir(os.path.dirname(__file__))

def get_count(answers):
  return len(set(''.join(answers)))

def run():
  with open('../data/prob06.txt') as f:
    curr_group = []
    sum = 0
    for line in f.readlines():
      line = line.strip()
      if line:
        curr_group.append(line)
      else:
        sum += get_count(curr_group)
        curr_group = []
    sum += get_count(curr_group)
  return sum

if __name__ == '__main__':
  print(run())
