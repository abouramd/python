rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

moves = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
index = int(input())
if index in range(0, 3):
    print(moves[index])
    print("Computer chose:")
    indexc = random.randint(0, 2)
    print(moves[indexc])

    lose_message = "You lose"

    if index == indexc:
        print("It's a Draw ;)")
    elif index == 0 and indexc == 1:
        print(lose_message)
    elif index == 1 and indexc == 2:
        print(lose_message)
    elif index == 2 and indexc == 0:
        print(lose_message)
    else:
        print("You win")
else:
    print("Invalid number, you lose!")