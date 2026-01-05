# python can be used to perform operstions on file.(read and write data)
# types of all Files
# 1. text files: .txt, .docx, .log etc.
# 2. Binary files : .mp4, .mov, .png, .jpeg etc.
# OPEN , READ & CLOSE FILE
# f = open("file_name", "mode")
# file_name --> sample.txt, demo.docx
# mode --> r : read mode, w:write mode
# data = f.read()
# f.close()
#DIFFERENT TYPES OF MODES
# 'r' - open for reading (default)
# r+ - read and overwrite the existing(stream is positioned ant starting, no truncate)
# 'w' - open for writing, truncating the file first
#w+ - read and overwrite the existing(stream is positioned ant starting,truncate)

# 'x' - create a new file and open it for writing
# 'a' - open for writing, appending to end of the file if it exists
# a+ - read , append, position at end, no truncate
# 'b' - binary mode
# 't' - text mode
# '+'- open a disk file for updating(reading &writing)
#we can combine 2 modes
#-----------------------------------------
# Reading a File
# data = f.read() #reads entire file
# data = f.read(5) #read upto 5 characters
# data = f.readline() #reads one line at a time. if no sentences available it gives empty line space
#-----------------------------------------
# f = open("Week 1/Day19_demo.txt", "r")

# line1 = f.readline()
# print(line1)

# line2 =f.readline()
# print(line2)

# line3 = f.read()
# print(line3)

# f.close()
#O/P
#hello I'm Learning Python # emply space is created after readline stmt is excuted

# Python syntax is very easy to learn and understand

# python is portable language
# python is object orianted and procedural orianted programming language    
#------------------------------------------------------------
# WRITING TO A FILE 
# w- writing into a file(overerites)
# a- writing itno file (new line) 

# f = open(r"C:\Users\pcred\.idlerc\Documents\PET(60)\Python\Week 1\Day19_demo.txt", "w")
# f.write("I want to learn javascript") #overwrites the entire file

# f.close()
#-------------------------------------
#APPENDING A TEXT TO A FILE
# f = open(r"C:\Users\pcred\.idlerc\Documents\PET(60)\Python\Week 1\Day19_demo.txt", "a")
# f.write("\nJavascript gives functionality to webpage") # adds to the file 
# f.close()
#----------------------------------------
# if i want to open file : Day19_sample.txt , but file is not present in the folder. it automatically create that file with the statement 
# f = open("Day19_sample.txt","w") #with only writing mode
#---------------------------------------------
#r+ -> is for reading and writing
# f = open(r"C:\Users\pcred\.idlerc\Documents\PET(60)\Python\Week 1\Day19_demo.txt", "r+")
# f.write("next I will learn react.js\n") # the stream is positioned at the beginning of the file
# f.close()
#--------------------------------------
# w+ -> open for reading and writing . the file is created if it doesnot exist, otherwise it is truncated(data will be deleted). 
# a+ -> the stream is positioned at the end of the file
#-------------------------------------------
# WITH SYNTAX
# with open("demo.txt", "a") as f:
#     data = f.read()
#---------------------------------------------
# DELETING A FILE 
# using the os module 
# Module(like a code library) is a file written by another programmer that generally has a functions we can use.
import os
# os.remove("filename")
# os.remove("Day19_sample.txt")
#-------------------------------------------- 
#PRACTICE QUESTIONS
# Create a new file "practice.txt" using python. add the following data in it.
"""hi everyone
we are learning File I/O 
using java
I like programming in java"""

# with open("Day19_practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O \nusing java\nI like programming in java")
#---------------------------------------------
# WAF that replaces all occurrences of "java" with python in above file.

# with open("Day19_practice.txt","r") as f:
#     data= f.read()
# new_data= data.replace("java","python")
# print(new_data)
#---------------------------------------------
#search the word "learning" exists in the file or not
# type 1 without functions
# word = "learning"
# with open("Day19_practice.txt") as file:
#     data = file.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

#type 2 with functions
# def check_for_word():
#     word = "learning"
#     with open("Day19_practice.txt") as file:
#         data = file.read()
#         if(data.find(word) != -1): #if(word in data != -1)
#           print("found")
#         else:
#             print("not found")

# check_for_word()
#------------------------------------------
# WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found 
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("Day19_practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data) :
#                  print(line_no)
#                  return
#         line_no += 1
# return -1
# check_for_line()
#---------------------------------------------
# from a file containing numbers seperated by comma, print the count of even numbers.
# with open("Day19_practice.txt", "r") as f:
#     data = f.read()
#     print(data)
#     num = ""
#     for i in range(len(data)):
#         if(data[i]==","):
#             print(int(num))
#             num =""
#         else:
#             num+=data[i]
#--------------------------------------------
count = 0
with open("Day19_practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)