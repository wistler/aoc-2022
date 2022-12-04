import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))

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

def part1(li: list):
  global log_prefix
  log_prefix = "Part 1"
  scores = []
  for them,me in li:
    points = (3 if DRAW_SYMBOL[them] == me else 6 if WIN_SYMBOL[them] == me else 0)
    scores.append(points + VALUE[me])
  return sum(scores)


def part2(li: list):
  global log_prefix
  log_prefix = "Part 2"
  scores = []
  for them,cond in li:
    points, sym_map = COND_MAP[cond]
    me = sym_map[them]
    scores.append( points + VALUE[me] )
  return sum(scores)


def part1_tests():
  test_cases = [
    ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 15),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2_tests():
  test_cases = [
    ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 12),
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
      input.append( tuple(line.split()) )
  
  log("Answer = {}".format(part1(input)))
  
  log("Answer = {}".format(part2(input)))

