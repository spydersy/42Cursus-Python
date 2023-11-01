import sys
from string import punctuation

# Colors definition:
OKGREEN_COLOR = '\033[92m'
FAIL_COLOR = '\033[93m'
BOLD_COLOR = '\033[1m'
ENDC_COLOR = '\033[0m'

# Program messages:
arguments_error_message = FAIL_COLOR + 'Please provide two arguments: a string and a positive integer.' + ENDC_COLOR
second_argument_error_message = FAIL_COLOR + 'The second argument must be a positive integer.' + ENDC_COLOR

def main():
    if len(sys.argv) != 3:
        print(arguments_error_message)
        return
    try:
        text = sys.argv[1].translate(str.maketrans('', '', punctuation))
        n = int(sys.argv[2])
        if n < 0:
            print(second_argument_error_message)
            return
        words = text.split()
        filtered_words = [word for word in words if len(word) > n]
        print(filtered_words)
    except ValueError:
        print(second_argument_error_message)
        return

    
if __name__ == '__main__':
    main()