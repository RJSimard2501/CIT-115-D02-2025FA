#Named Constants
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

#Greet the user
print("Welcome to Remi's Interplanetary Weight Calulator!")

#Ask for Values
sName = input("What is your name?: ")

fWeight = float( input("What is your Weight?: "))

#Acknowledge Users name & introduce Weights
print("Hi "+ sName + ", here is your weight on the following planets in our solar system!")

#Math
fMercury = fWeight * MERCURY
fVenus = fWeight * VENUS
fMoon = fWeight * MOON
fMars = fWeight * MARS
fJupiter = fWeight * JUPITER
fSaturn = fWeight * SATURN
fUranus = fWeight * URANUS
fNeptune = fWeight * NEPTUNE
fPluto = fWeight * PLUTO

#Print outputs
print("Weight on Mercury:" + format(fMercury, "10.2f"))
print("Weight on Venus:" + format(fVenus, "10.2f"))
print("Weight on Moon:" + format(fMoon, "10.2f"))
print("Weight on Mars:" + format(fMars, "10.2f"))
print("Weight on Jupiter:" + format(fJupiter, "10.2f"))
print("Weight on Saturn:" + format(fSaturn, "10.2f"))
print("Weight on Uranus:" + format(fUranus, "10.2f"))
print("Weight on Neptune:" + format(fNeptune, "10.2f"))
print("Weight on Pluto:" + format(fPluto, "10.2f"))