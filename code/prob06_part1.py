def get_count(answers):
  return len(set(''.join(answers)))

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
print(sum)
