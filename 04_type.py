# Typecasting 

name = "Yash Pokhriyal";
print(type(name));

age = 22;
print(type(age));

isTrue = True;
print(type(isTrue));


a = 1.87;
print(type(a),a);

# Implicit conversion ---->  Python automatically convert to higher datatype 

a = 10;
b = 24.6;
c=a+b;
print(type(c),c); #automatically change to float

# Explicit conversion ------>  we explicitly convert to different datatype
a = int("123");
b= 27.5;

print(type(a+b),a+b);