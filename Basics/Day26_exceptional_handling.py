# Errors:
# 1. compiletime Errors:
# --> missing colen , wrong spelling

# 2.  Logical Error:
# --> instead of adding two numbers, multiplying them eg. wrong output. this also comes under bugs

# 3.RuntimeError:
# --> no syntax error and no logical error but, might giving wrong input (divide by zero)

# --->>even if we are getting the exception/ error the excution should not stop is the main point of the exceptional handling

# statement : normal statement (will not give any error), critical()

#------------------------------------------------------
# try-except Block 
# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception as e:  #e is the object of exception
#     print("hey, you cannot divide a number by Zero   ", e) # e print the which type of exception it is
# print("byeeeee")

# try - test a block of code for errors. befor the error all stmts will execute , after the error it jumps into the except block
# except - it will handle the error, if we dont have the error we dont execute the except block
#finally -  it will be executed if we get error as well as if we dont get the error 
#---------------------------------------------------
# try-except-finally:
# a = [1, 2, 3, 4, 5]

# try:
#     print("we need the 6th index value of the list")
#     print(a[6])
# except Exception as e:  #e is the object of exception
#     print("index out of range ", e,) # e print the which type of exception it is (list index out of range)
# finally:
#     print("resource closed")
# print("from the out side of the try-except-finally block")
#-------------------------------------------------
a = 5
b = 2

try: 
    print("resource open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by Zero", e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("something went wrong", e)
    #-----------------------------------------------

