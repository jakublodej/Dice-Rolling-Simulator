import random
import time
min = 1
rolling = 'y'
while rolling is 'y':
    max_num = input('How many sides do you need on the dice? :')
    max=int(max_num)
    dice = int(input('How many dices do you need to roll? :'))
    print('Rolling the dices ...')
    time.sleep(2)
    print("Your numbers are :")
    
    for number in range(0,dice):
        num_current=random.randint(min,max)
        print(num_current)
    rolling=input('Would you like to roll again? y/n : ')