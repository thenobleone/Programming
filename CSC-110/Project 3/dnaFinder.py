# dnaFinder.py
# Created by Jo Narvaez-Jensen
# Project 3A

# This program takes in a file, creates two strings, and searches one string
#   with the information from the other, outputting

# Outputs the results of the search giving the string searched for (dna), how
#   many times it appears (howMany) and iterates thru a list of indexes where it can be found (where)
def printResults (dna, where, howMany):
    print ("The DNA sequence of {0} occurs {1} times.".format (dna, howMany))
    print ("They can be found at {0}.".format (', '.join (str (i) for i in where)))

# Gets the # of times the search string appeared
def findNumOccurance (locationList):
    numAppear = len (locationList)
    return numAppear

# Searches for the desired string (search) within the larger string (maze), sending the index when found to a list (location)
def finder (maze, search):
    location = []
    index = 0

    # Loop design to also catch search matches that might overlap.
    while index < len (maze):
        index = maze.find (search, index)
        if index == -1:
            break
        location.append (index)
        index += 1
    return location

# Reads the file, splits the file, and assigns the values to individual
#   strings (fieldSearched, searchTerm)
def setData ():
    readFile = open ('motifFinding.txt', 'r')
    fileList = readFile.read ().rstrip (). split ('\n')

    field, search = fileList [0], fileList [1]

    return field, search

# Handles the running of all funcations and passage of parameters.
def main ():
    fieldToSearch, searchTerm = setData ()
    locationList = finder (fieldToSearch, searchTerm)
    numAppear = findNumOccurance (locationList)
    printResults (searchTerm, locationList, numAppear)

main ()
