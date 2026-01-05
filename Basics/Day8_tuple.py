# Tuples: a built-in data type that lets us create immutable sequences of values.
#we cannot change tuple. but we can convert the tuple into a list, change the list, and convert the list back into a tuple.
# tup=(87, 64, 33, 95, 76, 64)
#tup[0]=43  # not allowed in python 
# print(type(tup))#class tuple
# tup = () #we can create empty tuple  
#tup = (1,) #  we need to specify the tuple with come if we assign single element otherwise the compiler thinks it as integer not tuple (single elements coma cmplsry)
#tup=(1) # type is integer
#print(tup.index(64)) ## returns index of first occurence (o/p -- 1(idx))
# tup.count(el)
# print(tup.count(64))
""" UNPACKING A TUPLE
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits 
print(green) # apple
print(yellow) #banana
print(red) #cherry
"""
"""
Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic) # ["mango", "papaya", "pineapple"]
print(red)
"""
#-----------------------------------------
# WAP to ask the user to enter names of their 3 fav movies and store them in a list 
# movies =[]
# movies.append(input("enter 1st movie: ")) #we can take input from user 1st and then we can append that variable to list too
# movies.append(input("enter 2nd movie: "))
# movies.append(input("enter 3rd movie: "))
#----------------------------------------------
# WAP to check if a list contains a palindrome of elements (hint:use copy()method )
#[1, 2, 3, 2, 1]
# list1=[1, 2, 3, 2, 1]
# list2=list1.copy()
# list2.reverse()
# if list1 ==list2:
#     print(list1," this list contains palindrome elements")
# else:
#     print("not a palindrome number")
#---------------------------------------------
# WAP to count the number of students with the "A" grade in the following tuple 
# grade= ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))
#----------------------------------------------
# Store the above values in a list & sort them from "A" to "D"
# Grade=list(grade) # converts them from tuple to list
# Grade.sort() #sort them in order
# print(Grade) 