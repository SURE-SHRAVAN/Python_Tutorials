#type of number


#integer

num = 9
print(type(num))


#float or decimal
num = 5.6
print(type(num))
#complex
num = 5+6j
print(type(num))
num = 9.99
from math import *
print(floor(num))
from array import *
arr = array("i",[])
n = int(input("Enter the  length of the array: "))
for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
 
print(arr)

