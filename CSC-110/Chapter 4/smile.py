# face.py
# Created by Jo Narvaez-Jensen

# top: 250
# bottom: 50
# left: 50
# right: 250

from graphics import *

def main ():
      # Creates GUI window for the user
      gWin = GraphWin ("Graphing Window", 300, 300)
      gWin.setBackground("blue")
      gWin.setCoords(0,0, 300, 300)

      cp1 = Point (150, 150)
      cShape = Circle (cp1, 100)
      cShape.setFill ("yellow")

      eyep1 = Point (125, 175)
      eyeShape1 = Circle (eyep1, 20)

      eyep2 = Point (175, 175)
      eyeShape2 = Circle (eyep2, 20)

      smile = Line (Point (100, 100), Point (200, 100))

      cShape.draw (gWin)
      eyep1.draw (gWin)
      eyeShape1.draw (gWin)
      eyep2.draw (gWin)
      eyeShape2.draw (gWin)
      smile.draw (gWin)

main ()
