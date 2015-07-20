# doTW.py
# Created by Jo Narvaez-Jensen

# Ask user to input number coresspeonding to the day of the week, starting with Sunday = 1
#   then output the 3 letter abbreviation of that days_of_week

days = "SunMonTueWedThuFriSat"

def main ():
    print ("This program will tell you what the letter abberivation for any day of the week!")

    day = eval (input("Starting with Sunday as 1, enter the numerical day of the week: "))

    pos = (day - 1) * 3
    selctedDay = days[pos:pos + 3]

#    for i in len(days):
#        if i = days.capitalize(day)
#        print (days[i:i+3])

    if day == 1:
        day = str(day) +"st"
    elif day == 2:
        day = str(day)+"nd"
    elif day == 3:
        day = str(day) + "rd"
    else:
        day = str(day) +"th"

    print ("The 3 letter abbrivation of",day, "day of the week is:",selctedDay)

main ()
