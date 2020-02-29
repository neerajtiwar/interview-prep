from collections import Counter
mydict = {}
arr = []
with open('/Users/b0210216/test', mode='r') as f:
    for line in f.readlines():
        if 'ERROR' in line:
            arr.append(line.split('|') [2])
    for filename in arr:
        if filename in mydict:
            mydict[filename] += 1
        else:
            mydict[filename] = 1
for i in mydict.keys():
    print(i,mydict[i])
