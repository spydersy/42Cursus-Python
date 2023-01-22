import sys

def operations(A, B):
    print(f"Sum: {A+B}\nDifference: {A-B}\nProduct: {A*B}")
    try:
        print(f"Quotient: {A/B}")
    except:
        print("Quotient: ERROR (division by zero)")
    try:
        print(f"Remainder: {A%B}")
    except:
        print("Remainder: ERROR (modulo by zero)")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print("AssertionError: too many arguments")
        try:
            operations(int(sys.argv[1]), int(sys.argv[2]))
        except:
            print("AssertionError: only integers")
    elif len(sys.argv) < 3:
        print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    elif len(sys.argv) > 3:
        print("AssertionError: too many arguments")