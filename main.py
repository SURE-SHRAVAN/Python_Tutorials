from Calc import *
print("Hello welcome to sure calculator")
a = int(input("Enter the values a  : "))
b = int(input("Enter the values  b : "))
operation = int(input("Enter the operation you want to perform (1.Add 2.Sub 3.Mul 4.Div): "))

if operation == 1:
    print("The sum of", a, "and", b, "is", add(a, b))
    print("The type of the result is", type(add(a, b)))
elif operation == 2:
    print("The difference between", a, "and", b, "is", sub(a, b))
    print("The type of the result is", type(sub(a, b)))
elif operation == 3:
    print("The product of", a, "and", b, "is", mul(a, b))
    print("The type of the result is", type(mul(a, b)))
elif operation == 4:
    print("The division of", a, "by", b, "is", div(a, b))
    print("The type of the result is", type(div(a, b)))
else:
    print("Invalid operation")
