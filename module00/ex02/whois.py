import sys

number_is_zero = 'I\'m Zero.'
number_is_even = 'I\'m Even.'
number_is_odd = 'I\'m Odd.'
more_than_one_argument_error = 'AssertionError: more than one argument are provided'
not_a_number_error = 'AssertionError: argument is not an integer'

if len(sys.argv) == 1:
    exit(1)
elif len(sys.argv) > 2:
    print(more_than_one_argument_error)
    exit(1)
else:
    try:
        number = int(sys.argv[1])
        print(number_is_zero if number == 0 else (number_is_even if number % 2 == 0 else number_is_odd))
    except:
        print(not_a_number_error)