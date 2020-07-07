#=======LAMBDA FUNCTIONS========

#for defining a normal function we use 'def' Keyword ,
# for defining a lambda function we use lambda keyword

#syntax: lambda arguments: body

#eg. function for calculating sum of two numbers

#Approach 1. By using normal functions

def add(a,b):
     return a+b

print(add(2,3))
#Output: 5

#Approach 2. By Lambda functions

add = lambda a,b : a+b
print(add(2,3))
#Ouptut: 5

# lambda function for calculating square of a number
k = lambda a: a**2
print(k(6))

#Output: 36

# lambda function for finding greater among two numbers
g = lambda a,b:a if a>b else b
print(g(34,12))
#Output: 34

#=========FILTER function=========

#eg. extracting vowels from a string
#syntax: filter(function,iterable)

#defininig the function
def ext_vwls(string):
    for i in string:
        if i in 'aeiouAEIOU':
            return True
        else:
            return False

string='Python Filter Function'

print(filter(ext_vwls,string))
#solving above by lambda scroll to the end

#when you will run the aove code you will get something like this:
# <filter object at 0x0000014CBB115580>
#This shows that filter returns an iterator objec
#which makes the memory efficient

#Now,to get the desired result typecast it into list
print(list(filter(ext_vwls,string)))
# Output: ['o', 'i', 'e', 'u', 'i', 'o']

#This shows filter only returned those value for which condition was True in the function


#=========MAP Function=============
#syntax: map(function,*iterables)

#for eg. Adding the corresponding elements of two lists
a = [1,2,3,4,5,6]
b = [11,22,33,44,55,66]
c = list(map(lambda x,y:x+y,a,b))
print(c)

#Output: [12, 24, 36, 48, 60, 72]

#Note: map returns a map object
# so as to get the desired output we need to typecast it into list
#to undersstand the code check out README

#changing a string of numbers to list of numbers by map
print(list(map(int,'123456')))
#Output: [1, 2, 3, 4, 5, 6]
#here int is mapped to each element of list

#=========REDUCE Function==========
#syntax: reduce(function,iterable)

from functools import reduce
lst = [1,2,3,4,5]
a = reduce(lambda a,b:a*b,lst)
print(a)

#To understand the reduce checkout README


#=========short version of the filter code==========
string='Python Filter Function'
print(list(filter(lambda x: True if x in'aeiouAEIOU' else False,string)))