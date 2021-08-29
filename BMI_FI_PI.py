def BMIcalculator():
    height=int(input("What is your height in cm?"))
    weight=int(input("What is your weight in kg"))
    print("You entered your height as", height, "cm and you weight as", weight, "kg")
    BMI=weight/height**2
    print("Your BMI is", BMI) 
BMIcalculator()
#Line number 1 to 7 is for the calculation of BMI and line number 9 to 14 is also for the same. Line 1 to 7 is without the function and line 9 to 14 is with the function.

def protienindex():
    height=int(input("What is your height in cm?"))
    weight=int(input("What is your weight in kg"))
    PI=height/weight
    print("Your protien index is", PI)
    if PI>2:
        amt_prt=PI*0.75
        print("You will get", amt_prt, "kg  of protein from the government of Switzerland")
    else: 
        print("You are not eligible to get the protein from the Swiss government")
protienindex()

def fitnessindex():
    height=int(input("What is your height in cm?"))
    weight=int(input("What is your weight in kg?"))
    FI=weight*3/height
    print("Your Fitness index is", FI)
    if FI>2:
        print("You will get 5000$ from the Swiss government")
    if FI<1:
        print("You will get 3000$ from the Swiss government")
    if FI>=1 and FI<=2:
        print("you will get 2000$ from the Swiss government")
fitnessindex()
