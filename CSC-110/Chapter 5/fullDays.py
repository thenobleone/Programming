# fullDays.py
# Created by Jo Narvaez-Jensen

# Ask user to input number coresspeonding to the day of the week, starting with Sunday = 1
#   then output the 3 letter abbreviation of that days_of_week

def main ():
    # Sets an array to the days of the week
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Displays and prompts the user for which day of the week is being requested
    print ("This program will tell you what day of the week it is based on it's numberical value!")
    day = eval (input("Starting with Sunday as 1, enter the numerical day of the week: "))

    # Pulls out the indexed value
    selectedDay = days[day - 1]

    # Converts user info into a string and adds appropriate ending to make the output nicer
    if day == 1:
        day = str(day) + "st"
    elif day == 2:
        day = str(day)+ "nd"
    elif day == 3:
        day = str(day) + "rd"
    else:
        day = str(day) +"th"

    print ("The",day, "day of the week is:",selectedDay)

main ()
