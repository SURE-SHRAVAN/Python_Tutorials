a = []
number = int(input("Enter the size of the list: "))
for i in range(number):
    num = int(input("Enter the number: "))
    a.append(num)

b = []
for i in a:
    if i % 2 == 0:
        b.append(i ** 2)

print("Even numbers squared:", b)


take = input("Enter a string: ")
if take == take[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
    
ask = input("Enter a string: ")
char_list = [char for char in ask if "aeiou".find(char) == -1]
print("number of vowels in the string:", len(ask) - len(char_list))

def palindrome(name):
    if name == name[::-1]:
      print("is a palindrome")
    else :
      print("NOt a a palindrome")
    
name = input("ENter a word to check wheter its a palindrome: ")
palindrome(name)

