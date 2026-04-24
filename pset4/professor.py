import random


def main():
    level = get_level()

    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        errors = 0
        for j in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                errors += 1
                continue
            else:
                if z == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    errors += 1
        if errors == 3:
            print(f"Correct answer: {x} + {y} = {correct}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2 or 3.")



if __name__ == "__main__":
    main()
