# factorial.py
# Created by Jo Narvaez-Jensen

# This program prompts the user for the user for a natural number #     (n), calculates, and outputs it's factorial (n!)

def main ():

    #Welcome statement
    print ("""
        This program will ask you to input a whole number, n.
        It will then calcuate and output n-factorial.
        """)

    #gets the input from the user
    n = eval (input ("What number would you like to factor: "))

    #initializes factorial to the value of 1
    factor = 1

    #definite loop to calcaute the factorial (factor)
    for i in range (n, 0, -1):
        factor = factor * i

    #outputs the result, factor
    print ("The product of", n, "is", factor, end = ".\n")



main ()
