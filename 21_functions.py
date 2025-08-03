# Functions are set of code which execute when it is called
# Make organized

# Basic function
def var():
    print("hello")

var();

def hello():
    print("Hello world")

hello()

#parameters and arguuments

# parameters variable written inside the function 
# arguments are value passed to parameter while calling the function

def add(x,y):
    print("Sum of ",x,"and",y,"is",x+y);

add(5,6)


def rectangle(length,width):
    print("Area of rectangle is :",length*width)

rectangle(5,6)

def hello(name):
    print("Welcome dear :",name)

hello("Yash")

# *arbitary argument
def hello1(*name):
    print("Hello my name is ",name[1])

hello1("yash","john")


#return statement 
# return keyword is used to return the function and return the value of function

def namaste(name):
    return "Namaste world",name

print(namaste("Yash"))

def addition(a,b):
    return a+b

print(addition(5,6))


#recurssion is function calling function itself 
def fact(n):
    if n==1 or n==0:
        return 1;
    return n*fact(n-1)

factorial=fact(6);
print("Factorial of 6 is : ",fact(6))


# Recusrssion advantages
# 1. they made code look clean 
# 2. By use of recurssion complex task can be broken down into small sub parts .
# 3. Sequence generation become easy .

#Recurssion disadvantages
# 1. recurssive function takes lots of memory 
# 2. Sometimes logic become hard to follow 

#lambda functions
# It is used when an anonmyous function is required for a short period of time.
# It can take numerous arguments
# It can only have oe expression 

funcLam = lambda b :b*5;
print(funcLam(4));

x = lambda a,b,c :a+b+c;
print(x(2,3,4))

# Global and local variables 
# Local variables are restricted to block of code 
# Global variable are not restricted to one block of code 

# x = 24;
# def hello():

#     x = 25
#     return x

# print(hello()) #25
# print(x) #24



x = 24;
def hello():
    global x
    x = 25
    return x

print(hello()) #25
print(x) #25