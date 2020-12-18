from collections import deque

def is_sum(num, nums):
  # Since we know there's only 25, we don't need an efficient algorithm
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j and nums[i] + nums[j] == num:
        return True
  return False

seen_nums = deque()
with open('../data/prob09.txt') as f:
  for line in f.readlines():
    line = line.strip()
    if len(seen_nums) == 25:
      if not is_sum(int(line), list(seen_nums)):
        print(line)
        break
      seen_nums.popleft()
    seen_nums.append(int(line))

