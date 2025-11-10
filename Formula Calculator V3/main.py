#Greet the User & Define Main
def main():
    #try:
        
        #Imports
        try:
            import formating as f
            import math
            import pythagoreanTheorem
            import quadraticFormula
            import vertexForm
            import randomNumberGenerator

        #Error if file missing
        except Exception as err:
            print("Calculator files are missing!!! " + format(err))
            print("To get a new version of the calculator click the following link:\n ")
            f.Dividerf()

        #Infinite Loop
        while True: 
            print("Welcome to Remi's Formula Calculator! Version 3.0")
            print("Available Calculators include:")
            f.Dividerf()
            print("1) Pythagorean Theorem")
            print("2) Quadratic Formula")
            print("3) Vertex Form")
            print("4) Random Number Generator")
            f.Dividerf()

            #Pick a Calculator
            try: 
                sWCalc = float(input("Pick a Calculator (1-4)"))
                if sWCalc == 1:
                    pythagoreanTheorem.pythagoreanTheoremCalculator()
                elif sWCalc == 2:
                    quadraticFormula.quadraticFormulaCalculator()
                elif sWCalc == 3:
                    vertexForm.vertexFormCalculator()
                elif sWCalc == 4:
                    randomNumberGenerator.randomNumberGenerator()
                elif sWCalc == 47:
                    easterEgg()
                else:
                    print("This field only accepts numbers.")
                    sWCalc = float(input("Pick a Calculator (1-4)"))
                            
            #Given a non number error exception & ask for new input
            except ValueError:
                print("This field only accepts numbers.")
            
            #Source file does not exist error
            except NameError:
                print("The calculator you have seected cannot run because you are missing files!!!\n To a new version of the calculator click the following link:\n")

    #General Error handler
    #except Exception as err:
        #print("General error: " + format(err))
          
#Easter Egg
def easterEgg():
    f.Dividerf()
    print("We don't do that here.")
    sWCalc = float(input("Pick literaly anything else \n"))

    if sWCalc == 47:
        print("You asked for it lol.")
        f.Dividerf()
        print("https://youtu.be/dQw4w9WgXcQ?si=MnwD2av2qRsYWZXX")
        f.Dividerf()
    else:
        print("Ok, good")
        main()

#Program start
main()
