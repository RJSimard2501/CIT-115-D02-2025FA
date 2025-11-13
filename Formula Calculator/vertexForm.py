#Imports
import formating as f
import math

#Vertex Form Calculator
def vertexFormCalculator():
    print("Welcome to the Vertex Form Calculator")

    #Vertex Form Calculator Loop
    while True:  
        #Get h, k, x, & a Variables
        fH = f.floatconverter(input("What is your H value"))
        fK = f.floatconverter(input("What is your K value"))
        fX = f.floatconverter(input("What is your X value"))
        fA = f.floatconverter(input("What is your A value"))
            
        #Calculation & String conversion
        #y = a(x - h)² + k
        fCalculation = fA*(fX - fH)**2 + fK
        sConvert = format(fCalculation,"0.04" )

        #Print outputs & continue
        f.Dividerf()
        print("Your Y value is: " + sConvert)
        
        #Contine/Go Back to Main
        f.scConfermation()
