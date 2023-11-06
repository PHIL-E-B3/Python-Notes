import math
from functools import reduce

# Now we finish up by covering Exponential Distribution.
# Before moving on though I want to define what an Exponential
# Function is for those that don't know. It is simply a
# function of the form ab to the power of x where b is a
# positive number and x occurs as an exponent.

# An Exponential Distribution is used for a Continuous
# Distribution, like we just saw, whose probability density
# has the shape of an Exponential Function. * This distribution
# is often used to model the time elapsed between events.

# A Density Function of the form f(x) = lambda e to the power
# of negative lambda times x where x is greater than or equal
# to 0 and lambda is constant. Lambda in this situation is
# called the parameter of the exponential distribution.
# * A large lambda caused the slope of the curve to drop
# quickly to zero and vice versa. * And like previously the
# probability of an Exponential Distribution is the area
# under the curve.

# There are 3 formulas for calculating Exponentials. You
# use different versions if x is less than, greater than or
# lies between values a and b.

# In the next few slides I'll calculate differing
# probabilities based of less than, greater than or lies
# between values of a and b. Here also is how to calculate
# Expected Value and Variance


# Get exponential probability greater than or less than
# a value
def exponential_distribution(lambda_val, x, direction):
    if direction == "l":
        ed = 1 - (math.e ** (-1 * lambda_val * x))
        return ed
    else:
        ed = math.e ** (-1 * lambda_val * x)
        return ed


# Get exponential probability between 2 values
def exponential_distribution_range(lambda_val, x, a, b):
    ed = (math.e ** (-1 * lambda_val * a)) - (math.e ** (-1 * lambda_val * b))
    return ed


def get_exponential_distribution():
    lambda_val = float(input("What is Lambda : "))
    x = float(input("What is X : "))
    range_bool = input("Calculate a Range (Y or N) : ")
    if range_bool[0].lower() == "y":
        a = float(input("What is a : "))
        b = float(input("What is b : "))
        ed = exponential_distribution_range(lambda_val, x, a, b)
        print(f"Probability of Success between {a} and {b} : {ed}")

    else:
        direction = input("Find Exponential Greater Than or Less Than (G or L) : ")
        ed = exponential_distribution(lambda_val, x, direction[0].lower())
        print(f"Probability of Success : {ed}")

    print(f"Expected Value : {1/lambda_val}")


# get_exponential_distribution()


# Get independent event probabilities by multiplying the
# probabilities
def independent_event_probability():
    print("Enter Independent Event Probabilities or Q")
    final_prob = 1
    while True:
        prob = input("Probability : ")
        if prob.lower() != "q":
            final_prob *= float(prob)
        else:
            break
    return "{:.4f}".format(final_prob)


# Odds of rolling a 1 and then a 2 : .167 x .167
# print(f"Independent Probability : {independent_event_probability()}")

# Probabilities based on multiple events
def total_probability():
    event_num = 1
    tot_prob = 0
    print("Enter Probabilities for Each Event Separated with Commas")
    while True:
        probs = input(f"Enter Event {event_num}s Probabilities or Q : ")
        if probs.lower() == "q":
            print(f"Total Probability : {tot_prob}")
            break
        else:
            # Replace all whitespace in string
            probs.replace(" ", "")
            # Convert to list
            prob_list = probs.split(",")
            # Multiply all values in the list
            prob_product = reduce(lambda x, y: float(x)*float(y), prob_list)
            # Adds product of probabilities to total probability
            tot_prob += prob_product
            event_num += 1


# If one course of action succeeds 95% of the time and it is tried
# by 60% of people. And, we have another that succeeds 85% of the
# time and it is tried by the other 40%. What is the probability
# of success for any participants?
# total_probability()

# Used when order matters versus combinations which don't
# care about order, but only who makes it
def variation_without_repetition(tot_items, items_picked):
    numerator = math.factorial(tot_items)
    denominator = math.factorial(tot_items-items_picked)
    return numerator / denominator


print(f"Variation without Repetition : {variation_without_repetition(5, 3)}")


def variation_with_repetition(tot_items, items_picked):
    return tot_items ** items_picked


print(f"Variation with Repetition : {variation_with_repetition(10, 3)}")






