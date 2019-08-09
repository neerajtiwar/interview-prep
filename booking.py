import os,sys
from collections import Counter

def getDict(mylist):
    mydict = {}
    for id,name,city in mylist:
        mydict.setdefault(city,[]).append(name)
    return mydict

if __name__ == '__main__':
    mylist = [('1234', 'Sheraton', 'Amsterdam'),
 ('1000', 'Sheraton', 'Buenos Aires'),
 ('1001', 'Hilton', 'Amsterdam'),
 ('1002', 'Royal Palace', 'Bogota'),
 ('1003', 'Hilton', 'Amsterdam'),
 ('1004', 'Sheraton', 'Buenos Aires'),
 ('1005', 'Sheraton', 'Buenos Aires')]
    
    # Convert list of tuples into dictionary
    mydict = getDict(mylist)
    for city,hotel in mydict.items():
        c =  Counter(hotel)
        for key,value in c.items():
            if value >= 3:
                print(city)
