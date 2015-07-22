# stringMethods.py
# Created by Jo Narvaez-Jensen

def main ():
    s = "today is a great day in July."

    print ("capitalize:", s. capitalize())
    print ("title:", s.title())
    print ("lower:", s.lower())
    print ("upper:", s.upper())
    print ("center: ", s.center(40))
    print ("ljust:", s.ljust(40))
    print ("rjust:", s.rjust(40))
    print ("count(day):", s.count("day"))
    print ("count(a):", s.count("a"))
    print ("sfind(great):", s.find("great"))
    print ("rfind(great):", s.rfind("great"))
    print ("sfind(a):", s.find("a"))
    print ("rfind(a):", s.rfind("a"))
    sR=s.replace( "today"  ,   "              ")
    print ("replace:", sR)
    sLS=sR.lstrip()
    print ("lstrip:", sLS)
    sJ = " ".join(["Everyday",s])
    print ("join:", sJ)
    sR2=s.replace("in July." , "                 "  )
    print ("replace2:", sR2)
    sRS=s.rstrip()
    print ("rstrip:", sRS)
    sJ2=" ".join([ s , "."])
    print ("join2:", sJ2)

main ()
