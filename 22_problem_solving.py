#1 . Write a function to find maximum of three numbers in python 

def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else : 
        return c
    
print(max(7,2,8))


#2 . Write a python function to create and print a list where the values are square of numbers between 1 and 30 
def create_list():
    l = [(i,i*i) for i in range(1,31)];
    return l

print(create_list())

def create_list2():
    l=[]
    for i in range(1,31):
        l.append(i*i)

    return l;

print(create_list2())


#3. write a python function which takes number as parameter and check if the number is prime or not 
def isprime(num):
    isPrime = True
    for i in range(2,num):
        if num%i==0:
            return False
            
        
    return isPrime
print(isprime(7))

#4. write a python function to sum all the numbers in the list 
def sumList(numbers):
    answer = 0
    for i in numbers:
        answer+=i
    return answer
print(sumList([12,11,8,9]))

def sumList2(numbers):
    if len(numbers)==1:
        return (numbers[0])
    else :
       return( numbers[0] + sumList2(numbers[1:]))

sumList2(([12,11,8,9]))


#5. Write a python function to solve fibonnaci series using recurssion 
def fib(n):
    if n==1:
        return 0
    elif n ==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)
    
print(fib(9))
    