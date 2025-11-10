#formating Functions
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
def scConfermation():
    while True:
        fConfrmation = input("Would you like to continue using this calculator? Type Y or N: ")
        if fConfrmation.upper() == "Y":
            return 
        elif fConfrmation.upper() == "N":
            main()
        else:
            print("Enter either Y or N")
