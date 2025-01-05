def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def power(a,b):
    return a**b
def sqr(a):
    return a**2
def eod(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def prime(num):
    if num % 3 != 0 and num % 2 == 1 :
        print("Prime")
    else:
        print("Composite")
def  circle_area(r):
    area = 3.14*r**2
    return area
def square_area(side):
    area = side**2
    return area
def rectangle_area(l,w):
    area = l*w
    return area
def triangle_area(b,h):
    area = 0.5*b*h
    return area
def SI(p,t,r):
    return (p*t*r)/100     
def weight(g):
   return g/1000

