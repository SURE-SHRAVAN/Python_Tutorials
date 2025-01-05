num = int(input("Enter the number you wish to see multiples for:"))
num2 = int(input("Enter how many multiples you want:"))
for i in range(1,num2+1):
   num3 = num*i
   print(num3)




students_data = []                                                                                      
num_students = int(input('Enter the number of students in your class:'))

for _ in range(num_students):
  name = input("Enter the name o fthe student: ")
  marks = int(input("Enter the marks: "))
  students_data.append((name, marks))

print(students_data)

for student in students_data:
  print("Name of the student", student[0], "and he scored", student[1], "out of 100.")














