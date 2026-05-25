
# Tuples

Genders = ("male", "female", "others")

print(Genders)

print(type(Genders)) # to find the types of class
print(len(Genders)) # to find the length
print(Genders[0]) #(index) to access individual element
print(Genders[1:3]) 

tuple1 = ("apple","banana","mango","orange")
tuple2 = ("musambi","muskmelon","watermelon","lemon")
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# tuple repetition:

tuple = ("musambi","muskmelon","watermelon","lemon") * 3

print(tuple)

# checking membership:

print("apple" in tuple1)

tuple = ("apple","banana","mango","orange")

print(tuple.count("apple")) 


