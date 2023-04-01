import subprocess
import  fileinput
import os
import sys


def extra_lines(var1):
        print("=======================================================================================")
        print(var1)
        print("=======================================================================================")


extra_lines("checking hostname")
s = subprocess.run(['hostname'],stdout=subprocess.PIPE, universal_newlines=True)
s = s.stdout
print(s)
