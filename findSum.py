#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

def findSum(a,k):
	first = 0
	last = len(a) - 1
	foundSum = 0

	while first < last:
		foundSum = a[first] + a[last]
		if (foundSum == k):
			return True
		else:
			first += 1
		return False
		
if __name__ == '__main__':
	print("Enter list of numbers")
	a = list(map(int,input().rstrip().rsplit()))
	print("Enter sum to find in the list")
	k = int(input())
	result = findSum(a,k)
	print(result)