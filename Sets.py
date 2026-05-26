set = {1,10,20,30,123,60,80,70} # set is unordered 
print(set)

s1 = {1,2,3}
s2 = {3,4,5}
print( s1 | s2 )

s1 = {1,2,3}
s2 = {3,4,5}
print( s1 & s2 )

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1 - s2
print( s1 - s2 )

fruits = {"apple","banana","water_mellon"}
fruits.add("orange")
print(fruits)

fruits = {"apple","banana","water_mellon"}
fruits.remove("banana")
print(fruits)

fruits = {"apple","banana","water_mellon"}
fruits.discard("water_mellon")
print(fruits)