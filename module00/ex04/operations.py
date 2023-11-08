import sys

# Colors definition:
OKGREEN_COLOR = '\033[92m'
FAIL_COLOR = '\033[93m'
BOLD_COLOR = '\033[1m'
ENDC_COLOR = '\033[0m'

too_many_arguments_error = FAIL_COLOR + 'AssertionError: too many arguments' + ENDC_COLOR
missing_argument_error = FAIL_COLOR + 'AssertionError: Missing argument' + ENDC_COLOR
not_a_number_error = FAIL_COLOR + 'AssertionError: only integers' + ENDC_COLOR
division_by_zero_error = FAIL_COLOR + 'ERROR (division by zero)' + ENDC_COLOR
module_by_zero_error = FAIL_COLOR + 'ERROR (modulo by zero)' + ENDC_COLOR

usage_text = FAIL_COLOR + '''
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
''' + ENDC_COLOR

result = '''\
Sum:        {}
Difference: {}
Product:    {}
Quotient:   {}
Remainder:  {}
'''

if len(sys.argv) == 1:
    print(usage_text)
elif len(sys.argv) > 3:
    print(too_many_arguments_error)
elif len(sys.argv) < 3:
    print(missing_argument_error)
else:
    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        print(result.format(A + B,
                            A - B,
                            A * B,
                            division_by_zero_error if B == 0 else A / B,
                            module_by_zero_error if B == 0 else A % B))
    except:
        print(not_a_number_error)
