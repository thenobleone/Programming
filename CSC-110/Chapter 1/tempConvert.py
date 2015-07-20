# tempConvert.py
# Created by Jo Narvaez-Jensen
# this program allows a user to convert temperatures between Celcius and Fahrenheit

import sys

def pick ():
    print ("""
        Choose Option 1 to convert Celsius to Fahrenheit
        Choose Option 2 to convert Fahrenheit to Celsuis
        """)
    option = eval (input ("Which option would you like: "))
    whichTemp (option)

def whichTemp (option):
    if option == 1:
        celsius ()
    elif option == 2:
        fahrenheit ()
    else:
        print ("That is not a valid option.")
        return pick ()

def celsius ():
    try:
        cTemp = eval (input ("Please enter the Celsuis you wish to convert: "))
        temp = (5/9 * cTemp) - 32
        print (cTemp, "˚ Celsuis converts to ", round (temp, 2), "˚ Fahrenheit.", sep ="")
        repeat ()
    except:
        error (1)

def fahrenheit ():
    try:
        fTemp = eval (input ("Please enter the Fahrenheit you wish to convert: "))
        temp = (fTemp - 32) * 5/9
        print (fTemp, "˚ Fahrenheit converts to ", round (temp, 2), "˚ Celsius", sep ="")
        repeat ()
    except:
        return error (2)

def repeat ():
    contd = input ("Would you like to convert another temperature (Y/N)? ")

    while contd.upper () == 'Y':
        return pick ()
    print ("Goodbye")

def error (temp):
    print ("Not a valid temperature.")

    if temp == 1:
        return celsius ()
    else:
        return fahrenheit ()

def main ():
    print("""
        Welcome to Temperature Converter!
        """)
    pick ()

main ()
