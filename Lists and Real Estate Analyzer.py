#Format Currency function
def formatCurrency(finput):
    return f"$     {finput:,.2f}"

#Convert from sting to Float function
def getFloatInput(sinput):
    while True:
        #Strip input to remove extra spaces
        sStripedInput = sinput.strip()
        try:
            fOutput = float(sStripedInput)
            #Negative or Zero input error
            if fOutput <= 0:
                print("Error: Value must be positive and above zero. Please try again.")

            #All is good, Return Output
            else:
                return fOutput

        #Not a number error    
        except ValueError:
            print("Error: Please enter a valid numeric value (e.g., 250000 or 250000.00).")

        #Get new input & Restart loop
        input("Enter a new value: ")

#Get Median value function
def getMedian(sales):

    lSortedValues = sorted(sales)
    n = len(lSortedValues)
    mid = n // 2

    if n % 2 == 1:
        #Get middle if odd
        return float(lSortedValues[mid])
    else:
        #Average if even
        return (lSortedValues[mid - 1] + lSortedValues[mid]) / 2.0

#Main
def main():

    #Create Sales list
    sales: list[float] = []

    #Ask for Property sales input
    while True:
        fSalesPrice = getFloatInput(input("Enter property sales value:"))
        sales.append(fSalesPrice)

        #Continue or not Loop
        while True:
            sContinue = input("Enter another value Y or N:")
            if sContinue.strip().upper() == "Y" or "N":
                break
            else:
                print("Enter only Y or N,")
                continue

        #If "N" End Loop
        if sContinue == "N":
            break

    #Sort list in ascending order
    sales.sort()

    #Output: Individual entries
    for idx, amount in enumerate(sales, 1):
        print(f"Property {idx:2d} {formatCurrency(amount)}")

    #Calculate the math 
    minimum = min(sales)
    maximum = max(sales)
    total = sum(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    #Print the new values and format
    print(f"Minimum:   {formatCurrency(minimum)}")
    print(f"Maximum:   {formatCurrency(maximum)}")
    print(f"Total:     {formatCurrency(total)}")
    print(f"Average:   {formatCurrency(average)}")
    print(f"Median:    {formatCurrency(median)}")
    print(f"Commission {formatCurrency(commission)}")

#Program Start
main()
