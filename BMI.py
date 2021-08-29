#This code will calculate the BMI for the given height and weight
height=int(input("what is your height in cm?"))
print("You have entered", height, "cm as your height")
weight=int(input("what is your weight in kg?"))
print("You have entered", weight, "kg as your weight")
BMI= weight/height**2
print("Your BMI is", BMI)

def BMIcalculator():
    height=int(input("What is your height in cm?"))
    weight=int(input("What is your weight in kg"))
    print("You entered your height as", height, "cm and you weight as", weight, "kg")
    BMI=weight/height**2
    print("Your BMI is", BMI) 
BMIcalculator()
#Line number 1 to 7 is for the calculation of BMI and line number 9 to 14 is also for the same. Line 1 to 7 is without the function and line 9 to 14 is with the function.
