# A = ["Ross","Rachael","Monica","Joe"]

#1.Write a programme to swap the first and fourth element 
a =["Ross","Rachael","Monica","Joe"]
a[0],a[3] = a[3],a[0]
print(a)



#2. Write a programme to add new value at secodn position
a.insert(1,"Rossy")
print(a)


#3. Write a programme to delete a value from third position 
a.pop(3)
print(a)

#B = [13,7,12,10]

#1 . Write a programme to multiply all the number in the list
B = [13,7,12,10]
ans =1
for i in B:
     ans*=i;
print(ans)

#2. Write a programme to get the largest number from the list
largest=B[0];
for i in B:
     if(i>largest):
          largest=i;

print(largest)


