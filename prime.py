def is_prime(num):
    """Check if a number is prime using the specified logic."""
    return num % 3 != 0 and num % 2 == 1


user_input = input("Enter a list of numbers separated by space: ")

user_list = [int(x) for x in user_input.split()]

print("\nEntered list:", user_list)

prime_numbers = [num for num in user_list if is_prime(num)]
print("Prime numbers in the list:", prime_numbers)


