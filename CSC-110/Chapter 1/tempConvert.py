# tempConvert.py
# Created by Jo Narvaez-Jensen
# this program allows a user to convert temperatures between Celcius and Fahrenheit

import sys

def repeat ():
    contd = input ("\nWould you like to convert another temperature (Y/N)? ")

    if contd.upper () == 'YES':
        contd = 'Y'
    try:
        while contd.upper () == "Y":
            print ("")
            return pick ()
        else:
            print ("\nGoodbye!\n")
    except:
        print ("Sorry, that answer didn't make sense to me, please try again.")
        return repeat ()

def error (code):
    if code == 1:
        print ("Sorry, that's not a valid option, please try again.\n")
        pick ()
    else:
        print ("Sorry, that's not a valid temperature.\n")
        if code == 2:
            celsius ()
        elif code == 3:
            fahrenheit ()

def celsius ():
    try:
        cTemp = eval (input ("Please enter the Celsuis you wish to convert: "))
        temp = (5/9 * cTemp) + 32
        print (cTemp, "˚ Celsuis converts to ", round (temp, 2), "˚ Fahrenheit.", sep ="")
        repeat ()
    except:
        return error (2)

def fahrenheit ():
    try:
        fTemp = eval (input ("Please enter the Fahrenheit you wish to convert: "))
        temp = (fTemp - 32) * 5/9
        print (fTemp, "˚ Fahrenheit converts to ", round (temp, 2), "˚ Celsius", sep ="")
        repeat ()
    except:
        return error (3)

def pick ():
    print ("Choose Option 1 to convert Celsius to Fahrenheit")
    print ("Choose Option 2 to convert Fahrenheit to Celsuis\n")

    try:
        option = eval (input ("Which option would you like: "))
        if option == 1:
            celsius ()
        elif option == 2:
            fahrenheit ()
        else:
            return error (1)
    except:
        return error (1)

def main ():
    print("\nWelcome to the Temperature Converter!\n")
    pick ()

main ()
