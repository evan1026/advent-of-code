with open('../data/prob1.txt') as f:
  nums = [int(x) for x in f.readlines()]
diffs = {}

for num1 in nums:
  for num2 in nums:
    for num3 in nums:
      if num1 + num2 + num3 == 2020:
        print(num1 * num2 * num3)
