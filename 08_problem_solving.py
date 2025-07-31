# Problem solving ---- 2

# 1 . Write a programme to check if a number is positive or not 

num = int(input("Write a number "))

print("Its a positive number ") if num>0 else print("Its not a positive number ");

# 2 . Check whether the number is odd or even 

num = int(input("Write a number "))
print("Its an even number ") if num%2==0 else print("Its an odd number");



# 3 . Write a programme to create area calculater 

print("******** AREA CALCULATOR ********")

print("""Press 1 to get the  area of square .
Press 2 to get the area of rectangle .
Press 3 to get the area of circle .
Press 4 to get the area of triangle .""")

choice = int(input("Enter number : "));

if choice == 1:
    side = int(input("Enter side of square : "))
    area = side*side;
    print("Area of square is : ",area);

elif choice == 2:
    length = int(input("Enter length : "));
    breadth = int(input("Enter breadth : "));
    area = length*breadth
    print("Area of rectangle is : ",area);

elif choice == 3:
    radius = int(input("Enter radius : "));
    area = 3.14*radius*radius;
    print("Area of circle ",area);

elif choice == 4:
    base = int (input("Enter base of triangle : "));
    height = int(input("Enter height of triangle : "))
    area = 1/2 *base *height;
else :
    print("Wrong input");


# 4 . Write a programme to check if a letter is vowel or not 

letter = input("Enter the letter : ");

print("It is a vowel ") if (letter in "aeiou") or (letter in "AEIOU") else print("It is not a vowel ");


# 5 . Write a programme to check if a number is a single digit , 2 digit number upto 5 digit number .
num = int(input("Enter number upto 5 digit : "));

if num>=0 and num<=9:
    print("Its a single digit number ");
elif num>=10 and num<=99:
    print("Its a two digit number ");
elif num>=100 and num<=999:
    print("Its a three digit number ")
elif num>=1000 and num<=9999:
    print("Its a four digit number ");
elif num>=10000 and num<=99999:
    print("Its a five digit number ");
else :
    print("Invalid input");



    
    
