#File: chaosPratice.py
#A simple program illustrating chaotic behaviour

def main ():
    print("This program illustrates a chaotic function")
    x = eval (input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 3.9 * (x - x * x)
        print (x)
main ()
