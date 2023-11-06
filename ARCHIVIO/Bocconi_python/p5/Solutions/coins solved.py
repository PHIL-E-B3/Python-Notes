
import random

heads = 0
tails = 0

n_tosses = int(input('How many tosses you want to simulate? '))


for toss in range(n_tosses):
    random_nr = random.randint(0,1)
    if random_nr == 0:
        heads = heads + 1
    else:
        tails = tails + 1

print('Number of heads tosses =', heads, '\nNumber of tails tosses =', tails)




















