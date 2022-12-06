import os

from lib.util import split_list, test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


@test([
  ({"li":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 24000),
])
def part1(li: list):
  return max(map(sum, split_list(li, 0)))


@test([
  ({"li":[1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000]}, 45000),
])
def part2(li: list):
  return sum(sorted(map(sum, split_list(li, 0)), reverse=True)[0:3])


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      try:
        i = int(line)
      except:
        i = 0
      input.append(i)
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

