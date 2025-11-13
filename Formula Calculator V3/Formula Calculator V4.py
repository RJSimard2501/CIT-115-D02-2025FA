#Imports
import math
import random

#Formating Functions
def Dividerf():
    print("_________________________")

#String to Float converter
def floatconverter(sinput):
    while True:
        try:
            fValue = float(sinput)
            return fValue
        
        #Can't convert letters to numbers error, get new input, & restart loop
        except ValueError:
            sinput = input("Input must be a positive numeric value: ")

#Continue using the same calculator? Function
def scConfirmation():
    while True:
        fConfrmation = input("Would you like to continue using this calculator? Type Y or N: ")
        if fConfrmation.upper() == "Y":
            return 
        elif fConfrmation.upper() == "N":
            return False
        else:
            print("Enter either Y or N")

#Calculator Functions
#Pythagorean Theorem Calculator Function
def pythagoreanTheoremCalculator():
    #Greet the user
    Dividerf()
    print("Welcome to the Pythagorean Theorem Calculator!")

    #Pythagorean Theorem Calculator Loop
    while True:
        #Ask for which side to solve for & Convert string to lowercase
        print("Which side are you solving for?")
        print("Type A/B, or C")
        sCalcType = input("Side: ")
   
        if sCalcType.lower() == "c":
            #Ask for values
            fA = floatconverter(input("What is your A Value?: "))
            fB = floatconverter(input("What is your B Value?: "))

            #Calculation "(A^2 + B^2)/ 0.5"
            fCalculation = ((fA** 2)+(fB** 2))** 0.5

            #Print Results
            Dividerf()
            print(f"Your C value is: {fCalculation:0.4f}"))

            #Contine/Go Back to Main
            scConfirmation()
            if not scConfermation():
                break

        #Solving for A/B
        elif sCalcType.lower() == "a" or sCalcType.lower() == "b":
    
            #Ask for values
            fA = floatconverter(input("What is your A/B Value?: "))
            fC = floatconverter(input("What is your C Value?: "))

            #Do the Math "C^2 - A^2 or B^2"
            fCalculation = math.sqrt(fC** 2 - fA** 2)

            #Print Results
            Dividerf()
            print(f"Your missing side value is: {fCalculation:0.4f}")
            
            #Contine/Go Back to Main
            scConfirmation()
            if not scConfermation():
                break

        else:
            #Fail Message and re input
            print("This field only accepts 'A', 'B', or 'C'")
            sCalcType = input("Side: ")

#Quadratic Formula Calculator
def quadraticFormulaCalculator():
    #Greet the User
    Dividerf()
    print("Welcome to the Quadratic Formula Calculator!")

    #Quadratic Formula Calculator Loop
    while True:
        #Get A, B, & C Variables
        fA = floatconverter(input("Type your A value: "))
        fB = floatconverter(input("Type your B value: "))
        fC = floatconverter(input("Type your C value: "))

        #Calculate the discriminant
        fDiscriminant = fB**2 - 4 * fA * fC

        #Check if discriminant is negative
        if fDiscriminant < 0:
            Dividerf()
            print("No real roots exist :( \n")
        else:
            #Do the positive formula
            fPAnswer = (-fB + math.sqrt(fDiscriminant)) / (2 * fA)

            #Do the negative formula
            fNAnswer = (-fB - math.sqrt(fDiscriminant)) / (2 * fA)

            #Print outputs
            Dividerf()
            print(f"The positive output is: {fPAnswer:0.4f}")
            print(f"The negative output is: {fNAnswer:0.4f}")  

        #Confermation
        scConfirmation()
        if not scConfermation():
            break

#Vertex Form Calculator
def vertexFormCalculator():
    print("Welcome to the Vertex Form Calculator")

    #Vertex Form Calculator Loop
    while True:  
        #Get h, k, x, & a Variables
        fH = floatconverter(input("What is your H value"))
        fK = floatconverter(input("What is your K value"))
        fX = floatconverter(input("What is your X value"))
        fA = floatconverter(input("What is your A value"))
            
        #Calculation & String conversion
        fCalculation = fA*(fX - fH)**2 + fK

        #Print outputs & continue
        Dividerf()
        print(f"Your Y value is: {fCalculation:0.04f}")
        
        #Contine/Go Back to Main
        scConfirmation()
        if not scConfermation():
            break

#Random Number Generator
def randomNumberGenerator():
    print("Welcome to the Random Number Generator")

    while True:
        #Get Range & Number Of Operations 
        fMin = int(floatconverter(input("What is the minimum number you want to start with: ")))        
        fMax = int(floatconverter(input("What is the maximum number you want to end with: ")))
        TotalOps = int(floatconverter(input("How many numbers do you want: ")))

        #Get the numbers
        fOpCount = 0
        while fOpCount < TotalOps:
            fOutput = random.uniform(fMin, fMax)
            print(f"Random number {fOpCount} is: {fOutput}")
            fOpCount += 1
            Dividerf()

        #Continue? Confermation check
        scConfirmation()
        if not scConfermation():
            break

#Main Function
def main():
    #try:
        #Main Calculator Loop
        while True: 
            print("Welcome to Remi's Formula Calculator! Version 3.0")
            print("Available Calculators include:")
            Dividerf()
            print("1) Pythagorean Theorem")
            print("2) Quadratic Formula")
            print("3) Vertex Form")
            print("4) Random Number Generator")
            Dividerf()

            #Pick a Calculator
            try: 
                sWCalc = float(input("Pick a Calculator (1-4)"))
                if sWCalc == 1:
                    pythagoreanTheoremCalculator()
                elif sWCalc == 2:
                    quadraticFormulaCalculator()
                elif sWCalc == 3:
                    vertexFormCalculator()
                elif sWCalc == 4:
                    randomNumberGenerator()
#                elif sWCalc == 47:
#                    easterEgg()
                else:
                    print("This field only accepts numbers.")
                    sWCalc = float(input("Pick a Calculator (1-4)"))
                            
            #Given a non number error exception & ask for new input
            except ValueError:
                print("This field only accepts numbers.")
            
            #Source file does not exist error
            except NameError:
                print("The calculator you have sected cannot run because you are missing files!!!\n To a new version of the calculator click the following link:\n")

    #General Error handler
    #except Exception as err:
        #print("General error: " + format(err))
          
#Easter Egg
#def easterEgg():
#    Dividerf()
#    print("We don't do that here.")
#    sWCalc = float(input("Pick literally anything else \n"))
#
#    if sWCalc == 47:
#        print("You asked for it lol.")
#        Dividerf()
#        print("https://youtu.be/dQw4w9WgXcQ?si=MnwD2av2qRsYWZXX")
#        Dividerf()
#    else:
#        print("Ok, good")
#        main()

#Program start
main()
