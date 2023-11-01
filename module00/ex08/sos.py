from sys import argv
from string import punctuation

# Colors definition:
OKGREEN_COLOR = '\033[92m'
FAIL_COLOR = '\033[93m'
BOLD_COLOR = '\033[1m'
ENDC_COLOR = '\033[0m'

# Program messages:
arguments_error_message = FAIL_COLOR + 'Please provide a message to encode.' + ENDC_COLOR
error_message = FAIL_COLOR + 'Please provide a valid message to encode.' + ENDC_COLOR

# Morse code dictionary:
morse_code = {
    'A':	'.-',
    'B':	'-...',
    'C':	'-.-.',
    'D':	'-..',
    'E':	'.',
    'F':	'..-.',
    'G':	'--.',
    'H':	'....',
    'I':	'..',
    'J':	'.---',
    'K':	'-.-',
    'L':	'.-..',
    'M':	'--',
    'N':	'-.',
    'O':	'---',
    'P':	'.--.',
    'Q':	'--.-',
    'R':	'.-.',
    'S':	'...',
    'T':	'-',
    'U':	'..-',
    'V':	'...-',
    'W':	'.--',
    'X':	'-..-',
    'Y':	'-.--',
    'Z':	'--..',
    '0':	'-----',
    '1':	'.----',
    '2':	'..---',
    '3':	'...--',
    '4':	'....-',
    '5':	'.....',
    '6':	'-....',
    '7':	'--...',
    '8':	'---..',
    '9':	'----.'
}

def morse_encode(message):
    '''Encodes a message into Morse code.'''
    message = message.upper()
    encoded_message = ''
    for letter in message:
        if letter in punctuation:
            print(error_message)
            return
        if letter == ' ': # Space
            encoded_message += '/ '
        elif letter in morse_code:
            encoded_message += morse_code[letter] + ' '
        else:
            print(error_message)
            return
    print(encoded_message)

if __name__ == '__main__':
    if len(argv) >= 2:
        morse_encode(' '.join(argv[1::]))
    else:
        print(arguments_error_message)
        '''----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .'''
        '''----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .'''