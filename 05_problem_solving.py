# Problem solving 

# 1. Write a Programme to display person's name , age , and address in three different lines.

name = "Yash Pokhriyal";
age = 22;
address = "Delhi";
print("My name is",name,"\nMy age is",age,"\nMy address is",address);


# 2. Write a programme to swap to variables


a= 5;
b=6;
temp= a;
a=b;
b=temp;
print("Value of a is",a,"Value of b is",b);

#method 2
a=30;
b=40;
a,b=b,a;
print("Value of a is",a,"Value of b is",b);


# 3. Write a programme to convert float into integer 

num = int(3.97)
print(type(num),num);


# 4 . Write a programme to take details from student for id card and print it on dofferent line


name = input("Enter your name : ");
age = int(input("Enter your age : "));
grade = input("Enter your grade : ");
state = input("Enter your state : ");
email = input("Enter email of student : ");
phone_number = input("Enter phone number : ");

print("Student Id Card Details : ");
print("Name : ",name);
print("Age : ",age);
print("Grade : ",grade);
print("State : ",state);
print("Email : ",email);    
print("Phone Number : ",phone_number);


# 5 . Write a programme to take an user input as integer and convert it into float 

num = int(input("Enter Number : "))

num = float(num);
print(num,type(num));


