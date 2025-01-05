srt =int(input ("Enter a number: "))
rep = int(input("Enter the last limit:  "))

for _ in range(1,rep+1,1):
 num = _*srt
 print(num)


print("meow\n"*3)

op = input('Do you want to get in a lopp (Y or N): ' .upper )

while True:
 if op == 'N':
   break
 else:
  inp = int(input("Enter how many times: "))
  i = 0
 while i < inp:
  print("loop")
  i +=1