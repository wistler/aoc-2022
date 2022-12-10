import os

from lib.util import test
from lib.coord import Coord

mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


DIRS = {
  'R': Coord(0, 1),
  'U': Coord(1, 0),
  'L': Coord(0, -1),
  'D': Coord(-1, 0),
}


def unit(value):
  if value > 0:
    return 1
  if value < 0:
    return -1
  return 0


def plotGrid(pts: set):
  minPt = Coord(0,0)
  maxPt = Coord(0,0)
  for pt in pts:
    if minPt.x > pt.x:
      minPt.x = pt.x
    if minPt.y > pt.y:
      minPt.y = pt.y
    if maxPt.x < pt.x:
      maxPt.x = pt.x
    if maxPt.y < pt.y:
      maxPt.y = pt.y

  print(pts, minPt, maxPt)
  print()
  for x in range(maxPt.x, minPt.x-1, -1):
    for y in range(minPt.y, maxPt.y+1, 1):
      if Coord(x,y) in pts:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()


def follow(H1: Coord, T: Coord):
  T1 = T + Coord(0,0)
  tailMoves = abs(T.x - H1.x) > 1 or abs(T.y - H1.y) > 1
  if tailMoves:
    T1.x += unit(H1.x - T.x)
    T1.y += unit(H1.y - T.y)
  return T1


@test([
  ({'H': Coord(0,0), 'T': Coord(0,0), 'dir': 'R'}, (Coord(0,1), Coord(0,0))),
  ({'H': Coord(0,1), 'T': Coord(0,0), 'dir': 'R'}, (Coord(0,2), Coord(0,1))),
  ({'H': Coord(1,1), 'T': Coord(0,0), 'dir': 'R'}, (Coord(1,2), Coord(1,1))),
])
def move_1(H: Coord, T: Coord, dir):
  H1 = H + DIRS[dir]
  T1 = follow(H1, T)
  return(H1,T1)


@test([
  ({"inst": [
    ("R", 4),
    ("U", 4),
    ("L", 3),
    ("D", 1),
    ("R", 4),
    ("D", 1),
    ("L", 5),
    ("R", 2),
  ]}, 13)
])
def part1(inst: list):
  H = Coord(0,0)
  T = Coord(0,0)
  headVisited = set()
  tailVisited = set()
  
  headVisited.add(H)
  tailVisited.add(T)
  
  for dir, steps in inst:
    for _ in range(steps):
      H, T = move_1(H, T, dir)
      tailVisited.add(T)
      headVisited.add(H)
  
  # plotGrid(headVisited)
  # plotGrid(tailVisited)
  return len(tailVisited)


@test([
  ({"inst": [
    ('R', 5),
    ('U', 8),
    ('L', 8),
    ('D', 3),
    ('R', 17),
    ('D', 10),
    ('L', 25),
    ('U', 20),
  ]}, 36)
])
def part2(inst: list):
  H = Coord(0,0)
  knots = [Coord(0,0) for k in range(8)]
  T = Coord(0,0)
  rope = []
  
  rope.append(H)
  rope.extend(knots)
  rope.append(T)
  
  headVisited = set()
  tailVisited = set()
  
  headVisited.add(rope[0])
  tailVisited.add(rope[-1])
  
  for dir, steps in inst:
    for _ in range(steps):
      rope[0], rope[1] = move_1(rope[0], rope[1], dir)
      for i in range(1, len(rope)-1):
        rope[i+1] = follow(rope[i], rope[i+1])
      headVisited.add(rope[0])
      tailVisited.add(rope[-1])
  
  # plotGrid(headVisited)
  # plotGrid(tailVisited)
  return len(tailVisited)


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      dir, steps = line.split()
      input.append((dir, int(steps)))
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

