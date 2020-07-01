import random


rps = ['Rock', 'Paper', 'Scissors']
computer = random.choice(rps).title()

user = False

while user == False:
    user = input('Rock, Paper, Scissors... ').title()
    if user == computer:
        print('Tie!')
    elif user == 'Rock':
        if computer == 'Paper':
            print(f"You Lost... {computer} Covers {user}")
        else:
            print(f"You Won... {user} Smashes {computer}")
    elif user == 'Paper':
        if computer == 'Rock':
            print(f"You Won... {user} Covers {computer}")
        else:
            print(f"You Lost... {computer} Cuts {user}")
    elif user == 'Scissors':
        if computer == 'Rock':
            print(f"You Lost... {computer} Smashes {user}")
        else:
            print(f"You Lost... {user} Cuts {computer}")
    else:
        print("Invalid Input... Try Again")
    user = False
    computer = random.choice(rps).title()