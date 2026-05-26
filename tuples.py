# Tuples 
genders = ("male","female","other")
print(type(genders))
print(genders)


genders = ("male","female","other")
print(len(genders))

genders = ("male","female","other")
print(genders[1])


tuple1 = (1,2,3)
tuple2 = (4,5,6)
combined_tuple = (tuple1 + tuple2)
print(combined_tuple)

repeated_tuple = (1, 2) *15
print(repeated_tuple)

fruit = ( "apple","banana","mango","water_apple","orange ")
print("apple" in fruit)


fruit = ( "apple","banana","mango","water_apple","orange","apple")
print(fruit.count("apple"))

fruit = ( "apple","banana","mango","water_apple","orange","apple")
print(len(fruit))

fruit = ( "apple","banana","mango","water_apple","orange","apple")
print(fruit.index("apple"))