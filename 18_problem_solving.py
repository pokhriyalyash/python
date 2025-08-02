#1. Write a python programme to sort a dictionary by value .
a = {"a":12,"b":23,"c":6,"d":91,"e":45};
a = sorted(a.values())
print(a)

#2. Write a python script to print the dictionary where the keys are numbers between 1 and 15 and the values are sqaure of keys

a = {};
for i in range (1,16):
    a[i] = i*i;

print(a)

#3. Write a programme to multiply all the items in dictionary

c = {"a":1,"b":2,"c":3,"d":4,"e":5};
product = 1;
for i in c :
    product*=c[i];

print(product)

#4. Write a python programme to sort a dictionary by key 

d= {12:"a",56:"b",23:"c",48:"d",91:"e"}
print(sorted(d.keys()))