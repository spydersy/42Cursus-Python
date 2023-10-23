import sys
import string

not_a_string_error = 'AssertionError: argument is not a string'
more_than_one_argument_error = 'AssertionError: more than one argument are provided'
provide_a_string_prompt = 'What is the text to analyze?\n>> '

count_result = '''The text contains {} character(s):
- {} upper letter(s)
- {} lower letter(s)
- {} punctuation mark(s)
- {} space(s)
'''

def count_characters(text):
    upper_case_count = 0
    lower_case_count = 0
    punctuatio_mark_count = 0
    space_count = 0
    count_all = 0

    for i in range(len(text)):    
        upper_case_count += text[i].isupper()
        lower_case_count += text[i].islower()
        punctuatio_mark_count += text[i] in string.punctuation
        space_count += text[i] == ' '
        count_all += 1

    print(count_result.format(count_all,
                              upper_case_count,
                              lower_case_count,
                              punctuatio_mark_count,
                              space_count))

def text_analyzer(text = None):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if (text == None):
        text = str(input(provide_a_string_prompt))
    if isinstance(text, str):
        count_characters(text)
    else:
        print(not_a_string_error)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    if len(sys.argv) > 2:
        print(more_than_one_argument_error)
    else:
        text_analyzer()