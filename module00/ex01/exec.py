import sys

if len(sys.argv) > 1:
    arguments = sys.argv[1::]
    merged_arguments = ' '.join(arguments)    
    reversed_arguments = merged_arguments[::-1]
    swapped_case_string = reversed_arguments.swapcase()
    print(swapped_case_string)
