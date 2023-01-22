
def text_analyzer(text = None):
    upper  = 0
    lower = 0
    punctuation = 0
    spaces = 0

    if text == None:
        text = str(input("Please provide a string: "))
    if not isinstance(text, str):
        print("Error: argument must be a string.")
        return
    for c in text:
        if c.isupper():
            upper +=1
        elif c.islower():
            lower += 1
        elif c.isspace():
            spaces += 1
        elif c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punctuation += 1
    print(f"- {upper} upper letter(s)\n- {lower} lower letter(s)\n- {punctuation} punctuation mark(s)\n- {spaces} space(s)")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv) > 2:
        print("Error: only one argument allowed.")
    else:
        text_analyzer()