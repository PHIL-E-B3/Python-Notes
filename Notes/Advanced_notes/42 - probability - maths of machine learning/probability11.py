import math

# Poisson (pwa san) Distributions focus on the probability a
# specific number of events will occur over time, distance,
# area, etc. Visits to website per hour, day. Number of pizzas
# sold. Red cars seen. Vegetables expected for harvest. * The
# conditions include that you count occurrences over time,
# distance, area. The mean occurrence must be the same over a
# similar time, area, etc. Count occurrences over an interval
# can't depend on other intervals. And, intervals can't overlap.

# This is the Poisson Probability Mass Function. k equals
# the number of times an event occurs. λ (Lambda) equals the
# average number of events per interval. e is Euler's Number
# (Oiler) 2.71828...

# If we know the average number of points scored by a Baseball
# team is 4.82 I can then calculate the probability of the
# expected number of runs per game. The Expected Value and
# Variance are both equal to λ or 4.82 in this situation.


# Will calculate Poisson Probability Mass from 0 to max_value
def poisson_pmf(lambda_val, k):
    numerator = (lambda_val ** k) * (math.e ** (-1 * lambda_val))
    denominator = math.factorial(k)
    return numerator/denominator


def poisson_pmf_range():
    max_value = int(input("Max Value to Calculate : "))
    lambda_val = float(input("Expected Average : "))
    for k in range(0, max_value + 1):
        p_pmf = poisson_pmf(lambda_val, k)
        print("Poisson {:d} : {:.4f}".format(k, p_pmf))


poisson_pmf_range()


# Geometric Probability calculates the probability of success
# depending on the number of trials. For example how many dice
# rolls are required to get a 6? * The conditions for using it
# include that trails must be independent, outcomes are pass or
# fail, probability of success must be constant and the number
# of trails need not be fixed like with binomials. * As you can
# see we are multiplying the probability of success by the
# probability of failure to the power of the number of trials
# minus 1.

# To find the probability of rolling a 6 in 3 dice rolls
# multiply the probability of a roll .167 by the failure
# probability .833 taken to the power of trails minus 1. * You
# see that that is .116. * If you want to find the probability
# of success in 3 or less rolls sum all previous probabilities
# which works out to .422.

# We can find the probability that it will take more than 3 dice
# rolls simply by subtracting the previous probability from 1. *
# We can calculate how many dice rolls it will take to get a
# success. This is called the mean and we can see success is
# expected in 6 dice rolls. * I also show how to calculate
# variance and standard deviation.

# Calculates Geometric Probability when provided with success probability
# and the trial to check for success
def geometric_probability(success_prob, trial_to_check):
    fail_prob = 1 - success_prob
    return success_prob * (fail_prob ** (trial_to_check - 1))


# Handles input and out put for Geometric Probability for One Trial
def trial_geometric_probability():
    success_prob = float(input("What is the Probability of Success : "))
    trial_to_check = int(input("On Which Trial Should I check for Success : "))
    print("Probability of Success on Trial {:d} is {:.3f}".format(trial_to_check, geometric_probability(success_prob, trial_to_check)))


# Handles input and output for Geometric Probability for Multiple of Trials
def geometric_probability_multiple_trials():
    success_prob = float(input("What is the Probability of Success : "))
    max_trial = int(input("Up to Which Trial Should I check for Success : "))
    prob_sum = 0
    for i in range(1, max_trial + 1):
        prob_sum += geometric_probability(success_prob, i)

    print("Probability of Success After {:d} Trials : {:.3f}".format(max_trial, prob_sum))
    print("Probability of Success > {:d} Trials : {:.3f}".format(max_trial, 1 - prob_sum))
    print(f"Expected Success on Trial {1/success_prob}")
    standard_deviation = math.sqrt((1 - success_prob) / (success_prob ** 2))
    print(f"Standard Deviation : {standard_deviation}")


trial_geometric_probability()
geometric_probability_multiple_trials()


