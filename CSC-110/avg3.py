# avg3.py
# Created by Jo Narvaez-Jensen
# A simple program to average three exam scores

def main ():
    print ("This program computes the average of two exam scores.")

    score1, score2, score3 = eval (input ("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3)/3

    print ("The average of the score is", average)

main ()
