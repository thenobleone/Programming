# futval2_5.py
# Created by Jo Narvaez-Jensen
# Modified version of the futval program to compute the value of an investment
#   based on a user inputed timeframe

def main ():
    print ("This program calculates the future value of an investment.")

    principle = eval (input ("Enter the initial principle: "))
    apr = eval (input ("Enter the annual interest rate: "))
    time = eval (input ("How many years for the investment: "))

    for i in range (time):
        principle = principle * (1 + apr)

    print ("The value of your investment in", time,"years is: ", round (principle, 2), end=".\n")

main ()
