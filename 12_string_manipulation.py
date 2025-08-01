# Strings are the combination of numbers , symbols ,and letters enclosed nside quotations .

#creation of string 
str ="Hello World";
print(str)
print(type(str))

# Strings methods

# len()
print(len(str))

#count() character btata string ka kitne bar aara hai .
print(str.count("o"))


#upper() and lower()
print(str.lower())
print(str.upper())

#index()
print(str.index("o"));

#capitalize()
print(str.capitalize())

#find()
print(str.find("l"))

#format()
name ="yash"
age =24
a = "My name is {} and age is {}"
print(a.format(name,age))

#center
name = "John"

print(name.center(10,"*"))

# casefold() and lower()
# casefold is more hlpful for foreign like lower() gibe beta while it will ss



a ="hello"
b ="Hello123"
c ="1234"
d ="HELLO"
e = " "
f = "Hello@123"
g = "1.234"


#isalnum
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(e,e.isalnum())


#isalpha()
#isdecimal()
#isdigit()-->return true if all character in strings are digit
#isnumeric())--->if all character in string are numeric
#islower()
#isupper()
#isspace()--->only space
#istitle()



#endswith()
#startswith()
#swapcase() lower case to uppercase and vice versa
#strip() return trim version of string (default spaces)
a= "    Harry Potter   "
print(a.strip())

b = "   ****gujju....   "
print(b.strip(".,*, "))

#split() --->splits the string at the specified separator and return the list
a= "#00FD#BRB#OMW#TB"
print(a.split("#"))

b = "Hello. My name is yash. I am a boy"
print(b.split("."))


#ljust() --->return the left justified version of string (default spaces , )
a= "Harry Potter"
x = a.ljust(20,"*") #Harry Potter******** is my favourite movie
print(x,"is my favourite movie")
# Harry Potter         is my favourite movie

#rjust()

#replace()

a = "My name is john "
print(a.replace("john","isaa"))


#rindex() search for the string for specified value and returns the last position of where it was found

a = "Harry Potter and the prisoner prisoner of Azbakan"
print(a.rindex("prisoner"))


#rfind()

#slicing in strings 
a = "Harry Potter and the Goblet of fire"
print(a)
print(a[0:5]) #Harry
print(a[6:12])#Potter
print(a[:5])  #Harry ----> here default starting value
print(a[-4:]) #fire---->here default ending value

b = "0123456789"
print(b[::2])#third value is step
print(b[:7:2])
print(b[::-1])

