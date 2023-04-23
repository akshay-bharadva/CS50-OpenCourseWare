import sys


try:
  print(f"Hello, {sys.argv[1]}")
except:
  print("Too few argument")