# birthdaySingAlong_cc.py
# Created by Jo Narvaez-Jensen
# Project 2C

# This program inputs a user's name and sings them happy birthday with a bouncing ball.

from graphics import *
from random import *

# textFormat method, standardizes all initial values for any graphic text and
#   creates an assoicated shadow
def textFormat (text, size):
    text.setSize (size)
    text.setFace ('arial')
    text.setStyle ('bold italic')

    # Sets the specific text color based on the various text thanks to their
    #   predetermined sizes, will look into a more method based approch
    if size == 20:
        text.setTextColor ('blue')
    elif size == 34:
        text.setTextColor ('dodgerblue')
    else:
        text.setTextColor ('darkmagenta')

    sText = text.clone ()
    sText.setTextColor ('dimgray')
    sText.move (-2, -2)

    return sText, text

# Function to change the various text colors
def colorChange (text):
    text.setTextColor (color_rgb (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255)))
    return text

# Function to draw the various graphic features
def featureDraw (feature, window):
    for i in range (len(feature)):
        feature[i].draw (window)

# Function to clear features from the graphic window
def featureClear (feature, window):
    for i in range (len(feature)):
        feature[i].draw (window)

# method getNam: explains program and instructs the user for their name
def getName (window):
    welcome = Text (Point(250, 350), "Please Tell Me\nWho Has a Birthday!")
    welcome = textFormat (welcome, 22)

    name = Entry (Point (250, 280), 30)
    name.setText("Name Here")



# Method to create and set text for the programs start button, with associated
#   assoicated instruction
def button (window):
    buttonFeature = []

    #script for the "phyical" button
    button = Rectangle (Point (150, 250), Point (350, 200))
    button.setFill ("royalblue")

    #script for the button lable
    buttonText = Text (Point (250, 225), "Click here to start!")
    buttonText = textFormat (buttonText, 19)

    return buttonFeature

# Method cretas a pretty birthday card congratulating the user on their birthday
def birthdayCard (window, name):

    # Creates the card
    rp1 = Point (50, 450)
    rp2 = Point (450, 190)
    rShape = Rectangle (rp1, rp2)
    rShape.setFill ('lightpink')
    rShape.setOutline ('darkslateblue')
    rShape.setWidth (9)
    rShape.draw (window)

def birthdayMessage (window, name):
    # card's full text
    #   title text
    size = 36
    title = Text (Point (250, 390), "!!  Happy Birthday   !!")
    title = textFormat (title, size)

    #   user's name
    name = Text (Point (250, 320), "{0}".format(name.getText()))
    name, nameShadow = textFormat (name, size)

    #   bottom message
    message = Text (Point (250, 245), "! Congatulations !")
    message, messageShadow = textFormat (message, 30)

# method that determines which verse is needed for the song
def lyrics (i, name):
    size = 20
    if i != 2:
        verse = Text (Point (250, 75), "Hap   -     py        Birth  -    day         to         you ")
    else:
        verse = Text (Point (250, 75), "Hap   -     py        Birth  -    day        dear       {0}".format (name.getText()))
    verse = textFormat (verse, size)
    return verse


# graphic method for the ball, left seperate to ensure limited conflicts with
#   the bounce method
def drawBall (window):
    ball = Circle (Point (5, 160), 12)
    ball.setFill ('slategray1')
    ball.setOutline ('slategray1')
    ball.draw (window)
    return ball

# graphic method for moving the ball object across the graphic window
def bouncing (ball):
    # Loop moves a ball 6 times across the graphic window
    for j in range (6):

        # Inside Loop makes the move appear more fluid to the user, API limits
        #   the time.sleep function to a smallest maximum of 10 - 13 ms
        for d in range (10):
            ball.move (4, -7.3)
            time.sleep (.012)
        for u in range (10):
            ball.move (4, 7.3)
            time.sleep (.012)

# method for the lyrics, ball, and bounce output
def birthdaySong (window, name):
    for i in range (4):
        ball = drawBall(window)
        verse = lyrics (i, name)

        bouncing (ball)

        ball.undraw ()
        i=+1

    return verse

# calls all funcations and closes the window when the user is done.
def main ():
    # Create a graphing window
    window = GraphWin ("Birthday Sing Along", 500, 500)
    window.setCoords (0, 0, 500, 500)
    window.setBackground ("darkcyan")

    getName (window)
    featureDraw (getName (window), window)
    featureDraw (button (window), window)

    if window.getMouse ():
        featureClear (getName, window)


    birthdayCard (window, name)
    verse = birthdaySong (window, name)

    for i in range (2):
        verse[i].setText ("Click to Exit")

    featureDraw (verse, window)

    window.getMouse ()
    window.close ()

main ()



#IDEAS Crete function to print the text, iterating thru a list of each in order to save repeating myself and keep a text with it's shadow form
