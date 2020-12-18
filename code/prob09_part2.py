import os
os.chdir(os.path.dirname(__file__))

from collections import deque

def is_sum(num, nums):
  # Since we know there's only 25, we don't need an efficient algorithm
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j and nums[i] + nums[j] == num:
        return True
  return False

def find_weakness(target, nums):
  upper = 0
  lower = 0

  current_total = sum(nums[lower:upper])
  while current_total != target:
    if current_total < target:
      upper += 1
    else:
      lower += 1

    current_total = sum(nums[lower:upper])

  range = nums[lower:upper]
  return max(range) + min(range)

def run():
  seen_nums = list()
  seen_nums_rolling = deque()
  with open('../data/prob09.txt') as f:
    for line in f.readlines():
      line = line.strip()
      line = int(line)
      if len(seen_nums_rolling) == 25:
        if not is_sum(line, list(seen_nums_rolling)):
          return find_weakness(line, seen_nums)
        seen_nums_rolling.popleft()
      seen_nums.append(line)
      seen_nums_rolling.append(line)

if __name__ == '__main__':
  print(run())
