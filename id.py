a = input("Enter a string: ")
v = a[4:11][::-1]
lst = []
lst.append(v)
for item in lst:
    for ele in item:
     print(ele , end = '')
 
 
a = 100.09
print(type(a))