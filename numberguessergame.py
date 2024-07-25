## Guess The Number

import random

difficulty = int(input('Please input the numerical value of the difficulty you want:\n1) Easy\n2) Medium\n3) Hard\n'))

if difficulty == 1:
    print('You have chosen Easy mode! You will get 3 chances to guess a number between 1-10!')
    enter = input('Press enter to continue:')
elif difficulty == 2:
    print('You have chosen Medium mode! You will get 5 chances to guess a number between 1-50!')
    enter = input('Press enter to continue:')
elif difficulty == 3:
    print('You have chosen Hard mode! You will get 7 chances to guess a number between 1-100!')
    enter = input('Press enter to continue:')

if difficulty == 1:
    chances = 0
    random_number = random.randint(1, 10)
    while chances < 3:
        user_guess = int(input('\nPlease input your guess:\n'))
        if user_guess == random_number:
            print('Congrats! You guessed the correct number! You won!')
            chances = 3
            exit()
        elif user_guess > random_number:
            print('Your guess is too high! Try again')
            chances += 1
        elif user_guess < random_number:
            print('Your guess is too low! Try again')
            chances += 1

    print(f'You didnt guess the correct number! The correct number was {random_number}. Try again next time!')

elif difficulty == 2:
    chances = 0
    random_number = random.randint(1, 50)
    while chances < 5:
        user_guess = int(input('\nPlease input your guess:\n'))
        if user_guess == random_number:
            print('Congrats! You guessed the correct number! You won!')
            exit()
        elif user_guess > random_number:
            print('Your guess is too high! Try again')
            chances += 1
        elif user_guess < random_number:
            print('Your guess is too low! Try again')
            chances += 1

    print(f'You didnt guess the correct number! The correct number was {random_number}. Try again next time!')

elif difficulty == 3:
    chances = 0
    random_number = random.randint(1, 100)
    while chances < 7:
        user_guess = int(input('\nPlease input your guess:\n'))
        if user_guess == random_number:
            print('Congrats! You guessed the correct number! You won!')
            chances = 7
            exit()
        elif user_guess > random_number:
            print('Your guess is too high! Try again')
            chances += 1
        elif user_guess < random_number:
            print('Your guess is too low! Try again')
            chances += 1

    print(f'You didnt guess the correct number! The correct number was {random_number}. Try again next time!')
