import sys

def split_list(li: list, de: any):
  '''
  Generator to split a list by given delimiter
  '''
  sl = []
  for i in li:
    if i == de:
      yield sl
      sl = []
    else:
      sl.append(i)
  yield sl


def test(test_cases = []):
  def decorator(func):
    # print("Testing: ", func.__module__, '>', func.__name__ )
    
    log_prefix = func.__module__ + '.' + func.__name__ + ' |'
    
    for index, (inputs, expected) in enumerate(test_cases, start=1):
      actual = func(**inputs)
      if actual != expected:
        print(log_prefix, "Test case #{}, Actual = {}. Expected = {}\nAborted.".format(index, actual, expected))
        sys.exit(1)
    
    def inner(*args, **kwargs):
      return func(*args, **kwargs)
    return inner
  return decorator
