#We can create functions like .upper(),.ceil() on our using keyword def
#Example code
def main():
    x =int(input("What is  the value of x??:"))
    if is_prime(x):
        print("Prime.")     
    else:
        print("Composite.")  
def is_prime(x):
    return x%2 == 1 and x%3 !=0

main()       

