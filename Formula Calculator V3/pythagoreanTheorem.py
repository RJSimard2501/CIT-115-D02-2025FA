#Imports
import formating as f
import math

#Pythagorean Theorem Calculator Function
def pythagoreanTheoremCalculator():
    #Greet the user
    f.Dividerf()
    print("Welcome to the Pythagorean Theorem Calculator!")
    
    #Loop Variable
    fLoop = 1

    #Pythagorean Theorem Calculator Loop
    while fLoop != 2:
        try:
            #Ask for which side to solve for & Convert string to lowercase
            print("Which side are you solving for?")
            print("Type A/B, or C")
            sCalcType = input("Side: ")
   
            if sCalcType.lower() == "c":
            
                #Ask for values
                fA = float(input("What is your A Value?: "))
                fB = float(input("What is your B Value?: "))

                #Calculation "(A^2 + B^2)/ 0.5"
                fCalculation = ((fA** 2)+(fB** 2))** 0.5

                #Print Results
                f.Dividerf()
                print("Your C value is: "+ format(fCalculation, "0.4f"))

                #Contine/Go Back to Main
                f.Dividerf()
                print("Continue with Pythagorean Theorem?")
                sConfermation = input("Type 'Y' or 'N' ")
                if sConfermation.lower() == "y":
                    f.Dividerf()
                    print("")
                elif sConfermation.lower() == "n":
                    f.Dividerf()
                    print("")
                    fLoop = 2
                else:
                    sConfermation = input("Type 'Y' or 'N' ")

            #Solving for A/B
            elif sCalcType.lower() == "a" or sCalcType.lower() == "b":
    
                #Ask for values
                fA = float(input("What is your A/B Value?: "))
                fC = float(input("What is your C Value?: "))

                #Do the Math "C^2 - A^2 or B^2"
                fCalculation = math.sqrt(fC** 2 - fA** 2)

                #Print Results
                f.Dividerf()
                print("Your C value is: "+ format(fCalculation, "0.4f"))
            
                #Contine/Go Back to Main
                f.Dividerf()
                print("Continue with Pythagorean Theorem?")
                sConfermation = input("Type 'Y' or 'N' ")
                if sConfermation.lower() == "y":
                    f.Dividerf()
                    print("")
                elif sConfermation.lower() == "n":
                    f.Dividerf()
                    print("")
                    fLoop = 2
                else:
                    sConfermation = input("Type 'Y' or 'N' ")
            else:
                #Fail Message and re input
                print("This field only accepts 'A', 'B', or 'C'")
                sCalcType = input("Side: ")
        
        #Tried to convert characters to numbers error
        except ValueError:
            print("These fields only accept numbers")
