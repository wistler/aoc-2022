import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def part1(li: list):
  global log_prefix
  log_prefix = "Part 1"
  exclusive = 0
  for a1,a2,b1,b2 in li:
    if (a1 <= b1 and a2 >= b2) or (b1<=a1 and b2>=a2):
      exclusive += 1
    
  return exclusive


def part2(li: list):
  global log_prefix
  log_prefix = "Part 2"
  overlaps = 0
  for a1,a2,b1,b2 in li:
    if (a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <=  b2):
      overlaps += 1
  
  return overlaps


def part1_tests():
  test_cases = [
    ({"li": [(2,4,6,8), (2,3,4,5), (5,7,7,9), (2,8,3,7), (6,6,4,6), (2,6,4,8)]}, 2),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2_tests():
  test_cases = [
    ({"li": [(2,4,6,8), (2,3,4,5), (5,7,7,9), (2,8,3,7), (6,6,4,6), (2,6,4,8)]}, 4),
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
      l1,l2 = line.split(',')
      a,b = map(int,l1.split('-'))
      c,d = map(int,l2.split('-'))
      input.append( (a,b,c,d) )
  
  log("Answer = {}".format(part1(input)))
  
  log("Answer = {}".format(part2(input)))

