l = [1,23,56,57,87,49,52,99]
total=0
for num in l:
    print(total)
    total=total +num
print(total)

# Doubling each number in a list
l = [1,2,3,4,5,6,7,8,9]
dl=[]

for num in l:
    dl.append(num*2)
    
print("dl:", dl)

#looping through dictionaries

student_marks = {"Anand": 85, "Geetha": 90, "kumar": 78}
for student, marks in student_marks.items():
    print(f"{student}--{marks}")
    
# iterating over dictionary values
student_marks = {"anand":85, "geetha":90, "kumar":78}
for marks in student_marks.values():
    print(marks)
    
    
# iterating over both Keys and values 
student_marks = {"Anand": 85, "Geetha": 90, "kumar": 78}
for student, marks in student_marks.items():
    print(f"{student} scored {marks}marks")
    
    
#for loop in range()
students = ["Anand" , "Geetha" , "kumar"]
marks =[85, 90, 78]
student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]
    
print(student_marks)


#for loop in range()
#example2

student = ["venkatesh","deepu","duthiksha"]
marks = [90,95,99]

student_marks = {}

for index, student in enumerate (student):
    student_marks[student] = marks [index]
    print(student_marks)