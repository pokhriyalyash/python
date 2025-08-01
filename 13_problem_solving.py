# Problems solving 

# 1. Write a programme to get fibonnaci series upto 10 numbers

# a = 0;
# b = 1;
# n = int(input("Enter a number here : "))
# if n == 1: 
#     print(1)
# else:
#     print(a)
#     print(b)

#     for i in range(2,11):
#        c=a+b;
#        a = b;
#        b = c;
#        print(c)


# 2. If number is prime or not

# num = int(input("Enter a number here : "))
# if num<=1:
#     print("Its not a prime number")
# else :
#     for i in range (2,n):
#         if n%i==0:
#             print("Not Prime")
#             break;
#         else :
#             print("Prime")


# 3. Valid palindrome 

num = 434;
rev =0 ;
temp=num
while num>0: 
    lastDigit = num%10;
    rev = rev*10+lastDigit;

    num//=10;

if rev == temp :
    print("Valid Palindrome")
else :
    print("Not Valid Palindrome")


# -----------------------------------------------------------------------------------------------------------------------
# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW";

#1. Write a programme to separate the string in comma separated value 

a = "OOTD.YOLO.ASAP.BRB.GTG.OTW";
b = a.split(".")
print(b) # ['OOTD', 'YOLO', 'ASAP', 'BRB', 'GTG', 'OTW']


#2. Write a programme to sort strings alphabetically in python .
a = "HELLO";
b = sorted(a);
print(b) #['E', 'H', 'L', 'L', 'O']


#3. Write a programme to remove a given character from string 



a = "hello"
print(a.replace("e",""));

#4 . Write a programme to remove dot from # Z = "F.R.I.E.N.D.S";

z ="F.R.I.E.N.D.S";
print(z.replace(".",""));

#5 . Write tro programme to check the occurence of a substring in the string 
a= "she sells seashells  on the sea shore "
print(a.count("sea"))

#6 . Take a input from a user as a string then reverse it .
str = input("Enter String ...")
print(str[::-1])


#7. Write a programme to check if a string contains only digits.
a = "1234"
print(a.isdigit())

#8. Write a programme to check if a string is palindrome . 
str = "madami"
if str == str[::-1]:
    print("Valid palindrome")
else :
    print("Not valid palindrome")


#9. Write a programme to find number of vowels in string 
a= "Hello its cool yash"
vowels =0;

for i in a :
    if i == 'a' or i =='i' or i =='o' or i=='e' or i=='u' or i =='A' or i == 'I' or i=='E' or i=="O" or i=='U':
        vowels+=1

print("No. of vowels in the string are ",vowels)

#10. Write a programme to check if eveery word in a string begins with a capital letter 

a= "The Hero Stays In House"
print(a.istitle())