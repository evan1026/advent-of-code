class Instruction:
  def __init__(self, op, arg):
    self.op = op
    self.arg = arg

def check_for_loop(instructions):
  executed_instructions = set()
  pc = 0
  acc = 0
  while pc < len(instructions):
    if pc in executed_instructions:
      return True, acc

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
    pc += 1
  return False, acc

instructions = []
with open('../data/prob08.txt') as f:
  for line in f.readlines():
    line = line.strip()
    parts = line.split()
    op = parts[0]
    arg = int(parts[1])
    instructions.append(Instruction(op, arg))

for i in range(len(instructions)):
  new_instructions = instructions[:]

  inst = instructions[i]
  if inst.op == 'nop':
    new_op = 'jmp'
  elif inst.op == 'acc':
    continue
  elif inst.op == 'jmp':
    new_op = 'nop'
  else:
    print('Invalid operation ' + inst.op + ' at line ' + str(pc))
    continue

  new_instructions[i] = Instruction(new_op, instructions[i].arg)
  has_loop, acc_val = check_for_loop(new_instructions)
  if not has_loop:
    print(acc_val)
    break
