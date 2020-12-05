with open('../data/prob1.txt') as f:
  nums = [int(x) for x in f.readlines()]
diffs = {}
for num in nums:
  diffs[2020 - num] = num
for num in nums:
  if num in diffs:
    print(diffs[num] * num)
