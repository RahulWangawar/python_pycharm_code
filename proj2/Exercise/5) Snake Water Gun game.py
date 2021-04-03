# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and water damages gun


def print_comp_win_result(_input, _random, computer_point, human_point):
    print(f"your guess {_input.lower()} and computer guess is {_random} \n")
    print("computer wins 1 point \n")
    print(f"computer_point is {computer_point} and your point is {human_point} \n ")

def print_human_win_result(_input, _random, computer_point, human_point):
    print(f"your guess {_input.lower()} and computer guess is {_random} \n")
    print("Human wins 1 point \n")
    print(f"computer_point is {computer_point} and your point is {human_point} \n")


import random

lst = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input.lower() == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input.lower() == "s" and _random == "g":
        computer_point = computer_point + 1
        print_comp_win_result(_input, _random, computer_point, human_point)


    elif _input.lower() == "s" and _random == "w":
        human_point = human_point + 1
        print_human_win_result(_input, _random, computer_point, human_point)


    # if user enter w
    elif _input.lower() == "w" and _random == "s":
        computer_point = computer_point + 1
        print_comp_win_result(_input, _random, computer_point, human_point)

    elif _input.lower() == "w" and _random == "g":
        human_point = human_point + 1
        print_human_win_result(_input, _random, computer_point, human_point)
    # if user enter g

    elif _input.lower() == "g" and _random == "s":
        human_point = human_point + 1
        print_human_win_result(_input, _random, computer_point, human_point)


    elif _input.lower() == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}")
    print("-   -   -   -   -   -   Try Again   -   -   -   -   -   -   -   \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")



