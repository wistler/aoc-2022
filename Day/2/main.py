import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))

WINS = [
  ('A','Y'), 
  ('B','Z'), 
  ('C','X')
]

DRAWS = [
  ('A', 'X'),
  ('B', 'Y'),
  ('C', 'Z')
]

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

def part1(li: list):
  score = 0
  for pair in li:
    round_score = VALUE[pair[1]] + (3 if pair in DRAWS else 6 if pair in WINS else 0)
    score += round_score
  return score


def part1_tests():
  test_cases = [
    ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 15),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2(li: list):
  score = 0
  for pair in li:
    if pair[1] == 'X':
      hand = LOSE_SYMBOL[pair[0]]
      round_score = VALUE[hand]
    elif pair[1] == 'Z':
      hand = WIN_SYMBOL[pair[0]]
      round_score = 6 + VALUE[hand]
    else:
      hand = DRAW_SYMBOL[pair[0]]
      round_score = 3 + VALUE[hand]
    score += round_score
  return score


def part2_tests():
  test_cases = [
    ({"li": [('A','Y'), ('B','X'), ('C','Z')]}, 12),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part2(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      [a,x] = line.split()
      i = (a,x)
      input.append(i)
  
  global log_prefix
  log_prefix = "Part 1"
  part1_tests()
  log("Answer = {}".format(part1(input)))
  
  log_prefix = "Part 2"
  part2_tests()
  log("Answer = {}".format(part2(input)))


if __name__ == '__main__':
  Run()

