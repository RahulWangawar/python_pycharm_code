n = 34
t = 9
print("You have 9 tries to guess")
while(t>1):
    guessed_num = int(input("Guess a number "))
    if guessed_num > n:
        print(f'"Number is less than {guessed_num}"')
    elif guessed_num < n:
        print(f'"Number is greater than {guessed_num}"')
    else:
        print("Congrats , You guessed it right")
        print(f'"Number of guesses you did : {10-t}"')
        print()
        break
    t = t - 1
    print("number of guesses left=",t )
print("Game Over,Try again")
