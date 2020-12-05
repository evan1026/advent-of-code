class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Position(self.x + other.x, self.y + other.y)

  def __repl__(self):
    return '(%d, %d)' % (self.x, self.y)

  def __str__(self):
    return self.__repl__()


def get(trees, pos):
  return trees[pos.y][pos.x % len(trees[pos.y])]

with open('../data/prob3.txt') as f:
  trees = [[(char == '#') for char in line.strip()] for line in f.readlines()]

total = 1
for direction in [Position(1,1), Position(3,1), Position(5,1), Position(7,1), Position(1,2)]:
  pos = Position(0, 0)
  tree_count = 0
  while pos.y < len(trees):
    if get(trees, pos):
      tree_count += 1
    pos += direction

  total *= tree_count

print(total)
