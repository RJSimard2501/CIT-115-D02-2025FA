#Greet the user
print("Welcome to the interest calculator!")

#Variable inputs
fPV = float(input("What is your starting invesment? "))
fR = float(input("What is your Interest rate? "))
fT = float(input("How many years will the account earn interest? "))
fM = float(input("How many times is the interest compounded per period? "))


#Calculation 
#FV = PV (1+R/M)^MT
fR = fR / 100
fExponents = fM * fT 
fPV = fPV * (1+(fR/fM))** fExponents

#Convert Vars to Stings
sT = str(fT)
sPV = str(format(fPV, "0.02f"))

#Print Outputs
print("At the end of " + sT + " years you will have $"  +sPV)