import os
import sys
from collections import Counter

def binarySearch(a,item):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high) // 2
		if a[mid] == item:
			return mid
		elif item < a[mid]:
			high = mid - 1
		else:
			low = mid + 1


if __name__ == '__main__':
	
	a = list(map(int,input().rstrip().rsplit()))
	item = int(input())
	result = binarySearch(a,item)
	print(result)