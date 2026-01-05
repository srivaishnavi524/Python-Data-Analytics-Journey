# Dictionaries are used to store data values in key:value pairs 
#they are unordered(no index),mutable(changable) & don't allow duplicate keys
# info = {
#     "name" : "Vaishnavi",
#     "age" : 21,
#     "marks" : [96, 97, 99],
#     "is_adult":True
# }
# info["name"]="Sri vaishnavi" #replaces the name vaishnavi 
#if we create the key value pair with same key it over write that name
# info ["subjects"] = ["python", "Java", "DBMS"] #added to info at the end
# print(info)
#-----------------------------
# null_dict={} #empty dict
# null_dict["name"]="Vaishnavi" #this name is added to null_dict
#------------------------------------
# Nested Dictonary in python
# student={
#     "name" : " priya",
#     "subjects" : {
#         "Phy" :97,
#         "Chem" : 99,
#         "Math" : 92
#     }
# }
# print(student["subjects"]["Chem"]) # 99
#--------------------------------------
#DIctonary Methods 
# student.keys() #returns all keys (only outer keys not nested keys)
# print(list(student.keys())) # typecaste
# print(len(list(student.keys()))) # 2 (name, subject)
# student.values()# return all values (priya , and nested key values) to convert them into list use 
# list(student.values())
# student.items()#returns all() key,val pairns as tuples , here it gives 2 tuples because of nested dict's(nested dict is written in dict formate in tuple)
# student.get("key") # returns the key according to value 
# print(student["name"]) # return name  (but if we ask for the other key whis is not in the dict it give's error )
# print(student["name1"]) #error
# print(student.get("name")) # return name (but if we ask for the other key whis is not in the dict it give's none )
# print(student.get("name1")) #none
# student.update(newDict) #insert the specfied items(key:value) to the dictonary
 #----------------------------------------------
#  example 1
# store following meanings in python dictionary
# table : "a piece of furniture","list of facts & figures"
# cat:"a small animals"
# dict={
#     "table" : ["a piece of furniture","list of facts & figures"],
#     "cat" : "a small animal"
# }
# print(dict)
#-------------------------------
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictonary & add one by one.use subject name as key & marks ae value 
marks={}
x=int(input("enter phy : "))
marks.update({"phy" : x })
y=int(input("enter math : "))
marks.update({"math" : y })
z=int(input("enter chem : "))
marks.update({"chem" : z })
print(marks) 
