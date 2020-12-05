required_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

with open('../data/prob4.txt') as f:
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
  print(valid)
