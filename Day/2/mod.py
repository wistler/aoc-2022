import os

from lib.util import test

mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


VALUE = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

WIN_SYMBOL = {
  'A': 'Y',
  'B': 'Z',
  'C': 'X'
}

LOSE_SYMBOL = {
  'A': 'Z',
  'B': 'X',
  'C': 'Y'
}

DRAW_SYMBOL = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z'
}

COND_MAP = {
  'X': (0, LOSE_SYMBOL),
  'Y': (3, DRAW_SYMBOL),
  'Z': (6, WIN_SYMBOL),
}

@test([
  ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 15),
])
def part1(li: list):
  scores = []
  for them,me in li:
    points = (3 if DRAW_SYMBOL[them] == me else 6 if WIN_SYMBOL[them] == me else 0)
    scores.append(points + VALUE[me])
  return sum(scores)


@test([
  ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 12),
])
def part2(li: list):
  scores = []
  for them,cond in li:
    points, sym_map = COND_MAP[cond]
    me = sym_map[them]
    scores.append( points + VALUE[me] )
  return sum(scores)


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append( tuple(line.split()) )
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

