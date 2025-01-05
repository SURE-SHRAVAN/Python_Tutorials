def factorial(n):
    if n== 0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
a= int(input("Enter a number: "))
ans = factorial(a)
print(ans, "is the factorial of" , a)

def is_leap(year):
    if(year % 4 != 0):
        print("False")
    else:
        print("True")
year = int(input("Enter the year: "))
print(is_leap(year))



