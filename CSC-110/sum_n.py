#File: sum_n.py
#Created by Jo Narvaez-Jensen
#Project 1C

def calculate ():
    total = 0

    cycles = eval (input ("Starting at 1, how many whole numbers do you want to add together? "))

    for start in range (cycles + 1):
        if start <= cycles:
            total = total + start

    return count (total)

def count (total):
    print ("The grand sum is: ", total)


def main ():
    print ("The Gauss Calculator")
    calculate ()

main()
