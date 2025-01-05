def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string
# Example usage:
str = input("Enter a string:")
result = reverse_string(str)
print(result)

#To repeat a string
repeated_string = "abc" * 3  # Results in "abcabcabc"
print(repeated_string)

#To find the lenght of the entered string
my_string = input("Enter a string:")
length = len(my_string) 
first_char = my_string[0]  # Accessing the first character
last_char = my_string[-1]  # Accessing the last character
# Convert to lowercase and uppercase
lowercase_string = my_string.lower()
uppercase_string = my_string.upper()

# Replace characters
replaced_string = my_string.replace("P", "J")

# Find substring
index = my_string.find("th")

# Check if the string starts or ends with a specific substring
starts_with = my_string.startswith("Py")
ends_with = my_string.endswith("on")
#formating a string
name = "shravan"
age = 18
op = "My name is {} and I am {} years old...".format(name,age)
print(op)
#f string literals
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
#Some more string functions
str = "I am a coder"
print(str.endswith("r"))#returns true if the sting ends with substring
print(str.capitalize())#Automatically capitalizes the first chara of a string
print(str.count("a"))#counts the occurence of the letter or character in a string
