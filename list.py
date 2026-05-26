list = ["bru","sugar","milk","cake"]
list.clear()  # clear all the element in the list.
print(list) 

list = ["bru","sugar","milk","cake"]
list[0] = "any coffee power" # changing a specific element in the list.
print(list) 

list = ["bru","sugar","milk","cake"]
print(len(list)) # check the length of the items list


list = [10,50,20,40,30,70,60,80,100,90]
#print(sorted(list)) # print the list from ascending order 
list.sort()
print(list)



list = [10,50,20,40,30,70,60,80,100,90]
sorted_list = sorted(list)
rev = sorted_list.reverse()
print(sorted_list) # print the list from descending order 

list = [10,50,20,40,30,70,60,80,100,90]
print(sum(list)) # return the sum of element in a list
