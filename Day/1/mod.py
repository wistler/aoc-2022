import sys
import os

from lib.util import split_list


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def part1(li: list):
  global log_prefix
  log_prefix = "Part 1"
  return max(map(sum, split_list(li, 0)))


def part2(li: list):
  global log_prefix
  log_prefix = "Part 1"
  return sum(sorted(map(sum, split_list(li, 0)), reverse=True)[0:3])


def part1_tests():
  test_cases = [
    ({"li":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 24000),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2_tests():
  test_cases = [
    ({"li":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 45000),
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
      try:
        i = int(line)
      except:
        i = 0
      input.append(i)
  
  log("Answer = {}".format(part1(input)))
  
  log("Answer = {}".format(part2(input)))

