import random
str = input("Enter a string: ")
ans = random.choice(str)
print(ans) 
def hello(name):
    print('hello' , name)
op = input('Enter u r name:')
hello(op)    
from Calc import weight
kg =  int(input("ENter the number of grams:"))
ans = weight(kg)
print(kg , " grams is equal to ", ans , "kgs") 
