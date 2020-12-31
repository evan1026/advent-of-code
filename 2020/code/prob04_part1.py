import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

def run():
  required_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

  with open('../data/prob04.txt') as f:
    found_fields = set()
    valid = 0
    for line in f.readlines():
      if not line.strip():
        if found_fields == required_fields:
          valid += 1
        found_fields = set()
      else:
        pairs = line.split()
        for pair in pairs:
          key, value = pair.split(':')
          if key in required_fields:
            found_fields.add(key)
    return valid

if __name__ == '__main__':
  print(run())
