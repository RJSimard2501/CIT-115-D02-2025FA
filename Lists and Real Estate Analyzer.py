#Currency format function
def formatCurrency(finput):
    return f"$     {finput:,.2f}"

#Convert to float function
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
        #Odd count: middle element (0-based indexing)
        return float(lSortedValues[mid])
    else:
        #Even count: average the two middle elements
        return (lSortedValues[mid - 1] + lSortedValues[mid]) / 2.0

#Main
def main():

    #Create Sales list
    sales: list[float] = []

    #Start entry loop
    while True:
        fSalesPrice = getFloatInput(input("Enter property sales value:"))
        sales.append(fSalesPrice)

        #Continue or not Loop
        while True:
            sContinue = input("Enter another value Y or N:")
            if sContinue.strip().upper() == "Y" or "N":
                break
            else:
                continue

        #If "n" End Loop
        if sContinue == "n":
            break

    #Sort ascending
    sales.sort()

    #Output: Individual entries
    for idx, amount in enumerate(sales, start=1):
        print(f"Property {idx:2d} {formatCurrency(amount)}")

    #Analytics 
    minimum = min(sales)
    maximum = max(sales)
    total = sum(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    #Output: Analytics formatted as currency
    print(f"Minimum:   {formatCurrency(minimum)}")
    print(f"Maximum:   {formatCurrency(maximum)}")
    print(f"Total:     {formatCurrency(total)}")
    print(f"Average:   {formatCurrency(average)}")
    print(f"Median:    {formatCurrency(median)}")
    print(f"Commission {formatCurrency(commission)}")

#Program Start
main()
