import math
import sys
import os


global log_prefix
log_prefix = ""

def log(message: str):
  print('{} | {}'.format(log_prefix, message))

def part1(x: int, y: int):
  return x + y


def Run():
    mydir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(mydir, 'input')

    global log_prefix
    log_prefix = "Part 1"
    for test in [
            ({"x":1, "y":2}, 3),
        ]:
        inputs = test[0]
        expected = test[1]
        actual = part1(**inputs)
        if actual != expected:
            log("Test case {} = {}. Expected = {}".format(inputs, actual, expected))
            sys.exit(1)

    with open(input_file) as input:
        ans = 0
        for line in input.readlines():
            i = int(line)
            ans += part1(i, i)
    
    log("Answer = {}\n".format(ans))

if __name__ == '__main__':
  Run()

