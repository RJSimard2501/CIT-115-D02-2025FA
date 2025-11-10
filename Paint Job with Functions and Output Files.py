#Imports & ref links
#https://docs.python.org/3/library/math.html#module-math
import math

#Data validation and float coversion function
def getFloatInput(sinput):
    while True:
        try:
            #Try to convert to float & negtive number error
            fValue = float(sinput)
            if fValue <= 0:
                sinput = input("Input must be a positive numeric value: ")

            #All is good
            else:
                return fValue
        
        #Can't convert letters to numbers error, get new input, & restart loop
        except ValueError:
            sinput = input("Input must be a positive numeric value: ")

#Fujnction to Calculate gallons of paint needed
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

#Function to Calculate labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

#Function to Calculate labor cost
def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    return fTotalLaborHours * fLaborChargePerHour

#Function to Calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

#Get sales tax rate based on state
#New Hampshire dosn't need to be in the list bc it has a tax rate of 0?
def getSalesTax(sState):
    sState = sState.upper()
    if sState == "CT":
        fTaxrate = .06
    elif sState == "MA":
        fTaxrate = .0625
    elif sState == "ME":
        fTaxrate = .085
    elif sState == "RI":
        fTaxrate = .07
    elif sState == "VT":
        fTaxrate = .06
    else:
        fTaxrate = 0

    return fTaxrate

#Show cost estimate and write to file
def showCostEstimate(sLastName, fPaintCost, fLaborCost, fSalesTaxRate):
    fSubtotal = fPaintCost + fLaborCost
    fTaxAmount = fSubtotal * fSalesTaxRate
    fTotalCost = fSubtotal + fTaxAmount

    #Print outputs
    print(f"Paint Cost: {fPaintCost:.2f}")
    print(f"Labor Cost:  {fLaborCost:.2f}")
    print(f"Sales Tax Rate: {fSalesTaxRate:.2f}")
    print(f"Tax Amount: {fTaxAmount:.2f}")
    print(f"Total Cost: {fTotalCost:.2f}")

    #Write to a file with users name
    sFileName = f"{sLastName}_PaintJobOutput.txt"
    outfile = open(sFileName, "w")
    outfile.write(f"Paint Cost:  {fPaintCost:.2f}\n")
    outfile.write(f"Labor Cost: {fLaborCost:.2f}\n")
    outfile.write(f"Sales Tax Rate: {fSalesTaxRate:.2f}\n")
    outfile.write(f"Tax Amount: {fTaxAmount:.2f}\n")
    outfile.write(f"Total Cost: {fTotalCost:.2f}")
    outfile.close()

#Main function
def main():

    #Get number inputs
    fSquareFeet = getFloatInput(input("Enter wall space in square feet: "))
    fPaintPrice = getFloatInput(input("Enter paint price per gallon: "))
    fFeetPerGallon = getFloatInput(input("Enter feet per gallon: "))
    fLaborHoursPerGallon = getFloatInput(input("How many hours of labor per gallon: "))
    fLaborChargePerHour = getFloatInput(input("Labor chaarge per hour: "))

    #Get string inputs 
    sState = input("State job is in: ")
    sLastName = input("Customer's Last Name: ")

    #Calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fTotalLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)

    #Show and save estimate
    showCostEstimate(sLastName, fPaintCost, fLaborCost, fSalesTaxRate)

#Program start
main()