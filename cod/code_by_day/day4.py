import random

choice = int(input("Welcome to RPS, Enter 0 for rock, 1 for paper, and 2 for scissor\n"))
cp_choice = random.randint(0, 2)

print(f"Computer chose {cp_choice}")

if choice == cp_choice:
    print("It's a tie")
    
elif (choice == 0 and cp_choice == 2) or \
     (choice == 1 and cp_choice == 0) or \
     (choice == 2 and cp_choice == 1):
    print("You win")
else:
    print("You lose")