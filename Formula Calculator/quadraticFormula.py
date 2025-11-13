#Imports
import formating as f
import math

#Quadratic Formula Calculator
def quadraticFormulaCalculator():
    #Greet the User
    f.Dividerf()
    print("Welcome to the Quadratic Formula Calculator!")

    #Quadratic Formula Calculator Loop
    while True:
        #Get A, B, & C Variables
        fA = f.floatconverter(input("Type your A value: "))
        fB = f.floatconverter(input("Type your B value: "))
        fC = f.floatconverter(input("Type your C value: "))

        #Calculate the discriminant
        fDiscriminant = fB**2 - 4 * fA * fC

        #Check if discriminant is negative
        if fDiscriminant < 0:
            f.Dividerf()
            print("No real roots exist :( \n")
        else:
            #Do the positive formula
            fPAnswer = (-fB + math.sqrt(fDiscriminant)) / (2 * fA)

            #Do the negative formula
            fNAnswer = (-fB - math.sqrt(fDiscriminant)) / (2 * fA)

            #Print outputs
            f.Dividerf()
            print("The positive output is: " + format(fPAnswer, "0.4f"))
            print("The negative output is: " + format(fNAnswer, "0.4f"))  

        #Confermation
        f.scConfermation()
