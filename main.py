import os
from os import walk
from pathlib import Path


for path, dirs, files in os.walk("."):
    print(path)
    for f in files:
        print(f)