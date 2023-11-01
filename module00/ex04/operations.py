import sys

too_many_arguments_error = 'AssertionError: too many arguments'
missing_argument_error = 'AssertionError: Missing argument'
not_a_number_error = 'AssertionError: only integers'
division_by_zero_error = 'ERROR (division by zero)'
module_by_zero_error = 'ERROR (modulo by zero)'

usage_text = '''
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3
'''

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
