 # EX:PROGRAM 1
'''condition = True 

while condition:
    print("condition is true")
    
# EX:PROGRAM 2 

is_failed = True  
i = 1 #attempt called as iteration
while is_failed and i<=100:
    print(f"never give up! {i}")
    i = i + 1
    
print("i gave up!")


# EX:PROGRAM 3
    
is_failed = True 
i = 1 #attempt
while is_failed:
    print(f"never give up! {i}")
    i = i + 1
    if i>=100:
        break
    
print("i gave up!")


# EX:PROGRAM 4

is_failed = True
i = 1

while is_failed:
    if i%2!=0: #is not even
        i = i + 1
        continue
    print(f"Attempt {i}")
    i = i + 1
    if i>100:
        break
print("I gave up !")

# EX:PROGRAM 5
i = 0
while i<=20:
    print(i)
    i += 1
    
# EX:PROGRAM 6
i = 0
while i<=10:
    x = 0
    while x<i:
         print("ABCD", end ="-")
    x += 1
    print("")
    i += 1 
    
    

    
pin = "1234"
while True:

     input_pin = input("pin >> ")
     if input_pin == pin:
          print("correct")
          break
else
    print("incorrect")
 
 
     
pin = "1234"
trials = 1
while trials<=5:
    input_pin = input (f"Trials-{trials} | pin >>")
    trials += 1
if input_pin == pin:
     print("correct")
     break
else:
    print(" incorrect ")
    
      
pin = "1234"
trials = 1

while trials <= 5:
    input_pin = input(f"Trials-{trials} | pin >> ")

    if input_pin == pin:
        print("correct")
        break
    else:
        print("incorrect")

    trials += 1
    
    
N = int(input("Enter the value of N: "))

i = 1
while i <= N:
    print(i)
    i += 1'''


i = 0
while i<=5:
    print(i, end = "   ")
    i += 1
    
    
for i in range (1 , 3):
    for j in range (1,11):
        print(f"{i}x{j}={i*j}")