import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


@test([
  ({"st": "mjqjpqmgbljsphdztnvjfqwrcgsmlb"}, 7),
  ({"st": "bvwbjplbgvbhsrlpgdmjqwftvncz"}, 5),
  ({"st": "nppdvjthqldpwncqszvftbrmjlhg"}, 6),
  ({"st": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}, 10),
  ({"st": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}, 11),
])
def part1(st: str):
  for i in range(4,len(st)):
    if len(set(st[i-4:i])) == 4:
      return i
  return -1


@test([
    ({"st": "mjqjpqmgbljsphdztnvjfqwrcgsmlb"}, 19),
    ({"st": "bvwbjplbgvbhsrlpgdmjqwftvncz"}, 23),
    ({"st": "nppdvjthqldpwncqszvftbrmjlhg"}, 23),
    ({"st": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}, 29),
    ({"st": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}, 26),
])
def part2(st: str):
  for i in range(14,len(st)):
    if len(set(st[i-14:i])) == 14:
      return i
  return -1


def Run():
  input = ''
  with open(input_file) as fi:
    for line in fi.readlines():
      input += line.strip()
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

