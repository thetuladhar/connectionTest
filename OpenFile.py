# 1. Generate two random option from the game data.
#    Note: solutions/higherLowerGame/game_data.py has game data.
import random
from game_data import data


# 2. Format account data into printable format.
def getName(input):
   return (input["name"])

#Use: Get follower count.
def getFollow(input):
   return (input["follower_count"])
# 5. Keep the score
score=0

#choose OPTION A-B outside the loop
option_a = random.choice(data)
option_b = random.choice(data)

# 6. Make game repeatable.
while True:

    print(getName(option_a),"versus",getName(option_b))
    #fllower checker
    #print(getFollow(option_a),getFollow(option_b))
    # 3. Ask user for a guess.
    entry=input("Guess who has more followers? Type A or B :").lower()

    # 4. Check if user is correct.
    if entry =='a' and getFollow(option_a) > getFollow(option_b):
        score +=1
        print("CORRECT , Your current score is",score)
    elif entry =='b' and getFollow(option_a) < getFollow(option_b):
        score +=1
        print("CORRECT , Your current score is",score)

    elif entry =='esc':
        print("Your final score is",score)
        break
    else:
        print("INCORRECT, Your current score is",score)

    # 7. Make B become the next A.
    option_a = option_b
    option_b = random.choice(data)
