import sys


if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) == 1:
    pass
else:
    print("AssertionError: more than one argument are provided")
