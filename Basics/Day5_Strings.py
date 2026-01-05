# Str1="this is a string"
# Str2='is a string'
# Str3="""this is a string, we use this for multi line comments too"""
#it is because in string when we are using single codes then python wiil confuse where does tht string stops
# ex.   'hello this is x's tutorials' =>here from s that string  is not recognised so "hello this is x's tutorials" (so we used double codes and vise-versa)
#---------------------------------
# escape sequence character 
# \n- new line
# str="this is string. \nI need to print this in new line"
# print(str)
#\t- tab space betweeen them
#-----------------------------------
# Basic Operations on strings
# 1. Concatenation(+ operator )
# "hello" + "world" ---> "helloworld"
# 2. length of a string
# len(str)
#---------------------------------
# Indexing in python(position number)
# inderxing starts from 0
# H E L L O  W O R L D
# 0 1 2 3 4 5 6 7 8 9 10
# Str[5] is blank Space
# Str[4] is O 
# we cannot change/modify the value of the particular index
#------------------------------------
# Slicing
# Accessing part of a string
# str[stsrt_index: end_index] #ending index is not included
# str="helloworld"
# str[1:4]  # is ello
# str[:4] # is same as[0:4]
# str[2:] #is same as str[2: remaining part of total_str] or we can say 
# print(str[2:len(str)]) # lloworld
# print(str[-5:-2]) # it give wor (from last -5 w to -2r )
#-------------------------
# check for particular string is prsnt or not
#  ### in , if, if not

#Check if "free" is present in the following text:
# txt = "The best things in life are free!"
# print("free" in txt)

#using if stmt
# Print only if "free" is present:
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)
#----------------------------
# The split() method returns a list where the text between the specified separator becomes the list items.
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']
#----------------------------
# The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))
#----------------------------
# The strip() method removes any whitespace from the beginning or the end:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
#---------------------------------
# The lower() method returns the string in lower case:
# print(a.lower()) # (a.upper())  gives string in upper case
#---------------------------------
# str="i am a coder."
# str.endswith("er.") # returns T/F 
# str.capitalize() # 1st char is capital
# str.replace(old, new) # it Replaces all occurrences by default
# string.replace(old, new, count) # count is used to changes how many places we want to change that many times it changes , if not mentioned it replaces all 
# str.find(word) # it returns index value, if that word or string is present (1st index number)

# str.count(word)# counts how may times it is present in the string 
#---------------------------------------
# WAP to input user's first name & print its length
# name=input("enter your first name: ")
# print("length of your name is :", len(name))
#-------------------------------
# WAP to count the occurance of the $ in a string
# str= "hello, my account balance is $45.00 and $50.00 is my savings"
# print(str.count("$"))   #2

