#Define Functions
#Main Function
def main():
    #Negative score test function
    def TestScoreTest(iTestInputValue):
        if iTestInputValue <= 0:
            print("Test scores must be greater than 0")
            exit()
        else:
            return

    #Prompt for user Name
    sName = input("Name of person we are calculating grades for: ")

    #Prompt for 4 Grades that are only int's
    iTest1 = int(input("Test 1: "))
    iTest2 = int(input("Test 2: "))
    iTest3 = int(input("Test 3: "))
    iTest4 = int(input("Test 4: "))

    #Run Negative test score function
    TestScoreTest(iTest1)
    TestScoreTest(iTest2)
    TestScoreTest(iTest3)
    TestScoreTest(iTest4)
    
    #Drop lowest grade if's
    sDropPrompt = input("Enter Y or N to Drop the Lowest Grade")
    if sDropPrompt.lower() == "y":
        
        #Test for lowest grade & Run function
        iLowestGrade = 100
        if iTest1 <= iLowestGrade:
            iLowestGrade = iTest1

        if iTest2 <= iLowestGrade:
            iLowestGrade = iTest2

        if iTest3 <= iLowestGrade:
            iLowestGrade = iTest3

        if iTest4 <= iLowestGrade:
            iLowestGrade = iTest4
            
        iGradeAverage = ((iTest1 + iTest2 + iTest3 + iTest4 - iLowestGrade) / 3)

    elif sDropPrompt.lower() == "n":
        iGradeAverage = ((iTest1 + iTest2 + iTest3 + iTest4) / 4)
    
    else:
        print("Enter Y or N to Dropthe Lowest Grade.")
        exit()

    #Grade the average
    if iGradeAverage >= 97:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: A+")
    
    elif iGradeAverage >= 94:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: A")

    elif iGradeAverage >= 90:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: A-")
    
    elif iGradeAverage >= 87:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: B+")
    
    elif iGradeAverage >= 84:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: B")
    
    elif iGradeAverage >= 80:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: B-")
    
    elif iGradeAverage >= 77:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: C+")
    
    elif iGradeAverage >= 74:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: C")

    elif iGradeAverage >= 70:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: C-")

    elif iGradeAverage >= 67:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: D+")
        
    elif iGradeAverage >= 64:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: D")

    elif iGradeAverage >= 60:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: D-")
    
    else:
        print(sName + " test average is: ", iGradeAverage)
        print("Letter Grade for this Test is: F")

#Run Main
main()