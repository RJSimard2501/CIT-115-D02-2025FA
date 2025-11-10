#Imports
import formating as f
import random

#Random Number Generator
def randomNumberGenerator():
    print("Welcome to the Random Number Generator")

    while True:
        
        #Get Range & Number Of Operations 
        fMin = input("What is the minimum number you want to start with: ")
        f.floatconverter(fMin)
        fMax = input("What is the maximum number you want to end with: ")
        f.floatconverter(fMax)
        TotalOps = input("How many numbers do you want: ")
        f.floatconverter(TotalOps)
        
        #Get the numbers
        fOpCount = 1
        while fOpCount != TotalOps:
            fOutput = random.randint(fMin, fMax)
            print(f"Random number {fOpCount} is: {fOutput}")
            fOpCount += 1

        #Continue? Confermation check
        f.scConfermation()
