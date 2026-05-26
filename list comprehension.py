list = [1,2,3,4,5]
double_list = [item**2 for item in list]

print(double_list)

#example:1
l = [x for x in range(1,101)]

print(l)

dl = [x**2 for x in l]

print(dl)

edl = [x**2 for x in l if x%2==0]
print(edl)

#EXAMPLE:2
l = ["Venkatesh","Deepushree","Duthiksha"]

cl = [x[7] for x in l]
print(cl)


#EXAMPLE:3
names =  ["Venkatesh","Deepushree","Duthiksha"]
d = {name:len(name) for name in names}
print(d)

city_population = {
    "bangalore":10,
    "mysuru":20,
    "hubballi":30,
    "manglore":40,
    "kunigal":50
}