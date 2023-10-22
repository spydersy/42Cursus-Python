import sys

if len(sys.argv) > 1:
    rev = sys.argv[1:]
    rev.reverse()
    print(rev)