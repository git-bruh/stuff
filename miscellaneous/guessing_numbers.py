import random


def guess_number():
    print("Guess a number from 0 - 9")
    special_number = random.randint(0, 9)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        try:
            guess = int(input("Guess : "))
            guess_count += 1
            if guess > special_number:
                print("Lower!")
            elif guess < special_number:
                print("Higher!")
            elif guess == special_number:
                print("You Won!")
                break
        except ValueError:
            print("That doesn't seem like a number, try again!")
    else:
        print(f"""
You Lost...
The special number was {special_number}
""")


guess_number()
