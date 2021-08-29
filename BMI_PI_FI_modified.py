#Government of Switzerland has decided to check the BMI, FI and the PI.If PI>2, government will provide PI*0.75 times protien. 
#If FI>2, then government will give 5000$. If FI<1,, 3000$ is awarded and if FI is in btw 1 and 2, 2000$ is awarded.
def BMIcalculator(height, weight):
    BMI=weight/height**2
    print("Your BMI is", BMI)

def protienindex(height, weight):
    PI=height/weight
    print("Your protien index is", PI)
    if PI>2:
        amt_prt=PI*0.75
        print("You will get", amt_prt, "kg  of protein from the government of Switzerland")
    else: 
        print("You are not eligible to get the protein from the Swiss government")

def fitnessindex(height,weight):
    FI=weight*3/height
    print("Your Fitness index is", FI)
    if FI>2:
        print("You will get 5000$ from the Swiss government")
    if FI<1:
        print("You will get 3000$ from the Swiss government")
    if FI>=1 and FI<=2:
        print("you will get 2000$ from the Swiss government")
height=int(input("What is your height in cm?"))
weight=int(input("What is your weight in kg"))
print("You have entered your height as", height, "cm and you weight as", weight, "kg")
BMIcalculator(height,weight)
protienindex(height,weight)
fitnessindex(height,weight)
