#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
import itertools
def findSum(a,k):
    i = 0 
    j = 1
    while i < len(a) - 1:
        if a[i] + a[j] ==k:
            return True
            break
        else:
            i += 1
            j += 1
    else:
        return False
if __name__ == '__main__':
	print("Enter list of numbers")
	a = list(map(int,input().rstrip().rsplit()))
	print("Enter sum to find in the list")
	k = int(input())
	result = findSum(a,k)
	print(result)
