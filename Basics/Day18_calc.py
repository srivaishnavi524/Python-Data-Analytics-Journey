def add():
    print("result 1 is ", __name__)

def sub():
    print("result 2 is ")

def main():
    print("in calc main")
    add()
    sub()

if __name__ == "__main__":
    main()

# here excution is starts from main so the O/P is 
# in calc main
# result 1 is __main__
# result 2 is 