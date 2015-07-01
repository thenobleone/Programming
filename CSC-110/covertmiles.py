# covertmiles.py
# this program converts distance in miles into kilometeres
# Created by Jo Narvaez-Jensen

def main ():
    miles = eval(input("Enter the distance in miles: "))
    km = 1.60934 * miles

    print ("The distance of", miles,"miles converts to", km, "kilometeres.")

main ()
