'''
attendance = 70
is_teacher_friend = False
if attendance >= 75 or is_teacher_friend:
    print("exam")
else:
    print("no exam")'''
    
    
gender = input("your gender>> ")
age =(int(input("your age>> ")))
if gender=="female":
  print("bus ticket is free")
  
else:
    if age <5:
      print("bus ticket is free")

    
    elif age <=12:
        print("you get child discount")
        
    elif age>=60:
        print("you will get senior citizen discount")