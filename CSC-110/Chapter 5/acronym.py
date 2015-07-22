# acronym.py
# Created by Jo Narvaez-Jensen

# Program creates ancroynms from a user inputed phrase

def main ():
    #initialize variables
    acronym = ""

    # prompts and gets inputs from user and splits it into a list
    print ("\nThis program creates an acronym from a given phrase!")
    wordList = input ("Please enter your phrase: ").split()

    # creating the acronym
    for w in wordList:
        acronym = acronym + w[0]

    # Displays the resulting acronym in all caps
    print ("\n The phrase:", (" ".join(wordList).title()))
    print (" Creates the acronym:", acronym.upper(),"\n")

main ()
