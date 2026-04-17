import random

def main():
    level = get_level("Level: ")
    correct_number = random.randint(1, level)
    guessing_game("Guess: ", correct_number)

def get_level(prompt1):
    while True:
        try:
            level = int(input(prompt1))
        except ValueError:
            pass
        else:
            if level > 0:
                return level
            else:
                pass

def guessing_game(prompt2, correct):
    while True:
        try:
            guess = int(input(prompt2))
        except ValueError:
            pass
        else:
            if guess < 1:
                continue
            else:
                if guess < correct:
                    print("Too small!")
                    continue
                elif guess > correct:
                    print("Too large!")
                    continue
                else:
                    print("Just right!")
                    break

main()
