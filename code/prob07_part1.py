class Bag:
  def __init__(self, name):
    self.name = name
    self.connections = []

  def add_connection(self, other):
    self.connections.append(other)

  def __repr__(self):
    return 'Bag[name="' + self.name + '"]'

def get_bag(name):
  if not name in bags:
    bags[name] = Bag(name)
  return bags[name]

def dfs_search(bag):
  holders = set()
  for connection in bag.connections:
    if connection not in holders:
      holders.add(connection)
      holders = holders.union(dfs_search(connection))
  return holders

bags = {}
with open('../data/prob07.txt') as f:
  for line in f.readlines():
    line = line.strip()
    words = line.replace(',', '').replace('.', '').split()

    this_bag = get_bag(words[0] + ' ' + words[1])

    words = words[4:]
    while words:
      count = words[0]
      new_bag = get_bag(words[1] + ' ' + words[2])
      new_bag.add_connection(this_bag)
      words = words[4:]

shiny_gold_bag = bags['shiny gold']
holders = dfs_search(shiny_gold_bag)
print(len(holders))
