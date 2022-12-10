import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


def read_file(f):
  with open(f) as fi:
    return fi.readlines()


def gen_timeline(inst: list):
  X = 1
  cycle = 1
  timeline = [(cycle, X)]
  
  for ins in inst:
    cmd = ins.split()
    if cmd[0] == 'noop':
      cycle += 1
    elif cmd[0] == 'addx':
      cycle += 2
      X += int(cmd[1])
    timeline.append((cycle, X))
    
  return timeline


@test([
  ({ 'inst': read_file(input_file + '.test') }, 13140)
])
def part1(inst: list):
  INSPECT_CYCLES=[20, 60, 100, 140, 180, 220]
  timeline = gen_timeline(inst)
  
  ti = 0
  signals = []
  for icy in INSPECT_CYCLES:
    while timeline[ti][0] <= icy:
      ti += 1
    signals.append(icy * timeline[ti-1][1])
  
  # print(signals)
  return sum(signals)


@test([
  ({ 'inst': read_file(input_file + '.test') }, None)
])
def part2(inst: list):
  timeline = gen_timeline(inst)
  
  mon = []
  cy = 1
  ti = 0
  for _ in range(0, 6):
    mon.append('')
    for y in range(0, 40):
      while timeline[ti][0] <= cy:
        ti += 1
      
      sprit_mid = timeline[ti-1][1]
      lit = y >= sprit_mid - 1 and y <= sprit_mid + 1
      px = '#' if lit else '.'
      mon[-1] += px
      cy += 1
  
  for line in mon:
    print(line)
    
  return None


def Run():
  input = read_file(input_file)
  
  print("Part1 Answer = {}".format(part1(input)))
  print("Part2 Answer = {}".format(part2(input)))

