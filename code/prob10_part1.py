from collections import defaultdict

def run():
  joltages = []
  with open('../data/prob10.txt') as f:
    for line in f.readlines():
      line = line.strip()
      joltages.append(int(line))

  joltages = sorted(joltages)
  differences = defaultdict(lambda: 1)
  for i in range(1, len(joltages)):
    differences[joltages[i] - joltages[i - 1]] += 1
  return differences[1] * differences[3]

if __name__ == '__main__':
  print(run())
