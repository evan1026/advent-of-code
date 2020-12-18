def run():
  with open('../data/prob01.txt') as f:
    nums = [int(x) for x in f.readlines()]
  diffs = {}
  for num in nums:
    diffs[2020 - num] = num
  for num in nums:
    if num in diffs:
      return diffs[num] * num

if __name__ == '__main__':
  print(run())
