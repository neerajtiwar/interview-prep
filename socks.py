#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(ar):
    pairs = 0
    count = Counter(ar)
    for i in count.values():
        pairs = pairs + i//2
    return pairs

if __name__ == '__main__': 
    print("Enter array items")
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)
    
    print(result)
