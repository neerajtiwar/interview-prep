from collections import OrderedDict
#Get the string
s = input("Enter String:")
substring = ""
a = [ ]
#find all possible substrings for a given string
for counter in range (0,len(s)):
    #d.update({s[counter:len(s)]: len(s[counter:len(s)])})
    substring = set(s[counter: len(s)])
    maxlen = len(substring)
    a.append(maxlen)
print(max(a))