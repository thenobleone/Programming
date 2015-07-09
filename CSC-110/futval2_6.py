# futval2_6.py
# Created by Jo Narvaez-Jensen
# Modified version of the futval program to compute the value of an investment
#   based on a user inputed timeframe where a certain amount is fixed amount
#   each year

def main ():
    principle = 0

    print ("This program calculates the future value of an investment.")

    invest = eval (input ("Enter the amount of money to be invested each year: "))
    apr = eval (input ("Enter the annual interest rate as a decimal: "))
    time = eval (input ("How many years for the investment: "))

    for i in range (time):
#        principle = principle + invest
#        principle = principle * (1 + apr)
#        print ("two line: ", principle)

        principle = (principle + invest) * (1 + apr)
        principle = round (principle, 2)
        print ("single: ", principle)

    print ("The value of your investment in", time,"years is: ", principle, end=".\n")

main ()
