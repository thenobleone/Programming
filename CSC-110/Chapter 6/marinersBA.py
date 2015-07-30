# marinersBA.py
# Created by Jo Narvaez-Jensen

# Program takes a text file of batters and their current batting averages for
#   the Seattle Mariner's and outputs the information in a string in the format
#   of: "<firstName> <lastName> is batting <average>."

# This function breaksdown the individual lines into it's individual
#   compoments in order to create the desired output.
def printList (batters):
    for i in range (len (batters)):
        batter = batters[i].split (', ')
        print ("{0} {1} is batting {2}.\n".format (batter[1], batter[0], batter [2]))

# This function takes the initial file and breaks down into individual
#   indexes per line of information, removing any extra whitespamce at the end.
def batterInfo (fileData):
    batters = fileData.rstrip ().split ('\n')
    print ("batterInfo: ",batters)
    return batters

# Main, opens then saves the file information into a variable, and calls two
#   functions to create the desired output
def main ():
    readFile = open ('MarinersBattingAverage.txt', 'r')
    fileData = readFile.read ()

    batters = batterInfo (fileData)
    printList (batters)

main ()
