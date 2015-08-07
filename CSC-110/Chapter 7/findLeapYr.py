# findLeapYr.py
# Created by Jo

def giveResults (year, ans):
    print ('ans:', ans)
    if ans == 'Yes':
        print ("{0} is a leap year!".format (year))
    else:
        print ("{0} is not a leap year!".format (year))

def leapYear (yr):
    if yr < 400:
        if yr % 4 == 0 and yr % 100 != 0:
           results = 'Yes'
        else:
           results = 'No'
    if yr >= 400:
        if yr % 4 == 0 and yr % 400 == 0:
            results = 'Yes'
        else:
            results = 'No'

    return results

def getYear ():
    year = eval (input ("Enter Year to find out if it's a leap year: "))
    return year

def main ():
    givenYear = getYear ()
    ans = leapYear (givenYear)
    giveResults (givenYear, ans)

main ()
