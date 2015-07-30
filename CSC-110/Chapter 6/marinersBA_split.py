# marinersBS_split.py
# Created by Jo Narvaez-Jesen

#  Program takes a text file of batters and their current batting averages for
#   the Seattle Mariner's and creates to lists (names, batting averages), and
#   outputs the information in a string in the format of:
#   "<firstName> <lastName> is batting <average>."

# creates the desired ouput from the player list and average list
def printList (playerList, avgList):
   for i in range (len (playerList)):
       print ("{1} {0}".format (playerList [i][0], playerList [i][1]) + " is batting {0}.\n".format (avgList[i]))

# Takes the main array and splits it into a player array and a batting average list
def splitList (lineData):
    avgList = []
    tempList = []
    playerList = []

    for l in range (len(lineData)):
        info = lineData[l]
        for i in range (len (info)):
            if i < len (info)-1:
                tempList.append (info[i])
            else:
                avgList.append (info[i])
        # Keeps each individual's name together as individual lists
        playerList.append (list (tempList))
        tempList.clear ()
    return playerList, avgList

# Imports the file and creates a master array
def masterList ():
    roster = []
    playerList = []
    readFile = open ('MarinersBattingAverage.txt', 'r')
    batters = readFile.read ().rstrip (). split ('\n')

    for i in range (len (batters)):
        batter = batters[i].split (', ')
        playerList.append (batter)

    return playerList

#
def main ():
    roster = masterList ()
    playerList, avgList = splitList (roster)
    printList (playerList, avgList)

main ()
