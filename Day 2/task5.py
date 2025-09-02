# Small Challenge
# guess the number
secret_number = 10 # you can change this number to any number you want
guess = 0 # initial guess is 0
while guess != secret_number: # keep running the loop until the guess is equal to secret number
    guess = int(input("Guess the number btw 1-10")) # take input from user
    if guess < secret_number:  # if guess is less than secret number
        print("Too low") 
    elif guess > secret_number: # if guess is greater than secret number
        print("Too high")
    else: # if guess is equal to secret number
        print("You guessed it right!")