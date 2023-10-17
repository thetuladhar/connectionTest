import random

#run game for ten times
for i in range(10):
    user_choice=int(input("Rock|0|Paper|1|Scissors|2| :"))

    choices=[0 , 1 , 2]

    computer_choice= random.choice(choices)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
            (user_choice == 2 and computer_choice == 1) or \
            (user_choice == 3 and computer_choice == 2):
        print("You win!") 
    else:
        print("Computer wins!")
    
    