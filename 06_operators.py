# Operators indicates what operations to be performed 
# Operands are the values on which these operations are performed.

# Python Arithmetic operators ---> + , - ,* , / , % , ** , //

a = 10;
b = 2;
print("Addition of a and b is ", a + b);
print("Subtraction of a and b is ",a - b);
print("Multiplication of a and b is ", a * b);
print("Division of a and b is ", a / b);
print("Modulus of a and b is ", a % b);
print("Exponentiation of a and b is ", b ** a);
print("Floor division of a and b is ", a//b);

# Floor division gives quotient in which digits after decimal are ignored.

# Comparsion operators 
print(3>2);
print(3<2);
print(3<=2);
print(3>=2);
print(3 =='3')
print(3==3)
print(3!=10)


# Logical operators 

# and , or , not

print(3>7 and  3<7);
print(3>7 or  3<7);
print(not 3>7)


# Assignment operators
# = , += , -= , *= , /= , %= , **= , //= , <<= ,

score = 0
score +=10;
print(score);


# Identity Operators
# identity operators are used to compare items to see if they are same objects with same memory address

# 1. is 2. is not 

a = 1234
b = '1234'
print(a is b)
print( a is not b)
print(a == b)


#Bitwise operators 
# These operators are used to compare binary numbers

# Types
# 1. And & 2. Or | 3. XOR ^ 4. Left shift << 5. Right shift >> 

a = 10;
b = 8;
print(a&b);
print(a|b);

# XOR similar items pe 0 dega and different pe 1 dega 


# Membership Operators are used to check the prsence of a sequence in an object .
# Types
# 1. in 2. not in

a = "Hello Yash Bruh";

print ("llo" in a);
print ("llo" not in a);


