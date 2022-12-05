import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def parse_input(text: list):
  inst = False
  raw_stacks = []
  instructions = []
  for line in text:
    line = line.strip('\n')
    if line[0:4] == " 1  ":  # container labels
      inst = True
      continue
    if len(line.strip()) == 0:
      continue
    if not inst:
      cr = list(line[1::4])
      raw_stacks.append(cr)  # TODO zip all elements 
    else:
      assert line.startswith("move ")
      [_,n,_,x,_,y] = line.split()
      instructions.append((int(n),int(x),int(y)))
  
  flipped_stacks = map(list,zip(*raw_stacks[::-1]))  # invert the stacks from bottom to top
  stacks = [[i for i in st if i != ' '] for st in flipped_stacks]  # remove empty containers
  return stacks, instructions


def part1(text: list):
  global log_prefix
  log_prefix = "Part 1"
  stacks, steps = parse_input(text)
  for n,x,y in steps:
    for _ in range(0,n):
      stacks[y-1].append(stacks[x-1].pop())
  return ''.join([st[-1] for st in stacks])


def part2(text: list):
  global log_prefix
  log_prefix = "Part 2"
  stacks, steps = parse_input(text)
  for n,x,y in steps:
    stacks[x-1], move = stacks[x-1][:-n], stacks[x-1][-n:]
    stacks[y-1].extend(move)
    
  return ''.join([st[-1] for st in stacks])


def part1_tests():
  test_cases = [
    ({"text": [
      "    [D]    ",
      "[N] [C]    ",
      "[Z] [M] [P]",
      " 1   2   3 ",
      "",
      "move 1 from 2 to 1",
      "move 3 from 1 to 3",
      "move 2 from 2 to 1",
      "move 1 from 1 to 2",
  ]}, "CMZ"),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2_tests():
  test_cases = [
    ({"text": [
      "    [D]    ",
      "[N] [C]    ",
      "[Z] [M] [P]",
      " 1   2   3 ",
      "",
      "move 1 from 2 to 1",
      "move 3 from 1 to 3",
      "move 2 from 2 to 1",
      "move 1 from 1 to 2",
  ]}, "MCD"),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part2(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def Test():
  part1_tests()
  part2_tests()


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append( line )
  
  log("Answer = {}".format(part1(input)))
  
  log("Answer = {}".format(part2(input)))

