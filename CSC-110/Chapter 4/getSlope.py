#getslope
#Created by Jo Narvaez-Jensen
#write a program to find the slope of a line given two points on the line

def points ():
    x1, y1 = eval ( input("What is the coordinates of the first point located on the line (separated by a comma): "))
    x2, y2 = eval ( input("What is the coordinates of the second point located on the line (separated by a comma)? "))
    findSlope(x1,x2,y1,y2)

def findSlope (x1,x2,y1,y2):
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
        answer(slope)
    else:
        print ("The line is undefined.")

def answer (slope):
    print ("The slope of the line is m = ", slope, end = ".\n")

def main ():
    print ("Find the slope of your line!")
    points ()

main()
