import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


@test([
  ({"li": [(2,4,6,8), (2,3,4,5), (5,7,7,9), (2,8,3,7), (6,6,4,6), (2,6,4,8)]}, 2),
])
def part1(li: list):
  exclusive = 0
  for a1,a2,b1,b2 in li:
    if (a1 <= b1 and a2 >= b2) or (b1<=a1 and b2>=a2):
      exclusive += 1
    
  return exclusive


@test([
  ({"li": [(2,4,6,8), (2,3,4,5), (5,7,7,9), (2,8,3,7), (6,6,4,6), (2,6,4,8)]}, 4),
])
def part2(li: list):
  overlaps = 0
  for a1,a2,b1,b2 in li:
    if (a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <=  b2):
      overlaps += 1
  
  return overlaps


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      l1,l2 = line.split(',')
      a,b = map(int,l1.split('-'))
      c,d = map(int,l2.split('-'))
      input.append( (a,b,c,d) )
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

