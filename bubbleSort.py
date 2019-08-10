#!/bin/python3
import os,sys
def bubbleSort(a):
   for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print(a)


if __name__ == '__main__':
    print("Enter list of numbers")
    a = list(map(int,input().rstrip().rsplit()))
    result = bubbleSort(a)
    print(result)
