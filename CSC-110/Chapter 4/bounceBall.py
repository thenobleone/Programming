# bouncingBall.py
# Created by Jo Narvaez-Jense

# This code is to  practice with a bouncing ball.

from graphics import *

def main ():
    # Create a graphing window
    win = GraphWin ("Bounce", 500, 500)
    win.setCoords (0, 0, 100, 100)

    # Create Lyric text
    verse = Text (Point (30,15), "Take      Me      Out       To     The       Ball   Game!")
    verse.draw (win)
    verse.setSize (20)
    verse.setStyle ("bold")
    verse.setFill ("blue")

    # Create and draw a ball
    ball = Circle (Point (10, 30), 2)
    ball.setFill ("LightSkyBlue")
    ball.draw (win)

    for j in range (7):
        # Create loop to bring the ball down
        for i  in range (10):
            ball.move (.1, -1)
            time.sleep (.025)

        # Create loop to bring the ball up and to the right
        for i  in range (10):
            ball.move (.5, 1)
            time.sleep (.025)


# FUNCTIONS CHAPTER 7!!


main ()
