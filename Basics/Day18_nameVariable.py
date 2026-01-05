#   __name__ , __main__
print(__name__) # print __main__ , the value of name is main , the point of excution starts from here
# now let us consider 2 files 
# 1. demo
# 2. calc
# when we write __name__ in demo file it excutes first 
#------------------------
# file : demo.py
# import calc 
print("Helloo" + __name__) # helloo __main__
#-------------------------
# file: calc.py
print("Hello" + __name__) # hello calc
# while running the demo 
# it give O/P as 
# helloo __main__
# hello calc
#------------------------------------------------------------
# if we want to import the file1 and dont want to print the functions from that file1 we ask if (that file1) == __main__ then only print in file 1 
# then that functions will not print in another file As that function / file is not main method
# https://youtu.be/pzNISmtmzcY?si=-vy55eI6YXU5zUJa  
