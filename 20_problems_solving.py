# Problem solving 

#1.Find the max and min in a set 

a= {12,56,34,8,90,1,57}
print("The minimum value in the set ",min(a))
print("The maximum value in the set ",max(a))

#2 Write a programme to find common elements in three lists using sets 
a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]
d = (set(a)&set(b)&set(c))
print(d)

#3.Write a programme to find difference between two sets 
a= {1,5,6,8,2}
b= {1,9,6,2,5}
print(a.difference(b))

#4. Write a python programme to remove an item from a set if it is present in set 
a={1,5,6,8,2}
a.discard(8)
print(a)

#5. Write apython programme to chcek is a set is subset of another set 
a={1,2,3,4,5,6}
b={2,3,4}
print(b.issubset(a))

