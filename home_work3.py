'''A = 20
B = 15
print(A>B and A<B)


A = 20
B = 15
print(A>B or A<B)

A = 20
B = 15
print(not(1>2))


 # (1)Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# (1) Check if both numbers are greater than 10 using AND operation
if num1 > 10 and num2 > 10:
    print(" Both numbers are greater than 10.")
else:
    print(" Both numbers are not greater than 10.")

# (2) Check if at least one number is less than 5 using OR operation
if num1 < 5 or num2 < 5:
    print(" At least one number is less than 5.")
else:
    print(" Neither of the numbers is less than 5.")

# (3) Check if the first number is NOT greater than the second (using NOT operation)
if not (num1 > num2):
    print(" The first number is not greater than the second.")
else:
    print(" The first number is greater than the second.")

#  example 2
user = float(input (" enter your age?: "))

if user >= 18 : 
    
    print(" you are an adult. ")

else:
    print(" you are a minor. ") 
'''
# example 3
'''
my_string = input("enter your name: ")
print("a" in my_string)
print("z" not in my_string) '''

'''
my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print("5" in my_list)
print("11" not in my_list)
'''

# Take two integer inputs from the user
A = int(input("Enter the first integer (A): "))
B = int(input("Enter the second integer (B): "))

# Perform bitwise operations
print("A & B =", A & B)       # Bitwise AND
print("A | B =", A | B)       # Bitwise OR
print("A ^ B =", A ^ B)       # Bitwise XOR
print("A << 2 =", A << 2)     # Left shift A by 2 bits
print("B >> 1 =", B >> 1)     # Right shift B by 1 bit
