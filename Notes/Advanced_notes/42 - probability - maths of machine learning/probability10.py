import re
import math

# We have been using Point Estimates so far which represent
# a singular point of data. The mean would be an example of
# a Point Estimate. * While point estimates are easy to
# calculate they can be inaccurate. An alternative is the
# use of an interval or range of values. * So if I have 3
# sample means taken from 3 different data sets I can
# create an interval that covers their range of values. * I
# then have to find how confident I am in that interval. We
# normally define normal confidence as 90%, 95%, or 99%. *
# That means if we have a confidence of 90% that we expect
# 9 out of 10 intervals to contain the mean value.

# When calculating our interval we take our sample mean and find the
# values of x and y by adding and subtracting the margin of error.
# Alpha is the doubt we have. So, if we have a confidence of 90% then
# alpha is 10%. n represents our sample size. We will use a Z Table
# again to find our interval.

# In this example I've gathered all our data. If we look up .025 on our
# Z Table we get .0580. * If we then plug in our data we find that x
# equals 42.97 * and y equals 43.029.

pos_z_code_list = [['.50000', '.50399', '.50798', '.51197', '.51595', '.51994', '.52392', '.52790', '.53188', '.53586'], ['.53983', '.54380', '.54776', '.55172', '.55567', '.55962', '.56356', '.56749', '.57142', '.57535'], ['.57926', '.58317', '.58706', '.59095', '.59483', '.59871', '.60257', '.60642', '.61026', '.61409'], ['.61791', '.62172', '.62552', '.62930', '.63307', '.63683', '.64058', '.64431', '.64803', '.65173'], ['.65542', '.65910', '.66276', '.66640', '.67003', '.67364', '.67724', '.68082', '.68439', '.68793'], ['.69146', '.69497', '.69847', '.70194', '.70540', '.70884', '.71226', '.71566', '.71904', '.72240'], ['.72575', '.72907', '.73237', '.73565', '.73891', '.74215', '.74537', '.74857', '.75175', '.75490'], ['.75804', '.76115', '.76424', '.76730', '.77035', '.77337', '.77637', '.77935', '.78230', '.78524'], ['.78814', '.79103', '.79389', '.79673', '.79955', '.80234', '.80511', '.80785', '.81057', '.81327'], ['.81594', '.81859', '.82121', '.82381', '.82639', '.82894', '.83147', '.83398', '.83646', '.83891'], ['.84134', '.84375', '.84614', '.84849', '.85083', '.85314', '.85543', '.85769', '.85993', '.86214'], ['.86433', '.86650', '.86864', '.87076', '.87286', '.87493', '.87698', '.87900', '.88100', '.88298'], ['.88493', '.88686', '.88877', '.89065', '.89251', '.89435', '.89617', '.89796', '.89973', '.90147'], ['.90320', '.90490', '.90658', '.90824', '.90988', '.91149', '.91309', '.91466', '.91621', '.91774'], ['.91924', '.92073', '.92220', '.92364', '.92507', '.92647', '.92785', '.92922', '.93056', '.93189'], ['.93319', '.93448', '.93574', '.93699', '.93822', '.93943', '.94062', '.94179', '.94295', '.94408'], ['.94520', '.94630', '.94738', '.94845', '.94950', '.95053', '.95154', '.95254', '.95352', '.95449'], ['.95543', '.95637', '.95728', '.95818', '.95907', '.95994', '.96080', '.96164', '.96246', '.96327'], ['.96407', '.96485', '.96562', '.96638', '.96712', '.96784', '.96856', '.96926', '.96995', '.97062'], ['.97128', '.97193', '.97257', '.97320', '.97381', '.97441', '.97500', '.97558', '.97615', '.97670'], ['.97725', '.97778', '.97831', '.97882', '.97932', '.97982', '.98030', '.98077', '.98124', '.98169'], ['.98214', '.98257', '.98300', '.98341', '.98382', '.98422', '.98461', '.98500', '.98537', '.98574'], ['.98610', '.98645', '.98679', '.98713', '.98745', '.98778', '.98809', '.98870', '.98899', '.98928'], ['.98956', '.98983', '.99010', '.99036', '.99061', '.99086', '.99111', '.99134', '.99158', '.99180'], ['.99202', '.99224', '.99245', '.99266', '.99286', '.99305', '.99324', '.99343', '.99361', '.99379'], ['.99396', '.99413', '.99430', '.99446', '.99461', '.99477', '.99492', '.99506', '.99520', '.99534'], ['.99547', '.99560', '.99573', '.99585', '.99598', '.99609', '.99621', '.99632', '.99643', '.99653'], ['.99664', '.99674', '.99683', '.99693', '.99702', '.99711', '.99720', '.99728', '.99736', '.99744'], ['.99752', '.99760', '.99767', '.99774', '.99781', '.99788', '.99795', '.99801', '.99807', '.99813'], ['.99819', '.99825', '.99831', '.99836', '.99841', '.99846', '.99851', '.99856', '.99861', '.99865'], ['.99869', '.99874', '.99878', '.99882', '.99886', '.99889', '.99893', '.99896', '.99900', '.99903'], ['.99906', '.99910', '.99913', '.99916', '.99918', '.99921', '.99924', '.99926', '.99929', '.99931'], ['.99934', '.99936', '.99938', '.99940', '.99942', '.99944', '.99946', '.99948', '.99950', '.99952'], ['.99953', '.99955', '.99957', '.99958', '.99960', '.99961', '.99962', '.99964', '.99965', '.99966'], ['.99968', '.99969', '.99970', '.99971', '.99972', '.99973', '.99974', '.99975', '.99976', '.99977'], ['.99978', '.99978', '.99979', '.99980', '.99981', '.99981', '.99982', '.99983', '.99983', '.99984'], ['.99985', '.99985', '.99986', '.99986', '.99987', '.99987', '.99988', '.99988', '.99989', '.99989'], ['.99990', '.99990', '.99990', '.99991', '.99991', '.99992', '.99992', '.99992', '.99992', '.99993'], ['.99993', '.99993', '.99994', '.99994', '.99994', '.99994', '.99995', '.99995', '.99995', '.99995'], ['.99995', '.99996', '.99996', '.99996', '.99996', '.99996', '.99996', '.99997', '.99997']]


# Finds area when provided the Z Code
def pos_z_code_area(z_code):
    # Breaks standard deviation into 3 numbers so we can use them to find
    # the area in the Z Table list
    # Ex. 1.23 -> [12][3]
    z_code_nums = re.findall("\d", str(z_code))
    first_z_code = int(z_code_nums[0] + z_code_nums[1])
    second_z_code = int(z_code_nums[2])
    return float(pos_z_code_list[first_z_code][second_z_code])

# Formula (x,y) = x̄ ± Z(α/2) * σ/√n
# x̄ : Sample Mean
# α : Alpha
# σ : Standard Deviation
# n : Sample Size
def get_confidence_interval():
    sample_mean = float(input("What is your Sample Mean : "))
    alpha = 100 - float(input("What is your Confidence (90, 95, 99) : "))
    alpha *= .01
    standard_deviation = float(input("What is the Standard Deviation : "))
    sample_size = float(input("What is your Sample Size : "))
    z_code_area = pos_z_code_area(alpha/2)
    x = sample_mean - (z_code_area * (standard_deviation / math.sqrt(sample_size)))
    y = sample_mean + (z_code_area * (standard_deviation / math.sqrt(sample_size)))
    print("X : {:.2f}".format(x))
    print("Y : {:.2f}".format(y))


get_confidence_interval()

# Now we will cover Binomial Probability which focuses on
# whether will or won't occur. * There are conditions how ever
# to use this formula. You must have multiple fixed trials
# with an outcome of pass or fail. The outcome of each trial
# can't effect other trials. Finally the probability for each
# trial must be equal.

# If you are rolling 1 die 100 times and want the binomial
# distribution of rolling a 6 that is ok because you met all
# the conditions. * Rolling dice until you get 5 sixes doesn't
# apply because the number of trials isn't fixed.

# Here is the Binomial Probability Formula. n represents the
# number of trials. r the number of successes. We must find
# the number of combinations. p finally represents the
# probability of each value.

# Let's calculate the probability of getting exactly 4 sixes
# in 10 rolls. * First we have to find the number of
# combinations. This is known as the binomial coefficient. *
# Then we plug in the values and we find that our probability
# is .048. * As we analyze our formula further we can see the
# parts representing the probability of success and failure.


def combination_without_rep(total_items, items_to_pick):
    numerator = math.factorial(total_items)
    denominator = math.factorial(items_to_pick) * math.factorial(total_items - items_to_pick)
    return numerator / denominator


def binomial_probability():
    trials = int(input("Number of Trials : "))
    successes = int(input("Number of Successes : "))
    success_prob = float(input("Probability of Success : "))
    combinations = combination_without_rep(trials, successes)

    bp = combinations * (success_prob ** successes) * ((1-success_prob) ** (trials - successes))
    print("Binomial Probability : {:.3f}".format(bp))


binomial_probability()





