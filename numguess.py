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


def choice():
  n_guess=int(input('Choose again: '))
  guess = n_guess
  return guess


def correct():
      print('*********************')
      sleep(1)
      print('*********************')
      sleep(1)
      print('*********************')
      sleep(1)
      return print("Correct! You got the right answer!")

def wrong():
  if guess > answer:
      print('Wrong! The answer is lower than you enter')
  elif guess < answer:
      print('Wrong! The answer is higher than you enter')



for i in range(3):
  if guess == answer:
    correct()
    break
  else:
    wrong()
    guess = choice()    
