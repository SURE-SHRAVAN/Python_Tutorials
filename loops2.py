num = int(input("Enter upto which number u want to check: "))
for i in range(3,num+1,1):
    if i%2 == 1 and i%3 !=0:
        print(i , " is prime.")
    else:
        (i , " is composite." ) 
         

num = int(input("Enter up to which number you want to check: "))
i = 2

while i <= num:
    is_prime = True
    
    # Check if i is divisible by any number from 2 to i-1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    
    # Print the result based on whether is_prime is True or False
    if is_prime:
        print(i, "is prime.")
    else:
        print(i, "is composite.")
    
    i += 1

        