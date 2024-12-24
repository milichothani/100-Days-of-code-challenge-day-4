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
import random
choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: \n"))
comp_choice = random.randint(0,2)
# print(f"Computer chose {comp_choice}")
if choice == 0:
    print("you chose: \n" , rock)
    print(f"Computer chose: ")
    if comp_choice == 0:
        print(rock, "Its a DRAW!")
    elif comp_choice == 1:
        print(paper, "You LOOSE :(")
    else:
        print(scissors, "you WIN!!")
elif choice == 1:
    print("You Choose: \n" , paper)
    print("Computer chose: ")
    if comp_choice == 0:
        print(rock , "You WIN!!")
    elif comp_choice == 1:
        print(paper, "Its a DRAW!!")
    else:
        print(scissors, "You LOOSE :(")
elif choice == 2:
    print("You chose: \n", scissors)
    print("Computer chose: ")
    if comp_choice == 0:
        print(rock, "You LOOSE :(")
    elif comp_choice == 1:
        print(paper, "youWIN!!")
    else:
        print(scissors, "Its a DRAW!!")
else:
    print("OOPS!! wrong choice!")

