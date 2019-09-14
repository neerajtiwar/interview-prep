def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < len(c) - 1:
        if (c[::3] == 0 and ):
            jump += 1
            i = i + 2
        else:
            jump = jump + 1
            i = i + 1
return jump
if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
