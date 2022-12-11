import os
from pprint import pprint

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


def read_file(f):
  with open(f) as fi:
    return fi.readlines()


def make_operator(op: str, term: str):
  if op == '+':
    return lambda item: (item + int(term))
  elif op == '*':
    if term == 'old':
      return lambda item: (item * item)
    else:
      return lambda item: (item * int(term))
  
  raise "Unknown Operator: " + op


def add_relief(func):
  return lambda item: func(item) // 3


def make_test(term: int):
  return lambda item: item % term == 0

monkeys = {
  # 0: { 'items': [], 'op': None, 'test': None, 'true': 0, 'false': 0 }
}  

def product(li: list):
  p = 1
  for it in li:
    p *= it
  return p


@test([
  ({ 'inst': read_file(input_file + '.test') }, 10605)
])
def part1(inst: list):
  monkeys = []
  m = None
  for li in inst:
    li = li.strip()
    if li.startswith('Monkey '):
      if m != None:
        monkeys.append(m)
      m = {}
      m['activity'] = 0
    
    if li.startswith('Starting items:'):
      m['items'] = list(map(int, li.split(':')[1].split(',')))
    elif li.startswith('Operation:'):
      oper = li.split('=')[1].split()
      m['op'] = add_relief(make_operator(oper[1], oper[2]))
    elif li.startswith('Test:'):
      term = li.split()[-1]
      m['test'] = make_test(int(term))
    elif li.startswith('If true:'):
      m['true'] = int(li.split()[-1])
    elif li.startswith('If false:'):
      m['false'] = int(li.split()[-1])
    
  monkeys.append(m)

  for round in range(1,21):
    for m in monkeys:
      m['activity'] += len(m['items'])
      while len(m['items']) > 0:
        it = m['items'].pop(0)
        new_it = m['op'](it)
        mi = m['true'] if m['test'](new_it) else m['false']
        monkeys[mi]['items'].append(new_it)
    
    # print("After round {}:".format(round))
    # for i, m in enumerate(monkeys):
    #   print("Monkey {}: {}".format(i, ', '.join(map(str, m['items']))))
    # print()
    
  # pprint(monkeys)
  return product(sorted([m['activity'] for m in monkeys], reverse=True)[0:2])


@test([
  # ({ 'inst': read_file(input_file + '.test') }, 2713310158)
])
def part2(inst: list):
  monkeys = []
  m = None
  for li in inst:
    li = li.strip()
    if li.startswith('Monkey '):
      if m != None:
        monkeys.append(m)
      m = {}
      m['activity'] = 0
    
    if li.startswith('Starting items:'):
      m['items'] = list(map(int, li.split(':')[1].split(',')))
    elif li.startswith('Operation:'):
      oper = li.split('=')[1].split()
      m['op'] = make_operator(oper[1], oper[2])
    elif li.startswith('Test:'):
      term = li.split()[-1]
      m['test'] = make_test(int(term))
    elif li.startswith('If true:'):
      m['true'] = int(li.split()[-1])
    elif li.startswith('If false:'):
      m['false'] = int(li.split()[-1])
    
  monkeys.append(m)
  
  for round in range(1,10001):
    for m in monkeys:
      m['activity'] += len(m['items'])
      while len(m['items']) > 0:
        it = m['items'].pop(0)
        new_it = m['op'](it)
        mi = m['true'] if m['test'](new_it) else m['false']
        monkeys[mi]['items'].append(new_it)
    
    if round % 1000 == 0:
      print("After round {}:".format(round))
      for i, m in enumerate(monkeys):
        print("Monkey {} inspected items {} times.".format(i, m['activity']))
      print()
    
  # pprint(monkeys)
  return product(sorted([m['activity'] for m in monkeys], reverse=True)[0:2])

def Run():
  input = read_file(input_file)
  
  print("Part1 Answer = {}".format(part1(input)))
  # print("Part2 Answer = {}".format(part2(input)))

