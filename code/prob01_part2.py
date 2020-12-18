import os
os.chdir(os.path.dirname(__file__))

def run():
  with open('../data/prob01.txt') as f:
    nums = [int(x) for x in f.readlines()]
  diffs = {}
  for num1 in nums:
    for num2 in nums:
      for num3 in nums:
        if num1 + num2 + num3 == 2020:
          return num1 * num2 * num3

if __name__ == '__main__':
  print(run())
