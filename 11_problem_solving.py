"""
A = "Why fit in , When you are Born to Stand Out ! "

"""

#1. Write a programme to find the length of the following string 
a = "Why fit in , When you are Born to Stand Out ! "
print("Lenth of the whole string is : ",len(a));


#2. Write a programme to check how many times the alphabet o is occuring 
print(a.count("o"))

#3. Write a programme to convert whole string to lower and upper case
print(a.upper())
print(a.lower())

#4. Write a programme to convert it into title 
x= a.title();
print(x)

#5. Write a programme to find the ndex number of "fit-in"
print(a.find("fit in"))

#6 .Write a programme to display this patter 

# 1
# 2 2
# 3 3 3
# 4 4 4 4

n = 5 ;
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=" ");
    print()


#7 . Write a programme to display this pattern 

# 1 1 1 1 
# 2 2 2
# 3 3 
# 4

for i in range (1,n):
    for j in range(n,i,-1):
        print(i,end=" ")
    print()


#8 . Write a programme to display this pattern 
#       *
#     * *
#   * * *
# * * * *

for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


#9 . Print this pattern 
# 1
# 2 1
# 3 2 1
# 4 3 2 1 

for i in range(1,n):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


#10. Print this pattern 
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

for i in range(1,5):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for j in range (1,i+1):
        print("*",end=" ")
    print()


#11. Print this pattern

# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 

for i in range(1,5):
    for j in range(1,5):
        print(i*j ,end=" ")
    print()

# 1
# 2 4
# 3 6 9 
# 4 8 12 16
for i in range(1,5):
    for j in range(1,i+1):
        print(i*j ,end=" ")
    print()