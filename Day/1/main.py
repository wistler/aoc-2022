import math
import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def part1(x: list):
  cal = 0
  maxCal = 0
  for c in x:
    if c == 0:
      if maxCal < cal:
        maxCal = cal
      cal = 0
    else:
      cal += c
  return maxCal


def part1_tests():
    for test in [
            ({"x":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 24000),
        ]:
        inputs = test[0]
        expected = test[1]
        actual = part1(**inputs)
        if actual != expected:
            log("Test case {} = {}. Expected = {}".format(inputs, actual, expected))
            sys.exit(1)


def part2(x: list):
  cal = 0
  totals = []
  for c in x:
    if c == 0:
      totals.append(cal)
      cal = 0
    else:
      cal += c
  totals.append(cal)
  totals.sort(reverse=True)
  # log(totals)
  return sum(totals[0:3])


def part2_tests():
    for test in [
            ({"x":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 45000),
        ]:
        inputs = test[0]
        expected = test[1]
        actual = part2(**inputs)
        if actual != expected:
            log("Test case {} = {}. Expected = {}".format(inputs, actual, expected))
            sys.exit(1)


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      try:
        i = int(line)
      except:
        i = 0
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

