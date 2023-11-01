from random import randint

# Colors definition:
OKGREEN_COLOR = '\033[92m'
FAIL_COLOR = '\033[93m'
BOLD_COLOR = '\033[1m'
ENDC_COLOR = '\033[0m'

welcome_message = BOLD_COLOR + '''\
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n\
''' + ENDC_COLOR
prompt = BOLD_COLOR + '''\
What\'s your guess between 1 and 99?
>> \
''' + ENDC_COLOR
goodbye_message = OKGREEN_COLOR + 'Goodbye!' + ENDC_COLOR
not_a_number = FAIL_COLOR + 'That\'s not a number.\n' + ENDC_COLOR
too_high = FAIL_COLOR + 'Too high!\n' + ENDC_COLOR
too_low = FAIL_COLOR + 'Too low!\n' + ENDC_COLOR
win = OKGREEN_COLOR + '''\
Congratulations, you've got it!
You won in {} attempts!\
''' + ENDC_COLOR

def guess():
    print(welcome_message)
    random_number = randint(1, 99)
    number_of_guesses = 0
    while True:
        print(prompt, end='')
        user_guess = ''
        try:
            user_guess = input()
            user_guess = int(user_guess)
            if user_guess == random_number:
                print(win.format(number_of_guesses))
                break
            elif user_guess > random_number:
                print(too_high)
            else:
                print(too_low)
            number_of_guesses += 1
        except:
            print('dbg: ' + user_guess)
            if user_guess == 'exit':
                print(goodbye_message)
                break
            else:
                print(not_a_number)
                continue

if __name__ == '__main__':
    guess()