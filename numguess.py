from random import randint
from time import sleep

# Generate answer
answer =randint(1, 100)

# Print answer for debugging
print(answer)

# User interaction
username =input("Hello! What your name?")
print(f"Nice to meet you,{username}! Please be my guest!")
guess = int(input(f"So {username}, Guess the number(1~100): "))
print(f"Good job {username}! You picked {guess}")

if guess == answer:
    print('*********************')
    sleep(1)
    print('*********************')
    sleep(1)
    print('*********************')
    sleep(1)
    print("Correct! You got the right answer!")
elif guess > answer:
    print('Wrong! The answer is lower than you enter')
elif guess < answer:
    print('Wrong! The answer is higher than you enter')

