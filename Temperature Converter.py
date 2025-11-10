#Print name
print("Remi Simard's Temperature Converter")

#Prompt for Temperature
fTemp = float(input("Enter a temperature: "))

#Prompt for conversion
sConvert = input("Is the temp F for Fahrenheit or C for Celsius? ")

#Fahrenheit ifs, Error & Calculation
if sConvert.lower() == "f":
    if fTemp >= 212:
        print("Temp can not be > 212")
    else:
        fTempOutput = (5.0 / 9) * (fTemp - 32)
        print("The Celsius equivalent is: " + format(fTempOutput,".1f"))

#Celsius ifs, Error & Calculation
elif sConvert.lower() == "c":
    if fTemp >= 100:
        print("Temp can not be > 100")
    else:
        fTempOutput = (((9.0 / 5.0) * fTemp) + 32)
        print("The Fahrenheit equivalent is: " + format(fTempOutput,".1f"))

#Give Error
else:
    print("Enter a F or C")