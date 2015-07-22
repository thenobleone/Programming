# grade_calcuator.py
# Created by Jo Narvaez-Jensen

# This program is designed to allow a user to convert any number of inputed
#   percentage grades into it's corresponding letter grade on the 4.0 GPA scale.

def main ():
    # Initialize needed variables
    totalScore = 0
    letterGrades = ["F", "D", "C", "B", "A"]

    # Welcomes and prompts the user for their input then splits the input into
    #   a list, and sets the indexed value.
    print ("\nWelcome to the percentage to GPA convert!")
    print ("This program calculates your average score (1- 100) & tell you your average along with its corresponding grade.")
    grades =  input ("\nEnter any number of grades seperated by a comma (eg. a, b, c): \n").split(",")

    # Gets the max sum of the scores inputted by pulling each indexed value
    #   and converting it into a float
    for i in range (len(grades)):
        totalScore =  totalScore + float (grades[i])

    # Calculates the avg score and the gpa
    avg = totalScore / len(grades)
    gpa = int(avg/10 - 5)

    # Handles the possible gpa exemptions that are outside the ideal range
    if gpa < 0:
        gpa = 0
    elif gpa > 4:
        gpa = 4

    #Outputs the all the given information, rounds the avg, and gives the GPA
    #   by the indexed value
    print ("\nThe average of your", len(grades), "scores is:", round (avg, 1), "resulting in a",letterGrades[gpa],"grade.\n")

main ()
