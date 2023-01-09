from random import randint

# Generate answer
answer =randint(1, 100)

# Print answer for debugging
print(answer)

# User interaction
username =input("Hello! What your name?")
print(f"Nice to meet you,{username}! Please be my guest!")
guess = int(input(f"So {username}, Guess the number(1~100): "))
print(f"Good job {username}! You got the right answer!)
