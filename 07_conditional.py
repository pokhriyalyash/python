# Conditionals Statements 
# Allows the computer to excecute  certain condition if it is true 

# If statement 
marks = 97;
if marks>90 :
    print("You will get a mobile");

print("Thank you");



#If-else statement 

marks = 87;

if marks>=90:
   print( "You will get");
else :
    print("No phone for one week");

print("Thank You ");


# if elif else statement 

marks = 97;

if marks>=90:
    print("You wil get a trip");
elif marks>=80 and marks<90 :
    print("You will get a new phone");
elif marks>=70 and marks<80 :
    print("You will get a new book");
else :
    print("You will not get your phone");



# Nested if statement

marks = 87;
if marks>=80:
    print("You will get new phone");
    if marks>=95:
        print("You can go to a trip");
else:
    print("No phone for one year");



#Short hand if statement 
marks = 97;
if marks>=90 : print("You will get phone ");


#Short hand if else statement 
# (Body of if)  if (condition) else (body of else)

marks = 97;
print("You will get phone ") if marks>=90 else print("No phone for one year");



