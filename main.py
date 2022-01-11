import random

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
---'   ______)____
          ________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rps = [rock, paper, scissors]

if my_choice > 2:
    print("YOU Chosen wrong number, Computer Won")
else:
    print("You chosen")
    print(rps[my_choice])
computer_chooses = random.randint(0, 2)
print("Computer Chosen")
print(rps[computer_chooses])

if computer_chooses == 0 and my_choice == 2:
    print("Computer wins")

elif computer_chooses == 2 and my_choice == 1:
    print("Computer wins")

elif computer_chooses == 1 and my_choice == 0:
    print("Computer wins")
# ----------------------------------------------
elif computer_chooses == 2 and my_choice == 0:
    print("You win")

elif computer_chooses == 1 and my_choice == 2:
    print("You win")

elif computer_chooses == 0 and my_choice == 1:
    print("You win")
# ---------------------------------------------
elif computer_chooses == 0 and my_choice == 0:
    print("Game Tied")

elif computer_chooses == 1 and my_choice == 1:
    print("Game Tied")

elif computer_chooses == 2 and my_choice == 2:
    print("Game Tied")
