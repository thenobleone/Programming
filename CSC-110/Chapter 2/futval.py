# futval.py
# Created by Jo Narvaez-Jensen
# A program to compute rht value of an investment carried 10 years into the future

def main ():
    print ("This program calculates the future value.")
    print ("of a 10 year investment.")

    principle = eval (input ("Enter the initial principle: "))
    apr = eval (input ("Enter the annual interest rate: "))

    for i in range (10):
        principle = principle * (1 + apr)

    print ("The value in 10 years is: ", round (principle, 2))

main ()
