#File: chaosModified.py
#Self project to take the end of Chatper 1 programing practice work and more them into a single working program
#Future modifications to include giving the user the option to return and try more options and creation of an exiting message.
# Created by Jo Narvaez-Jensen


# function designed to prompt user for an integer about which choice of chaos they would like to see.
def options ():
    print("""
        Please select from the following options:
            Enter 1 for Basic
            Enter 2 for Multipling by 2
            Enter 3 for 20 Returns
            Enter 4 to Pick the Range
            Enter 5 to use formula A
            Enter 6 to use formula B
            Enter 7 to use formula C
            Enter 8 to compare two numbers
        """)
    choice = int (input ("Which version of Chaos do you want: "))
    return chaos(choice)

#function designed to determine which choice the user makes and carry out the desired test
def chaos (choice):

#promts the user for a decimal number and then outputs then evaluation of 10 results based on the original formula provided.
    if choice == 1 or choice == 5:
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(10):
            x = 3.9 * x * (1 - x)
            print (x)

#promts the user for a decimal number and then outputs then evaluation of 10 results based on the formula provided using 2.0 as the multiplier instead of 3.9
    elif choice == 2:
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(10):
            x = 2.0 * x * (1 - x)
            print (x)

#promts the user for a decimal number and then outputs then evaluation of 20 results based on the original formula
    elif choice == 3:
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(20):
            x = 3.9 * x * (1 - x)
            print (x)

#promts the user for a decimal number as well as the number of times it should evaluate the number using the original formula
    elif choice == 4:
        repeat = eval(input ("How many times should I run: "))
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(repeat):
            x = 3.9 * x * (1 - x)
            print (x)

#promts the user for a decimal number and then outputs then evaluation of 10 results based on a modified formula of 3.9(x-x^2)
    elif choice == 6:
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(10):
            x = 3.9 * (x - x * x)
            print (x)

#promts the user for a decimal number and then outputs then evaluation of 10 results based on a modified formula of 3.9 * x - 3.9 * x - x
    elif choice == 7:
        x = eval (input ("Enter a number between 0 and 1:"))
        for i in range(10):
            x = 3.9 * x - 3.9 * x - x
            print (x)

#promts the user for two decimal numbers and outputs the results based on the original formula
    elif choice == 8:
        print("This program illustrates a two chaotic function at the same time!")
        x = eval (input ("Enter the 1st number between 0 and 1:"))
        y = eval (input ("Enter the 2nd number between 0 and 1:"))

        print ("input   1st:",x,"   2nd:",y)
        print ("------------------------")

        for i in range(10):
            #I know that I could just use x,y to run the evaluation but I prefer to keep them seperated in case there is ever a need to modify the formula being used.
            x = 3.9 * x * (1 - x)
            y = 3.9 * x * (1 - x)
            print ("     ",x,"    |   ",y)

#if the user selections an option beyond the provided choices
    else:
        print ("Sorry that is not an option! Goodbye!")

#function to welcome the user and invoke the chaos function
def main ():
    print ("Welcome to Chaos!")
    options()

main ()
