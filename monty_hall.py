from random import shuffle, choice

doors = [0,0,1] # 0:goat, 1:car
shuffle(doors)
#print(doors)
user_choice = choice(doors)
print(user_choice)
