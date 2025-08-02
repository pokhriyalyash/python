# List are collection of ordered and mutable data
# multiple data can be stored in the data.

a= ["apple","mango",4,7,True];
print(a);
print (type(a));


# Slicing lists 
b = ["superman","batman","ironman","spiderman","hulk"];

#indexing
print(b);
print(b[0])
print(b[-1]) #hulk

#slicing 
print(b[1:3]) #['batman', 'ironman']
print(b[1:])
print(b[::-1])
print(b[1::2])


#list iteration 

#iteration using for loop 

avengers=["thor","captain america","hulk","ironman"]

for i in avengers:
    print(i)


print(len(a))
#iteration using for loop with range and length function 
for i in range(len(avengers)):
    print(avengers[i])

#iteration using while loops
i = 0;
while i<len(avengers):
    print(avengers[i])
    i+=1;


#Using Short hand for loop
print("Iterate using short hand for loop");

[print(i) for i in avengers]



#List Functions 
a = ["Thor","Hulk","Ironman","Spiderman","Batman","Hulk"]

#to find length of a ---len(a)
print(len(a))

#to count occurence of particular element ----
print(a.count("Hulk")) #2

#to add to the list at last 
a.append("Shaktiman");
print(a)


#to add to a specific location
a.insert(1,"Vision")
print(a)

#to remove from list 
a.remove("Hulk")
print(a)

#to remove from a certain location
print(a.pop(2))
print(a)


#to create a copy of list 
b = a.copy();
print(b)

#to access and element 
print(a.index("Hulk")) #4

#to extend the list 
c=["benjamin","Ironman"]
a.extend(c)
print(a)

#to reverse the list 
a.reverse()
print(a)

#to sort the list
a.sort()
d=[1,9,11,10] #follow alphabetical sorting
print(d)
print(a)

#clear all data from the list
# a.clear()


#List comprehension

l1 = [30,40,50,60]
l2=[]

for i in l1:
    if i>45:
        l2.append(i)

print(l2)

# List comprehension
# obtain i by using for loop
l3 = [i for i in l1]
print(l3);

l4 =  [i for i in l1 if i>40]
print(l4)




