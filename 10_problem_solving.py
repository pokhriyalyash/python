# 1. Write a programme to find a sum of all the even numbers p to 50

sum =0;
for i in range(1,51):
    if i%2==0:
        sum+=i;
print("Sum of all even numbers upto 50 is : ",sum);


# 2.  Write a programme to write first 20 numbers and their squared numbers

for i in range(1,21):
    print("Square of ",i," is ",i*i);


# 3. Write a programme to find sum of first 10 odd numbers using while loops

sum =0;
n = 0;
while n<=20:
    if n%2!=0 :
        sum+=n;
    n+=1;
print("Sum of 10 odd numbers are : ",sum);



# 4. Write a programme to check if a number is divisble by 8 nd 12 upto 100 number

for i in range(1,101):
    if i%8==0 and i%12==0 :
        print(i);


# 5. Write a programme to create a billing system in marketplace

while True :
    name = input("Enter your name : ");
    total = 0 ;
    while True:
        quantity = int(input("Enter quantity : "))
        amount = int(input("Enter amount : "))
        total += quantity*amount;
        repeat = input("Do you want to buy further items ");
        if repeat == "no" or repeat =="No":
            break;

    print("-"*40);
    print("Name : ",name);
    print("Amount to be paid in total ",total);
    print("-"*40);
    print("*************** Happy Shopping ***************")
    repeat1 = input("Do you want to go to next customer ? ")
    if repeat1 == "no" or repeat1=="No":
        break;
