# Tuples are collection of ordered and unmutable data 
#multiple datatype can be written in tuples

a= "apple","banana","mango",3
print(type(a))

# for tuple in single element bas element ke baad , comma lga do
b = "Banana",
print(type(b))


#slicing and iteration in tuples

fruits = "apple","banana","mango","grapes","orange"
print(fruits[1])
print(fruits[1:4]) 
# ('banana', 'mango', 'grapes')

print(fruits[::2])

#with for loop
for i in fruits:
    print(i)


#along with range and lenth
for i in range(len(fruits)):
    print(fruits[i])


#along with while loop 
i =0;
while(i<len(fruits)):
    print(fruits[i])
    i+=1;



#Conversion of tuples and tuples functions 

a = "Oneplus","Nokia","Redmi","Oneplus"
print("Type before conversion ",type(a))

a= list(a)
print("Type after conversion ",type(a))
a.append("Vivo")
print(a)
a= tuple(a)
print(type(a))

#functions of tuples
print(a.count("Oneplus"))
print(a.index("Nokia"))