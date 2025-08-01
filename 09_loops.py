# Loops in python 
# for loop
# for(variable) in range(1,6,gap):
#      print(variable);

for a in range(1,6):
    print(a);

print();
for a in range(1,10,2):
    print(a);


# Print table
print("Tables")

n = int(input("Enter the number you want table of : "))
for a in range(1,11):
    print(n,"x",a,"=",n*a);


# While loop 
n = 0;
while n<=10 :
    print(n);
    n+=1;



#while true loop 
# Its an infinite loop 
# To break this infinite loop we used break statement


while True:
    num1 = int(input("Enter number 1 "))
    num2 = int(input("Enter number 2 "))
    print(num1+num2)
    repeat = input("Do you want to stop the programme ")
    if repeat=="yes" or repeat =="Yes" :
        break;


# Nested loops

for i in range(1,4):
    for j in range(1,11):
        print(i,j)
    print()


# Print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="");
    print()
    

#for loops with conditional statements

for i in range (1,11):
    if i ==3 :
        print("Added this song to favourite");
    else :
        print(i)

#break is to stop and continue is to skip