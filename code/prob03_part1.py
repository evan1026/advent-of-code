import os
dirname = os.path.dirname(__file__)
if dirname:
  os.chdir(dirname)

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

def run():
  with open('../data/prob03.txt') as f:
    trees = [[(char == '#') for char in line.strip()] for line in f.readlines()]

  direction = Position(3, 1)
  pos = Position(0, 0)
  tree_count = 0
  while pos.y < len(trees):
    if get(trees, pos):
      tree_count += 1
    pos += direction
  return tree_count

if __name__ == '__main__':
  print(run())
