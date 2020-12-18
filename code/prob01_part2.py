with open('../data/prob01.txt') as f:
  nums = [int(x) for x in f.readlines()]
diffs = {}

def run():
  for num1 in nums:
    for num2 in nums:
      for num3 in nums:
        if num1 + num2 + num3 == 2020:
          print(num1 * num2 * num3)
          return

run()
