class Bag:
  def __init__(self, name):
    self.name = name
    self.connections = []

  def add_connection(self, other, count):
    self.connections.append(Connection(self, other, count))

  def __repr__(self):
    return 'Bag[name="' + self.name + '"]'

class Connection:
  def __init__(self, from_bag, to_bag, count):
    self.fr = from_bag
    self.to = to_bag
    self.count = count

def get_bag(name):
  if not name in bags:
    bags[name] = Bag(name)
  return bags[name]

def dfs_search(bag, bag_counts=None):
  if bag_counts is None:
    bag_counts = {}
  count = 1
  for connection in bag.connections:
    if connection.to not in bag_counts:
      dfs_search(connection.to, bag_counts)
    count += (connection.count * bag_counts[connection.to])
  bag_counts[bag] = count
  return count

bags = {}
with open('../data/prob07.txt') as f:
  for line in f.readlines():
    line = line.strip()
    words = line.replace(',', '').replace('.', '').split()

    this_bag = get_bag(words[0] + ' ' + words[1])

    words = words[4:]
    while words:
      count = words[0]
      if count == 'no':
        count = 0
      else:
        count = int(count)
      new_bag = get_bag(words[1] + ' ' + words[2])
      this_bag.add_connection(new_bag, count)
      words = words[4:]

shiny_gold_bag = bags['shiny gold']
count = dfs_search(shiny_gold_bag) - 1
print(count)
