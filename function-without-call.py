num=8000

# printNum is sa function which doesnt nedd parameter to get executed
def printNum():
    num=12000
    print("Num",num) # This print statement is correct but this will no print anything because function is not called
    printNum()       # This is calling printNum function but this will not be executed because function is not called
    print("Num":num)  # Invalid syntax because messsage and varibale can be seprated with , not : . To use concatenation + can be also used like : "Num"+str(num), but after execution we will not get error because this line is not executed, because function was not called.
# only first line will be executed 5 th to 8 willl be executed only if function is called

