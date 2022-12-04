import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def part1(li: list):
  totalCal = 0
  maxCal = 0
  for c in li:
    if c == 0:
      if maxCal < totalCal:
        maxCal = totalCal
      totalCal = 0
    else:
      totalCal += c
      
  # one last time
  if maxCal < totalCal:
    maxCal = totalCal
  
  return maxCal


def part1_tests():
  test_cases = [
    ({"li":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 2400),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2(li: list):
  totalCal = 0
  totals = []
  for c in li:
    if c == 0:
      totals.append(totalCal)
      totalCal = 0
    else:
      totalCal += c
  
  if (totalCal > 0):
    totals.append(totalCal)
  
  totals.sort(reverse=True)
  return sum(totals[0:3])


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
  global log_prefix
  
  log_prefix = "Part 1"
  part1_tests()
  
  log_prefix = "Part 2"
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
  
  global log_prefix
  log_prefix = "Part 1"
  log("Answer = {}".format(part1(input)))
  
  log_prefix = "Part 2"
  log("Answer = {}".format(part2(input)))


if __name__ == '__main__':
  Run()

