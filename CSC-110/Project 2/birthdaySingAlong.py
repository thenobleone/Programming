# birthdaySingAlong.py
# Created by Jo Narvaez-Jensen
# Project 2C

# This program inputs a user's name and sings them happy birthday with a bouncing ball.

from graphics import *

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
    sText.move(-2, -2)

    return text, sText

# method getNam: explains program and instructs the user for their name
def getName (window):
    prompt = Text (Point(250, 350), "Please Tell Me\nWho Has a Birthday!")

    prompt, promptShadow = textFormat (prompt, 22)
    promptShadow.draw (window)
    prompt.draw (window)

    name = Entry (Point (250, 280), 30)
    name.setText("Name Here")
    name.draw (window)
    return name

# Method to create and set text for the programs start button, with associated
#   assoicated instruction
def drawButton (window):

    #script for the "phyical" button
    button = Rectangle (Point (150, 250), Point (350, 200))
    button.setFill ("royalblue")
    button.draw (window)

    #script for the button lable
    buttonText = Text (Point (250, 225), "Click here to start!")
    buttonText, buttonTextShadow = textFormat (buttonText, 19)
    buttonTextShadow.draw (window)
    buttonText.draw (window)

    return button, buttonText, buttonTextShadow


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

    return title, name, message

# method that determines which verse is needed for the song
def lyrics (i, name):
    size = 20
    if i < 2 or i > 2:
        verse = Text (Point (250, 75), "Hap   -     py        Birth  -    day         to         you ")
    else:
        verse = Text (Point (250, 75), "Hap   -     py        Birth  -    day        dear       {0}".format (name.getText()))
    verse, verseShadow = textFormat (verse, size)
    return verse, verseShadow


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
        verse,verseShadow = lyrics (i, name)
        verse.draw (window)
        bouncing (ball)
        verseShadow.undraw ()
        verse.undraw ()
        ball.undraw ()
        i=+1

    return verse

# calls all funcations and closes the window when the user is done.
def main ():
    # Create a graphing window
    window = GraphWin ("Birthday Sing Along", 500, 500)
    window.setCoords (0, 0, 500, 500)
    window.setBackground ("darkcyan")

    name = getName (window)
    button, buttonText, buttonTextShadow = drawButton (window)

    if window.getMouse ():
        name.undraw ()
        buttonTextShadow.undraw ()
        buttonText.undraw ()
        button.undraw()

    birthdayCard (window, name)
    verse = birthdaySong (window, name)

    verse.setText ("Click to Exit")
    verse.draw (window)

    window.getMouse ()
    window.close ()

main ()
