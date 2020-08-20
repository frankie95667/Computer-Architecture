#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) != 2:
    print("usage: ls8.py filename")

else:
    try:
        filename = sys.argv[1]
        cpu.load(filename)
        cpu.run()
    except FileNotFoundError:
        print(f"filename \"{sys.argv[1]}\" not found!")