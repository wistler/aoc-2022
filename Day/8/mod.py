import os

from lib.util import test


mydir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(mydir, 'input')


@test([
  ({"grid": [
    list(map(int, "30373")),
    list(map(int, "25512")),
    list(map(int, "65332")),
    list(map(int, "33549")),
    list(map(int, "35390")),
  ]}, 21)
])
def part1(grid: list):
  visible = 0
  for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
      myHeight = grid[i][j]
      hiddenFromTop = len(list(filter(myHeight.__le__, [grid[k][j] for k in range(0, i)]))) > 0
      hiddenFromBottom = len(list(filter(myHeight.__le__, [grid[k][j] for k in range(i+1, len(grid))]))) > 0
      hiddenFromLeft = len(list(filter(myHeight.__le__, [grid[i][l] for l in range(0, j)]))) > 0
      hiddenFromRight = len(list(filter(myHeight.__le__, [grid[i][l] for l in range(j+1, len(grid[0]))]))) > 0
      
      isVisible = not hiddenFromTop or not hiddenFromLeft or not hiddenFromBottom or not hiddenFromRight
      if isVisible:
        visible += 1
  return visible


@test([
  ({"grid": [
    list(map(int, "30373")),
    list(map(int, "25512")),
    list(map(int, "65332")),
    list(map(int, "33549")),
    list(map(int, "35390")),
  ]}, 8)
])
def part2(grid: list):
  def filter(cond, iter):
    for it in iter:
      if cond(it):
        yield it  # shorter trees
      else:
        yield it  # the tree blocking the view
        break
      
  maxScore = 0
  scores = [[0 for _ in range(len(grid[0])) ] for _ in range(len(grid))]
  
  for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
      myHeight = grid[i][j]
      topView = list(filter(myHeight.__gt__, [grid[k][j] for k in range(i-1, -1, -1)]))
      bottomView = list(filter(myHeight.__gt__, [grid[k][j] for k in range(i+1, len(grid))]))
      leftView = list(filter(myHeight.__gt__, [grid[i][l] for l in range(j-1, -1, -1)]))
      rightView = list(filter(myHeight.__gt__, [grid[i][l] for l in range(j+1, len(grid[0]))]))
      
      score = len(topView) * len(bottomView) * len(leftView) * len(rightView)
      scores[i][j] = score
      maxScore = max(score, maxScore)
  
  return maxScore



def Run():
  input = []
  with open(input_file) as fi:
    for line in fi.readlines():
      input.append(list(map(int,line.strip())))
  
  print("Part1 Answer = {}".format(part1(input)))
  
  print("Part2 Answer = {}".format(part2(input)))

