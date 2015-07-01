#File: chaosPratice.py
#tester file for the various modifications to the base chaos.py script used in Chapter 1
# Created by Jo Narvaez-Jensen

def main ():
    print("This program illustrates a chaotic function")
    x = eval (input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * (x - x * x)
        print (x)
main ()
