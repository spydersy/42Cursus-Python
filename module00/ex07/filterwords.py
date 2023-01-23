import sys
import string

def filter_words(S, N):
    S = S.translate(str.maketrans('', '', string.punctuation))

    words = [word for word in S.split() if len(word) > N]
    print(words)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('ERROR')
        exit()
    try:
        filter_words(sys.argv[1], int(sys.argv[2]))
    except:
        print('ERROR')
