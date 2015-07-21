# chapter4p2.py
# Created by Jo Narvaez-Jensen

# program designed to draw an archery target using'rings' of the same 'width'; colors inside to outside: yellow, red, blue, black, white

from graphics import *

def main ():
    archery = GraphWin ("Archery", 375, 375)
    archery.setCoords (0,0, 375, 375)
    archery.setBackground ("LightBlue")
    center = Point (190, 185)

    # White Ring
    whiteRing = Circle (center, 175)
    whiteRing.setFill ("white")
    whiteRing.draw (archery)

    # Black Ring
    blackRing = Circle (center, 140)
    blackRing.setFill ("black")
    blackRing.draw (archery)

    # Blue Ring
    blueRing = Circle (center, 105)
    blueRing.setFill ("blue")
    blueRing.draw (archery)

    # Red Ring
    redRing = Circle (center, 70)
    redRing.setFill ("red")
    redRing.draw (archery)

    # Yellow Ring
    yellowRing = Circle (center, 35)
    yellowRing.setFill ("yellow")
    yellowRing.draw (archery)

    # 10 Ring
    yellowRing = Circle (center, 15)
    yellowRing.setOutline ("black")
    yellowRing.draw (archery)

    center.draw (archery)


main ()
