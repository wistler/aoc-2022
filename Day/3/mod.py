import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


def pri(c):
  if c.islower():
    pri = ord(c) - ord('a') + 1
  else:
    pri = ord(c) - ord('A') + 27
  return pri

@test([
  ({"li": [
      "vJrwpWtwJgWrhcsFMMfFFhFp",
      "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
      "PmmdzqPrVvPwwTWBwg",
      "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
      "ttgJtRGJQctTZtZT",
      "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]}, 157),
])
def part1(li: list):
  sum = 0
  for line in li:
    c1 = set(line[0:len(line)//2])
    c2 = set(line[len(line)//2:])
    shared = c1.intersection(c2)
    assert(len(shared) == 1)
    c = shared.pop()
    sum += pri(c)
  return sum


@test([
  ({"li": [
      "vJrwpWtwJgWrhcsFMMfFFhFp",
      "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
      "PmmdzqPrVvPwwTWBwg",
      "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
      "ttgJtRGJQctTZtZT",
      "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]}, 70),
])
def part2(li: list):
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


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append(line.strip())
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

