import sys

if len(sys.argv) > 1:
    arr = sys.argv[1:]
    arr.reverse()
    x = ' '.join(arr)
    print(x.swapcase())