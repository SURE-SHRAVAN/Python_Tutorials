list = [33,45,234,234,423,34,45,535,635]
print(list)
#indexing always starts from 0 and also last element of the list can be said as -1
print(list[0])
#lenght
print(len(list))
print(id(list[1]))
print(id(list[6]))
print(list[:8])
#to print alternate numbers
print(list[::4])
#to extend an list by adding another
numbers =[2,3,5,7,3,3,56,8,0]
friends =["jim","joey","chandler"]
friends.extend(numbers)
print(friends)
#to add an element in list
friends.append("Tony")
print(friends)
#to add an element in the middle of the of the list
friend =["jim","joey","chandler"]
friend.insert(2,"sana")
print(friend)
#to remove an element
friend.remove("joey")
print(friend)
#to assign in alphabetical order
friend.sort()
print(friend)
