#!/usr/bin/env python3
import shutil
import os

cwd = os.path.realpath(__file__)
print(cwd)

total, used, free = shutil.disk_usage(cwd)

print(f'Total: {(total / (1024**3)):.2f} GB')
print(f'Used: {(used / (1024**3)):.2f} GB')
print(f'Free: {(free / (1024**3)):.2f} GB')

