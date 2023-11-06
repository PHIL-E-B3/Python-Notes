import math

# Now we'll talk about the Negative Binomial Probability. While the
# geometric model finds the number of trails required for success,
# number of dice rolls before you get 6. * The negative binomial
# model finds the number of trials until the nth success. For
# example how many rolls are required until you get 3 sixes. * The
# conditions are that you must have independent random trials with
# either a pass or fail. The probability of success is equal for
# each trial. Finally you must keep track of the number of trials
# up to the target success.

# Very often the most confusing decision is based on which formula
# you should use and when. The Binomial Model is used when you want
# to count the number of successes with a fixed number of trials. *
# The Negative Binomial Model counts the number of trials required
# to find a fixed number of successes. * Finally the Geometric
# Model is used to find the number of trials required for 1 success.

# Here is the formula for the negative binomial. p is the
# probability of success, k is the number of successes we I'm to
# have. n is the number of trials. * Now let's say we want to
# calculate the probability of rolling 3 sixes in 10 rolls. * First
#  we have to find the number of combinations taking 3 from 10 with
# repetition which works out to 220. * Then we plug in all other
# values to find a probability of 28%

# You can see here our probability of rolling 3 sixes maximizes at
# 15 rolls at .354. Then it starts falling. Can you guess why? Well
# if our goal is to get 3 sixes at some point we have an increased
# probability of rolling 4 sixes which is not what we want.


def combination_with_rep(total_items, items_to_pick):
    numerator = math.factorial(items_to_pick + total_items - 1)
    denominator = math.factorial(items_to_pick) * math.factorial(total_items - 1)
    return numerator / denominator


def negative_binomial(success_prob, success_goal, trial):
    combinations = combination_with_rep(trial, success_goal)
    success_prob_pow = pow(success_prob, success_goal)
    fail_prob_pow = pow(1 - success_prob, (trial - success_goal))
    return combinations * success_prob_pow * fail_prob_pow


def negative_binomial_range():
    success_prob = float(input("What is the Probability of Success : "))
    success_goal = int(input("What is the Success Goal : "))
    num_trials = int(input("Max Number of Trials : "))
    for trial in range(success_goal, num_trials + 1):
        print("Probability with Trial {:d} : {:.4f}".format(trial, negative_binomial(success_prob, success_goal, trial)))


negative_binomial_range()

# Hypergeometric Distribution is used with samples without replacement
# to find the probability a specific number of items fit a defined
# characteristic. * With Binomial and Hypergeometric you find how
# many people have a characteristic. Replacement defines which to use.

# The required conditions are that you sample without replacement.
# Population has an equal chance of being sampled. Population is in
# 2 groups being those with the important characteristic and those
# without it. The number of people with the characteristic and the
# total population size must be known. x represents the total number
# of people you're interested in.

# Here is the formula used to calculate Hypergeometric Distribution
# Probabilities. I provide a pictogram to help explain the parts.

# Here I'll work through an example. What is the probability of
# getting 2 black cards if I draw 5 from a deck without replacement?
# There are 26 possible black or success cards. There are 2 successes
# in my sample. The total number of cards is 52. Finally I'm drawing
# 5 cards for the whole sample. * If I find the combinations for the
# formula and work through it you'll see I have a .325 probability
# of success.

# I'll calculate the expected value which is the number of successes
# you expect in the sample. When I plug in the values I get 2.5.
# * Then I'll find Variance which is the average deviation from the
# mean over the long term. And, if you plug in those values and work
# them out you'll find you get a value of 1.15

def combination_without_rep(total_items, items_to_pick):
    numerator = math.factorial(total_items)
    denominator = math.factorial(items_to_pick) * math.factorial(total_items - items_to_pick)
    return numerator / denominator


# Receives the total population, successes in population,
# total number of samples and successes in the sample and
# finds the probability that the sample will have a specific
# number of successes
def hypergeometric_distribution(population, pop_success, total_sample, samp_success):
    numerator_1 = combination_without_rep(pop_success, samp_success)
    numerator_2 = combination_without_rep(population - pop_success, total_sample - samp_success)
    numerator = numerator_1 * numerator_2
    denominator = combination_without_rep(population, total_sample)
    return numerator/denominator


# Handles input and output for Hypergeometric Distribution
def get_hypergeometric_distribution():
    population = int(input("What is the Total Population : "))
    pop_success = int(input("How Many Possible Successes are There in the Population : "))
    total_sample = int(input("What is your Sample Size : "))
    samp_success = int(input("How Many Successes do you Expect in the Sample : "))
    print("The Hypergeometric Distribution Probability : {:.4f}".format(hypergeometric_distribution(population, pop_success, total_sample, samp_success)))
    expected_val = total_sample * (pop_success / population)
    print("Expected Value : {:.4f}".format(expected_val))
    variance = (total_sample * pop_success) / (population ** 2 * (population - 1))
    print("Variance : {:.4f}".format(variance))


get_hypergeometric_distribution()


# Independent Event Probability
# Mutually Exclusive Probability
# Total Probability
# Bayes' Theorem 1 and 2
# Permutations
# Variations
# Exponential Distribution











