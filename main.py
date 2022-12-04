import sys
import importlib

if __name__ == '__main__':
  try:
    day = int(sys.argv[1]) 
  except:
    day = 1
  mod_name = 'Day.{}.mod'.format(day)
  try:
    mod = importlib.import_module(mod_name)
    print('Testing Module: {}'.format(mod_name))
    mod.Test()
    print('Running Module: {}'.format(mod_name))
    mod.Run()
  except Exception as e:
    print(e)
    exit(1)


