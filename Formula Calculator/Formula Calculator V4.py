#Imports
import math
import random

#Formating Functions
#Divider Function
def Dividerf():
    print("-" * 25)

#String to Float converter
def floatconverter(sinput):
    while True:
        try:
            fValue = float(sinput)
            return fValue
        
        #Can't convert letters to numbers error, get new input, & restart loop
        except ValueError:
            sinput = input("Input must be a positive numeric value: ")

#Continue using the same calculator? Function & Close CalcHistory.txt
def scConfirmation():
    while True:
        sCheck = input("Would you like to continue using this calculator? Type Y or N: ")
        if sCheck.upper() == "Y":
            Dividerf()
            return True
        elif sCheck.upper() == "N":
            Dividerf()
            return False
        else:
            print("Enter either Y or N")

#Calc History function
def calcHistory(sinput):
    with open("CalcHistory.txt", "a") as outfile:
        outfile.write(f"{sinput}")
        outfile.close()

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
        print("Type A, B, or C")
        sCalcType = input("Side: ")
   
        if sCalcType.lower() == "c":
            #Ask for values
            fA = floatconverter(input("What is your A Value?: "))
            fB = floatconverter(input("What is your B Value?: "))

            #Calculation "((fA**2)+(fB**2))**0.5"
            fCalculation = ((fA** 2)+(fB** 2))** 0.5

            #Print Results
            Dividerf()
            calcHistory(f"Your C value is: {fCalculation:0.4f}")
            print(f"Your C value is: {fCalculation:0.4f}")

            #Contine/Go Back to Main
            if not scConfirmation():
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
            calcHistory(f"Your missing side value is: {fCalculation:0.4f}")
            print(f"Your missing side value is: {fCalculation:0.4f}")
            
            #Contine/Go Back to Main
            if not scConfirmation():
                break

        else:
            #Fail Message and re input
            print("This field only accepts 'A', 'B', or 'C'")

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
            calcHistory("No real roots exist :( \n")
            print("No real roots exist :( \n")
        else:
            #Do the positive formula
            fPAnswer = (-fB + math.sqrt(fDiscriminant)) / (2 * fA)

            #Do the negative formula
            fNAnswer = (-fB - math.sqrt(fDiscriminant)) / (2 * fA)

            #Print outputs
            Dividerf()
            calcHistory(f"The positive output is: {fPAnswer:0.4f}")
            calcHistory(f"The negative output is: {fNAnswer:0.4f}")
            print(f"The positive output is: {fPAnswer:0.4f}")
            print(f"The negative output is: {fNAnswer:0.4f}")  

        #Confirmation
        if not scConfirmation():
            break

#Vertex Form Calculator
def vertexFormCalculator():
    print("Welcome to the Vertex Form Calculator!")

    #Vertex Form Calculator Loop
    while True:  
        #Get h, k, x, & a Variables
        fH = floatconverter(input("What is your H value: "))
        fK = floatconverter(input("What is your K value: "))
        fX = floatconverter(input("What is your X value: "))
        fA = floatconverter(input("What is your A value: "))
            
        #Calculation & String conversion
        fCalculation = fA*(fX - fH)**2 + fK

        #Print outputs & continue
        Dividerf()
        calcHistory(f"Your Y value is: {fCalculation:0.01f}")
        print(f"Your Y value is: {fCalculation:0.01f}")
        
        #Contine/Go Back to Main
        if not scConfirmation():
            break

#Random Number Generator
def randomNumberGenerator():
    Dividerf()
    print("Welcome to the Random Number Generator!")

    while True:
        #Get Range & Number Of Operations 
        fMin = floatconverter(input("What is the minimum number you want to start with: "))        
        fMax = floatconverter(input("What is the maximum number you want to end with: "))
        TotalOps = int(floatconverter(input("How many numbers do you want: ")))
        
        #Get the numbers
        fOpCount = 0
        while fOpCount < TotalOps:
            fOutput = random.uniform(fMin, fMax)
            print(f"Random number {fOpCount} is: {fOutput:0.1f}\n")
            calcHistory(f"Random number {fOpCount} is: {fOutput:0.1f}\n")
            fOpCount += 1

        #Confirmation check
        Dividerf()
        if not scConfirmation():
            break

#Easter Egg
def easterEgg():
    global FTEMPER
    if FTEMPER == 3:
        print("Check the back...")
        calcHistory(f"-------------------------\n")
        calcHistory(f"https://youtu.be/dQw4w9WgXcQ?si=MnwD2av2qRsYWZXX\n")
        calcHistory(f"-------------------------\n")
        
    else:
        print("This field only accepts numbers.")
        FTEMPER += 1
        
#Main Function
def main():
    #try:
        #Main Calculator Loop
        while True:
            print("\nWelcome to Remi's Formula Calculator! Version 4.0")
            print("Available Calculators include:")
            Dividerf()
            print("1) Pythagorean Theorem")
            print("2) Quadratic Formula")
            print("3) Vertex Form")
            print("4) Random Number Generator")
            Dividerf()

            #Pick a Calculator
            sWCalc = floatconverter(input("Pick a Calculator (1-4): "))
            if sWCalc == 1:
                calcHistory("\n --- Pythagorean Theorem Calculator --- \n\n")
                pythagoreanTheoremCalculator()
            elif sWCalc == 2:
                calcHistory("\n --- Quadratic Formula Calculator --- \n\n")
                quadraticFormulaCalculator()
            elif sWCalc == 3:
                calcHistory("\n --- Vertex Form Calculator --- \n\n")
                vertexFormCalculator()
            elif sWCalc == 4:
                calcHistory("\n --- Random Number Generator --- \n\n")
                randomNumberGenerator()
            elif sWCalc == 47:
                easterEgg()
            else:
                print("This field only accepts numbers (1-4).")
                        
#Program start
FTEMPER = 1
main()
