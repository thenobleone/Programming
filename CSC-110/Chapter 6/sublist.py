# sublist.py
# Created by Jo

def main ():
    playerList = []

    readFile = open ('MarinersBattingAverage.txt', 'r')
    fileData = readFile.read ().rstrip ()
    batters = fileData.rstrip ().split ('\n')

    for i in range (len (batters)):
        batter = batters[i].split (', ')
        playerList.append (batter)

    print (playerList)
    print (playerList[0][1])
    newList = playerList[0]
    print (newList[1])
main ()
