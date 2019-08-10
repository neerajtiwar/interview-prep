
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl = 0
    val = 0
    for i in s:
        if i == "U":
            lvl += 1
        if i == "D":
            lvl -= 1
        if (lvl == 0 and i == "U"):
            val += 1
    return val
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
