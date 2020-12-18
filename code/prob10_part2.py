joltages = []
with open('../data/prob10.txt') as f:
  for line in f.readlines():
    line = line.strip()
    joltages.append(int(line))

joltages = sorted(joltages)
joltages.insert(0, 0)
joltages.append(joltages[-1] + 3)

totals = {}
totals[0] = 1

for i in range(1, len(joltages)):
  total = 0
  j = i - 1
  while joltages[i] - joltages[j] <= 3 and j >= 0:
    total += totals[j]
    j -= 1
  totals[i] = total
print(totals[len(joltages) - 1])
