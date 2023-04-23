# before exec of this program
# you should have installed cowsay on local machine
# pip install cowsay

import cowsay
import sys

if len(sys.argv) < 2:
  sys.exit("Too few arguments")
elif len(sys.argv) > 2:
  sys.exit("Too many arguments")
else:
  cowsay.cow(f"Hello, {sys.argv[1]}")