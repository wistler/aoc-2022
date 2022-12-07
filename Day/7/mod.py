import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


def mkfile(path, file, size, DIRS):
  for i in range(0, len(path)):
    dir_path = '/'.join(path[:i+1])
    if dir_path not in DIRS:
      DIRS[dir_path] = 0
    DIRS[dir_path] += size
  DIRS['/'] += size


def process(current: str, cwd: list, DIRS):
  words = current.split()
  if words[0] == '$':  # command
    cmd =  words[1]
    if cmd == 'cd':
      dir = words[2]
      if dir == '/':
        cwd.clear()
      elif dir == '..':
        cwd.pop()
      else:
        cwd.append(dir)
      return (cwd)
  else:
    if words[0] == 'dir':
      pass
    else:
      mkfile(cwd, words[1], int(words[0]), DIRS)
  return (cwd)


TEST_SETUP = [
  "$ cd /",
  "$ ls",
  "dir a",
  "14848514 b.txt",
  "8504156 c.dat",
  "dir d",
  "$ cd a",
  "$ ls",
  "dir e",
  "29116 f",
  "2557 g",
  "62596 h.lst",
  "$ cd e",
  "$ ls",
  "584 i",
  "$ cd ..",
  "$ cd ..",
  "$ cd d",
  "$ ls",
  "4060174 j",
  "8033020 d.log",
  "5626152 d.ext",
  "7214296 k",
]

@test([({"st": TEST_SETUP}, 95437)])
def part1(st: str):
  DIRS = {'/': 0}
  cwd = []
  for line in st:
    process(line, cwd, DIRS)
  big_dirs = sorted([ds for ds in DIRS.values() if ds <= 100000])
  return sum(big_dirs)


@test([({"st": TEST_SETUP}, 24933642)])
def part2(st: str):
  DIRS = {'/': 0}
  cwd = []
  for line in st:
    process(line, cwd, DIRS)
  
  total_size = DIRS['/']
  
  DISK_SIZE = 70_000_000
  SPACE_REQ = 30_000_000
  unused_space = DISK_SIZE - total_size
  space_needed = SPACE_REQ - unused_space
  sorted_dirs = sorted(DIRS.values())
  
  target = list(filter(space_needed.__le__, sorted_dirs))[0]
  return target


def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append(line.strip())
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

