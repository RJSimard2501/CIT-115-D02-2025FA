#Imports
import formating as f
import random

#Random Number Generator
def randomNumberGenerator():
    print("Welcome to the Random Number Generator")

    while True:
        
        #Get Range & Number Of Operations 
        fMin = int(f.floatconverter(input("What is the minimum number you want to start with: ")))        
        fMax = int(f.floatconverter(input("What is the maximum number you want to end with: ")))
        TotalOps = int(f.floatconverter(input("How many numbers do you want: ")))

        #Get the numbers
        fOpCount = 0
        while fOpCount <= TotalOps:
            fOutput = random.uniform(fMin, fMax)
            print(f"Random number {fOpCount} is: {fOutput}")
            fOpCount += 1
            f.Dividerf()

        #Continue? Confermation check
        f.scConfermation()

#Run Random number generator
randomNumberGenerator()
