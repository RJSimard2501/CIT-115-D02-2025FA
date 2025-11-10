#Imports
import formating as f
import math

#Vertex Form Calculator
def vertexFormCalculator():
    print("Welcome to the Vertex Form Calculator")

    #Loop Variable
    fLoop = 1
    
    #Vertex Form Calculator Loop
    while fLoop != 2: 
        try: 
            #Get h, k, x, & a Variables
            fH = float(input("Type your H value: "))
            fK = float(input("Type your K value: "))
            fX = float(input("Type your X value: "))
            fA = float(input("Type your A value: "))        

            #Calculation & String conversion
            #y = a(x - h)² + k
            fCalculation = fA*(fX - fH)**2 + fK
            sConvert = format(fCalculation,"0.04" )

            #Print outputs & continue
            f.Dividerf()
            print("Your Y value is: " + sConvert)
        
            #Contine/Go Back to Main
            f.Dividerf()
            print("Continue with Vertex Form?")
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
        
        #Tried to convert characters to numbers error
        except ValueError:
            print("These fields only accept numbers")

