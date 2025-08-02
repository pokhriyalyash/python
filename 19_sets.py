# Sets are unordered collection of data . Every element in sets are unique and mutable

a={"Hulk","Thor","Captain America","Ironman"}
print(a)
print(type(a))
for x in a:
    print(x)


#Set functions
#add 
a.add("Spiderman")
print(a)
#pop random remove

a.pop()
print(a)

#remove jab particular value htani ho
a.remove("Ironman")
print(a)

#discard
a.discard("Hulk")
print(a)

#cody
b = a.copy()
print(b)


#isdisjoint
a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor"}

#isdisjoint -- ek bhi common na ho
print(a.isdisjoint(b))

#issubset
print(a.issubset(c)) #false
print(c.issubset(a)) #true

#issuperset
print(b.issuperset(a)) #false
print(a.issuperset(c)) #true

#update --union
a.update(c)
print(a)

#clear
# a.clear()
# Clear the whole set


a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Spiderman"}

#union
# print(a.union(b))

#difference
# print(a.difference(c))

#difference update a ke andar sabhi changes dega --->ussi me update krta
# a.difference_update(c)
# print(a)

#intersection
# x=a.intersection(c)
# print(x)

#intersection update 
# a.intersection_update(c)
# print(a)

#symmetric difference
x = a.symmetric_difference(c)
print(x)

#Symmetric difference update
a.symmetric_difference_update(c);
print(a)

