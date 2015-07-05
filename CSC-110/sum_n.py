#File: sum_n.py
#Created by Jo Narvaez-Jensen
#Project 1C

def main ():
    total = 0

    print ("The Gauss Calculator")
    cycles = eval (input ("Starting at 1, how many whole numbers do you want to add together? "))

    for start in range (cycles + 1):
        total = total + start
        if total != 0:
            print (total)

main()
