# grade_calculator.py
# Elaine Vu-Phan, Phuong Nguyen(Emily), Syed Kazmi
# This program will ask the user to input three scores out of 100. It
#

def main():

    
    #define the list of grades
    grades=["F","D","C","B","A"]
    
    #Discribe the program16,22,
    print("This program calculates the average of three scores out of 100 and outputs ")
    print("the value with its corresponding grade.")
    print()

    #This prompts the user to enter the three scores out of 100, (a, b, c).
    a, b, c = eval(input("Enter the three scores out of 100, separated by commas (eg. a, b, c): "))

    #calculate and output the average
    average=(a+b+c)/3
    average=round(average,1)
    print("The average score is", average, end=".\n")

    #calculate average with corresponding grade

    n=int((average-50)/10)

    #Output the grade
    if n <0:
        print("The grade is F")
    else:
        print()
        print("The grade is",grades[n],end=".")
    
main()
