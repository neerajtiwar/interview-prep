#problem to count of filename having ERROR in a log file
#like below lines
#477123675|ERROR|handler.cpp|127|findHandlers|Division by zero
#1477997395|ERROR|nw_tx.cpp|1110|getHandlers|Array out of bounds
#1477997395|ERROR|nw_tx.cpp|1110|getHandlers|Array out of bounds
#example output:
#handler.cpp 1
#nw_tx.cpp 2


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
