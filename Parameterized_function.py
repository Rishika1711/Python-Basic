name="Rishika"
place="Switzerland"
dob="12-11-2004"

# This doesnt require any parameter to call
def bioData():
    print("Name is Ram who lives in India and dob is 15-09-2005")
    
# This require 2 parameter to get called
def bioData(name,place):
    print("Name is "+name+"She lives in "+place+"and dob is 15-09-2004")

# This require 3 parameter to get called
def bioData(name,place,dob):
    print("Name is "+name+"She lives in "+place+" and dob is "+dob)

#bioData()  # calling a function without parameter so top one should   be executed but python doesnt support overloading so it will gave error
#bioData(name,place) # Calling a function with 2 parameter so middle one should  be executed but it will not because python doesnt support overloading
bioData(name, place,dob) # Calling a function with 3 parameter so last function will be executed)

bioData("Anna","basel","12-02-2004")
bioData("Asean","Zurich","09-08-2003")
#bioData("Lucky","SWZ") # Middle function should be executed nut it will nt because python doesnt support overloading uncommenting will give error 

# When different method or function have same name with different parameter this concept is called method overloading

# We can define many function with same name in python but only the latest one will be considered
