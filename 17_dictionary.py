# Dictionary allows user to write the data in the from of keys and value pairs

Employee_data = {"name":"john","age":24,"gender":"male"}
print(Employee_data["age"])


#Iteration in dictionary 
Student = {"name":"John","class":"6th","roll_no":23}

#printing all the key names one by one 

for x in Student :
    print(x)
    print(Student[x])


#using value functions 
for x in Student.values():
    print(x)

#using items function
# for x in Student.items():
#     print(x)

# ('name', 'John')
# ('class', '6th')
# ('roll_no', 23)

for x,y in Student.items():
    print(x,y)


#Dictionary functions 


# Student = {"name":"John","class":"6th","roll_no":23}

#get 
print(Student.get("name"))
#item
print(Student.items())
# dict_items([('name', 'John'), ('class', '6th'), ('roll_no', 23)])

#keys
print(Student.keys())
# dict_keys(['name', 'class', 'roll_no'])

#copy 
d = Student.copy()
print(d)

#setdefault
x = Student.setdefault("roll_no",26)
print(x)
#update 
#pop
#popitem
#clear

#Nested dictionary 
Employees_data = {1:{"Name":"Raju","Age":23,"Gender":"male"},
                  2:{"Name":"Sehej","Age":32,"Gender":"female"},
                  3:{"Name":"Suhan","Age":22,"Gender":"male"}}

print(Employees_data[2]["Age"])
print(Employees_data[1])