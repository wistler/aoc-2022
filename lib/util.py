
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

