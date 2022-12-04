import sys
import os


global log_prefix
log_prefix = ""
mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')

def log(message: str):
  print('{} | {}'.format(log_prefix, message))


def pri(c):
  if c.islower():
    pri = ord(c) - ord('a') + 1
  else:
    pri = ord(c) - ord('A') + 27
  return pri

def part1(li: list):
  global log_prefix
  log_prefix = "Part 1"
  sum = 0
  for line in li:
    c1 = set(line[0:len(line)//2])
    c2 = set(line[len(line)//2:])
    shared = c1.intersection(c2)
    assert(len(shared) == 1)
    c = shared.pop()
    sum += pri(c)
  return sum


def part2(li: list):
  global log_prefix
  log_prefix = "Part 2"
  sum = 0
  for i in range(0,len(li),3):
    shared = set(li[i])
    shared.intersection_update(li[i+1])
    shared.intersection_update(li[i+2])
    try:
      assert(len(shared) == 1)
    except:
      print(shared, li[i], li[i+1], li[i+2])
      exit(2)
    c = shared.pop()
    sum += pri(c)
  return sum


def part1_tests():
  test_cases = [
    ({"li": [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
      ]}, 157),
  ]
  for index, (inputs, expected) in enumerate(test_cases, start=1):
    actual = part1(**inputs)
    if actual != expected:
      log("Test case #{}, Actual = {}. Expected = {}".format(index, actual, expected))
      sys.exit(1)


def part2_tests():
  test_cases = [
    ({"li": [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
      ]}, 70),
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
      input.append(line.strip())
  
  log("Answer = {}".format(part1(input)))
  
  log("Answer = {}".format(part2(input)))

