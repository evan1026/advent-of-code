required_fields = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def validate_field(key, value):
  try:
    if key == 'byr':
      return 1920 <= int(value) <= 2002
    elif key == 'iyr':
      return 2010 <= int(value) <= 2020
    elif key == 'eyr':
      return 2020 <= int(value) <= 2030
    elif key == 'hgt':
      if value[-2:] == 'in':
        return 59 <= int(value[:-2]) <= 76
      elif value[-2:] == 'cm':
        return 150 <= int(value[:-2]) <= 193
      else:
        return False
    elif key == 'hcl':
      if len(value) == 7 and value[0] == '#':
        int(value[1:], 16)  # If this doesn't throw, it is a valid hex string
        return True
      else:
        return False
    elif key == 'ecl':
      return value in eye_colors
    elif key == 'pid':
      if len(value) == 9:
        int(value)  # If this doesn't throw, it is a valid number
        return True
      else:
        return False
    else:
      return False
  except:
    return False

with open('../data/prob04.txt') as f:
  found_fields = set()
  valid = 0
  for line in f.readlines():
    if not line.strip():
      if found_fields == required_fields:
        valid += 1
      found_fields = set()
    else:
      pairs = line.strip().split()
      for pair in pairs:
        key, value = pair.split(':')
        if key in required_fields and validate_field(key, value):
          found_fields.add(key)
  if found_fields == required_fields:
    valid += 1
  print(valid)
