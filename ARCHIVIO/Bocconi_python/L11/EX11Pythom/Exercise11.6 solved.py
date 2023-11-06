import random

print('Let\'s play "heads or tails" with a "virtual" coin')
choice = input("Make your choice: heads (H) or tails (T)? ")

rnd_num = random.randint(1, 2)

if rnd_num == 1:
    toss = 'HEADS'
else:
    toss = 'TAILS'

if (choice=='H' and rnd_num==1) or (choice=='T' and rnd_num==2):
    outcome = "WON"
else:
    outcome = "LOST"

print("The outcome of the virtual coin is " + toss + " so you " + outcome)
