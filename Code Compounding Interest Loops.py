#Data validation and float coversion function
def valueCheck(sinput):
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

#Data validation and float coversion function without 0 check
def valueCheckWithoutZero(sinput):
    while True:
        try:
            #Try to convert to float & return
            fValue = float(sinput)
            return fValue
    
        #Can't convert letters to numbers error, get new input, & restart loop
        except ValueError:
            sinput = input("Input must be a positive numeric value: ")

#Define Main
def main():
    #Get Inputs & Check them
    fOgDeposit = valueCheck(input("What is the Original Deposit (positive value): "))
    fInterestRate = valueCheck(input("What is the Interest Rate (positive value): "))
    fMonths = valueCheck(input("What is the Number of Months (positive value): "))
    fGoal = valueCheckWithoutZero(input("What is the Goal Amount (can enter 0 but not negative): "))

    #Clone Original Deposit before math operations
    fOgDeposit2 = fOgDeposit

    #Convert interest to a monthly percentage
    fMonthlyRate = (fInterestRate / 100) / 12

    #Calculate the interest, add interest to total summ, add 1 to month counter & print
    fMonthCounter = 0
    while fMonthCounter != fMonths:
        fTempRate = fOgDeposit * fMonthlyRate
        fOgDeposit = fTempRate + fOgDeposit 
        fMonthCounter += 1
        print(f"Month:  {fMonthCounter}  Acount Balance is: ${fOgDeposit:.2f}")

    #Find how many months it will take to reach the Goal using fOgDeposit2
    fMonthCounter2 = 0
    while fOgDeposit2 < fGoal:
        fTempRate = fOgDeposit2 * fMonthlyRate
        fOgDeposit2 = fTempRate + fOgDeposit2 
        fMonthCounter2 += 1
    
    #Print goal Data
    print(f"It will take: {fMonthCounter2} months to reach the goal of ${fGoal:.2f}")

#Run Main
main()