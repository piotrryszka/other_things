#!/usr/bin/python
import os

print(os.environ["PATH"])
print("Czy to działa?")

if os.path.isfile('.pythonrc.py'):
    exec(open('.pythonrc.py').read())

    