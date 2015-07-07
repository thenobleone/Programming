#File: sum_n.py
#Created by Jo Narvaez-Jensen
#Project 1C

#program design to take an input (cycles) from the user.
#   then calcuate it's sum
#   and output the final results

def main ():
    total = 0

    # Welcome message
    print ("The Gauss Calculator")

    # Prompt user input for number to times they want to run (cycles)
    cycles = eval (input ("Starting at 1, how many natural numbers do you want to add together? "))

    #definite loop to calcuate the sum of the users request
    for start in range (cycles + 1):
        if start <= cycles:
            total = total + start

    #output the final sum (total) to the user
    print ("Final Sum: ", total)

main()
