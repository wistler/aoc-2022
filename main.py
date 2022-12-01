import sys
import importlib

if __name__ == '__main__':
 
  try: 
    day = int(sys.argv[1]) 
  except:
    day = 1
  
  mod_name = 'Day.{}.main'.format(day)
  
  print('Running Module: {}'.format(mod_name))
  
  try:
    mod = importlib.import_module(mod_name)
  except Exception as e:
    print(e)
    exit(1)
    
  mod.Run()
  


