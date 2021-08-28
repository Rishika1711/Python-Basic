num=8000

# printNum is sa function which doesnt nedd parameter to get executed
def printNum():
    num=12000
    print("Num",num) # This print statement is correct
    printNum()       # This is calling printNum function and this will lead to error because it will call function continuously
    # ** Function should not be called from the same function other wise it will go in infinite loop
    print("Num":num)  # Invalid syntax because messsage and varibale can be seprated with , not : To use concatenation + can be also used like : "Num"+str(num), but after execution we will not get error because this line is not executed, because function was not called.
    
printNum()  # calling a function
    
# line 1 will be executed memory will be aloocated to num variable. it will ignore 4 to 9 because it is part of function line 11 will be executed printNum function will be called
# command will go to function and line 5 will be executed, a new memory will be executed to num varibale, previous num was global and this is local thats  why both ahve different memory
# allocation then line 6 will be executed and at 7 it will call function again 5 will be executed this time new memory is not going to allocate value will be updated in previous local
# memory only then 6 will be executed and 7 will call the function again and this will continue for infinite thats why it will give recursive error.

