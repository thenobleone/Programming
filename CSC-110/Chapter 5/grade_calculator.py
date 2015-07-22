# grade_calcuator.py
# Created by Jo Narvaez-Jensen, Nghiep Vu, Hermes Esono

def main ():
    # Initialize needed variables
    grades = ["F", "D", "C", "B", "A"]

    # Prompts the user for their grades
    print ("\nWelcome to the percentage to GPA convert!")
    print ("This program calculates the average of three scores (1 out of 100) & outputs the value with its corresponding grade.")
    grade1, grade2, grade3 = eval (input ("Please enter your 3 grades (seperated by commas): "))

    # Calculates the average and gpa values
    avg = (grade1 + grade2 + grade3)/3
    gpa = int(avg/10 - 5)
    if gpa < 0:
        gpa = 0
    elif gpa > 4:
        gpa = 4

    # Outputs the percentage average and letter grade using gpa as indexed value
    print ("\nThe average of your scores is", round (avg, 1), "resulting in an",grades[gpa],"grade.")

main ()
