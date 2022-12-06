import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


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


@test([
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
])
def part1(text: list):
  stacks, steps = parse_input(text)
  for n,x,y in steps:
    for _ in range(0,n):
      stacks[y-1].append(stacks[x-1].pop())
  return ''.join([st[-1] for st in stacks])


@test([
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
])
def part2(text: list):
  stacks, steps = parse_input(text)
  for n,x,y in steps:
    stacks[x-1], move = stacks[x-1][:-n], stacks[x-1][-n:]
    stacks[y-1].extend(move)
    
  return ''.join([st[-1] for st in stacks])


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append( line )
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

