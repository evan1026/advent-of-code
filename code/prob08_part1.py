class Instruction:
  def __init__(self, op, arg):
    self.op = op
    self.arg = arg

def run():
  instructions = []
  with open('../data/prob08.txt') as f:
    for line in f.readlines():
      line = line.strip()
      parts = line.split()
      op = parts[0]
      arg = int(parts[1])
      instructions.append(Instruction(op, arg))

  executed_instructions = set()
  pc = 0
  acc = 0
  while pc < len(instructions):
    if pc in executed_instructions:
      return acc

    executed_instructions.add(pc)
    inst = instructions[pc]
    if inst.op == 'nop':
      pass
    elif inst.op == 'acc':
      acc += inst.arg
    elif inst.op == 'jmp':
      pc += inst.arg - 1
    else:
      print('Invalid operation ' + inst.op + ' at line ' + str(pc))
      return -1
    pc += 1

if __name__ == '__main__':
  print(run())
