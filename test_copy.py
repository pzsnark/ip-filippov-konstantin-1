# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil
import sys

path = sys.argv[0]
path2 = path[:-3]
shutil.copy(path, path2 + "_copy.py")
