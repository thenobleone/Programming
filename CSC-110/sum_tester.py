#File: sum_tester.py
#Created by Jo Narvaez-Jensen
#Project 1C

def main ():
    total = 0

    print ("The Gauss Calculator")

    cycles = eval (input ("Starting at 1, how many whole numbers do you want to add together? "))

    for start in range (cycles + 1):
        if start <= cycles:
            total = total + start

    print ("Grand Sum Total: ",total)

main()
