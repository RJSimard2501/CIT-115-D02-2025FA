#Imports
import formating as f
import math

#Pythagorean Theorem Calculator Function
def pythagoreanTheoremCalculator():
    #Greet the user
    f.Dividerf()
    print("Welcome to the Pythagorean Theorem Calculator!")

    #Pythagorean Theorem Calculator Loop
    while True:
        #Ask for which side to solve for & Convert string to lowercase
        print("Which side are you solving for?")
        print("Type A/B, or C")
        sCalcType = input("Side: ")
   
        if sCalcType.lower() == "c":
            #Ask for values
            fA = f.floatconverterinput(input("What is your A Value?: "))
            fB = f.floatconverterinput(input("What is your B Value?: "))

            #Calculation "(A^2 + B^2)/ 0.5"
            fCalculation = ((fA** 2)+(fB** 2))** 0.5

            #Print Results
            f.Dividerf()
            print(f"Your C value is: {fCalculation:0.4f}"))

            #Contine/Go Back to Main
            f.scConfermation()

        #Solving for A/B
        elif sCalcType.lower() == "a" or sCalcType.lower() == "b":
    
            #Ask for values
            fA = f.floatconverterinput(input("What is your A/B Value?: "))
            fC = f.floatconverterinput(input("What is your C Value?: "))

            #Do the Math "C^2 - A^2 or B^2"
            fCalculation = math.sqrt(fC** 2 - fA** 2)

            #Print Results
            f.Dividerf()
            print("Your C value is: {fCalculation:0.4f}"))
            
            #Contine/Go Back to Main
            f.scConfermation()

        else:
            #Fail Message and re input
            print("This field only accepts 'A', 'B', or 'C'")
            sCalcType = input("Side: ")
