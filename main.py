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
my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
my_choice = int(my_choice)

if my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
else:
  print(scissors)

print("\n")
print("Computer chose:\n")
comp_choice = random.randint(0,2)
print(comp_choice)

if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
else:
  print(scissors)

if my_choice == 0 and comp_choice == 2:
  print("You win")
elif my_choice == 2 and comp_choice == 1:
  print("You win")
elif my_choice == 1 and comp_choice == 0:
  print("You win")
elif my_choice == comp_choice:
  print("It's draw")
else:
  print("You lose")
