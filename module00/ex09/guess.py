import random

def play_game():
    rand = random.randint(1, 99)
    count = 1
    rangeError = "Invalid input. Please enter a number between 1 and 99."
    done = """Congratulations, you've got it!
You won in {} attempts!"""
    goodbye = "Goodbye!"
    prompt = """What's your guess between 1 and 99?
>> """
    while True:
        guess = input(prompt)
        if guess == 'exit':
            print(goodbye)
            exit()
        try:
            if not (0 < int(guess) and int(guess) < 100):
                print(rangeError)
                count += 1
            elif int(guess) == rand:
                print(done.format(count))
                break
            elif int(guess) > rand:
                print("Too high!")
                count += 1
            else:
                print("Too low!")
                count += 1
        except:
            print("That's not a number.")

if __name__ == '__main__':
    intro = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n"""
    print(intro)
    play_game()