num=8000
#print(num)
def printNum():
    num=12000
    name="Rishika"
    print("Num",num)       # Num 12000 whenever want to print messsage with   variable keep , between message and varibale
    # First of all python will look for local variable if not found the it will loook for global variable and if that also not found it will give error
    print("Name is",name,"Who lives in Switzerland") # Message and varibale value can be mixed with the help of ,
    print("Num",+num)      # Num 12000 + after , is not for concatenation
    print("Num"+num)       # Error TypeError: can only concatenate str (not "int") to str num is integer to concatenate num should be converted in to string
    print("Num "+str(num)) # Num 12000, str is a function to convert a variable in to string
    dob=12
    month=11
    year=1987
    # Question is to print dob in DDMMYYYY
    print(dob,month,year)  # 12 11 1987 there will be space if , is used
    print(str(dob)+str(month)+str(year)) #12111987 to remove space concatenation is done, before concatenation integer should be converted in to string with str function.
    line1="I am living "
    line2="in swithzerland "
    line3="with my faimly"
    final_line=line1+line2+line3  # Line1 line2 line3 is concatenated with + sign, as it is string already so no need to use str function.
    print(final_line)
printNum()
#Done 
