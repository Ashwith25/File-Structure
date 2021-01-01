import os
import sys

path = sys.argv[1]

print(path)

os.chdir(path)
[print(files) for files in os.listdir()]