# Venn Diagrams can be very useful for representing events and how
# they interact. They work best for marginal probabilities, being
# probabilities that don't effect each other. They also work good
# with Joint Probabilities which measure the likelihood of events
# occurring together. They don't work well with conditional
# probabilities and when analyzing sequences of events.

# You can see here how all the symbols you have seen so far work
# together in a Venn Diagram. The c represents the compliment of
# the event.

# Here I'll use our previous exercising table in a Venn Diagram
# format * You can see how the table data translates over.

# Tree Diagrams are normally used when Venn Diagrams cannot. They
# work best with multistage and conditional probability problems
# which is the opposite versus Venn Diagrams. They work poorly
# when events take place at the same time. Here I'll break down
# the process of flipping a coin twice. You can see we can find
# the probability of .5.

# The most basic probability model is known as the discrete
# uniform distribution. The conditions for using it is that all
# values of x must be consecutive integers 1, 2, 3, ... N  and
# each value of x must have an equal probability. The probability
# mass function assigns probabilities to random values. For these
# each would have the probability of 1/N.

# To calculate the probability mass of a die roll take 1/b-a+1
# where b is the max value and a is the lowest value. For a die
# roll that equals 1/6th.

# Variance measures how far a set of numbers is spread out. To
# calculate that take (b-a+2)*(b-a) / 12 where again b is the max
# value and a is the lowest value. With a die roll we see that
# that is 2.9 or 3.

# This chart provides the probability mass for each roll of 2
# dice. * A relative frequency histogram shows how often values
# are expected for each roll of 2 dice.

# This is a cumulative distribution chart which provides the
# cumulative probability associated with adding additional
# possible dice rolls.

import random
import re

dice_values = [0] * 13


def prob_dice_rolls():

    for i in range(100000):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        dice_sum = die_1 + die_2
        dice_values[dice_sum] += 1

    for j in range(2, 13):
        print(f"{j} : {dice_values[j]/100000}")


# Variance measures how far a set of numbers is spread out
def dud_variance(min_val, max_val):
    numerator = (max_val - min_val + 1) ** 2
    print(f"DUD Variance : {numerator / 12}")


# Expected value is the long term expected average
def dud_expected_val(max_val, num):
    sum = 0
    for k in range(num):
        sum += (max_val + 1) / 2
    print(f"Expected Value : {sum}")


prob_dice_rolls()
dud_variance(1, 6)
dud_expected_val(6, 2)

# With a normal distribution in which we contain 100% of the
# probability under the curve we also have an equal bell curve
# with the same area under both sides * We also see here that the
# mean and median are equal. We also see that 68% of the total
# area is 1 standard deviation from the mean. This continues with
# 95% at 2 SDs and 99.7% at 3 SDS. This is known as the empirical
# rule.

# I further break that down here into all the parts for a standard
# normal distribution. Also notice that just .3 % or .15% on both
# sides is all that is left after 3 standard deviations.

# The Z Score gives us the value in standard deviations for the
# percentile we want * For example if we want 95% of the data it
# tells us how many standard deviations are required. * The
# formula asks for the length from the mean to x and divides by
# the standard deviation.

# This will make more sense with an example. Here is a Z Table.
# If we know our mean is 40.8, the standard deviation is 3.5 and
# we want the area to the left of the point 48 we perform our
# calculation to get 2.06. * We then find 2.0 on the left of the
# Z Table * and .06 on the top. * This tells us that the area
# under the curve makes up .98030 of the total.

pos_z_code_arr = [0][0]*10

pos_z_codes = ".50000 .50399 .50798 .51197 .51595 .51994 .52392 .52790 .53188 .53586 0.1 .53983 .54380 .54776 .55172 .55567 .55962 .56356 .56749 .57142 .57535 0.2 .57926 .58317 .58706 .59095 .59483 .59871 .60257 .60642 .61026 .61409 0.3 .61791 .62172 .62552 .62930 .63307 .63683 .64058 .64431 .64803 .65173 0.4 .65542 .65910 .66276 .66640 .67003 .67364 .67724 .68082 .68439 .68793 0.5 .69146 .69497 .69847 .70194 .70540 .70884 .71226 .71566 .71904 .72240 0.6 .72575 .72907 .73237 .73565 .73891 .74215 .74537 .74857 .75175 .75490 0.7 .75804 .76115 .76424 .76730 .77035 .77337 .77637 .77935 .78230 .78524 0.8 .78814 .79103 .79389 .79673 .79955 .80234 .80511 .80785 .81057 .81327 0.9 .81594 .81859 .82121 .82381 .82639 .82894 .83147 .83398 .83646 .83891 1.0 .84134 .84375 .84614 .84849 .85083 .85314 .85543 .85769 .85993 .86214 1.1 .86433 .86650 .86864 .87076 .87286 .87493 .87698 .87900 .88100 .88298 1.2 .88493 .88686 .88877 .89065 .89251 .89435 .89617 .89796 .89973 .90147 1.3 .90320 .90490 .90658 .90824 .90988 .91149 .91309 .91466 .91621 .91774 1.4 .91924 .92073 .92220 .92364 .92507 .92647 .92785 .92922 .93056 .93189 1.5 .93319 .93448 .93574 .93699 .93822 .93943 .94062 .94179 .94295 .94408 1.6 .94520 .94630 .94738 .94845 .94950 .95053 .95154 .95254 .95352 .95449 1.7 .95543 .95637 .95728 .95818 .95907 .95994 .96080 .96164 .96246 .96327 1.8 .96407 .96485 .96562 .96638 .96712 .96784 .96856 .96926 .96995 .97062 1.9 .97128 .97193 .97257 .97320 .97381 .97441 .97500 .97558 .97615 .97670 2.0 .97725 .97778 .97831 .97882 .97932 .97982 .98030 .98077 .98124 .98169 2.1 .98214 .98257 .98300 .98341 .98382 .98422 .98461 .98500 .98537 .98574 2.2 .98610 .98645 .98679 .98713 .98745 .98778 .98809 .9884 .98870 .98899 2.3 .98928 .98956 .98983 .99010 .99036 .99061 .99086 .99111 .99134 .99158 2.4 .99180 .99202 .99224 .99245 .99266 .99286 .99305 .99324 .99343 .99361 2.5 .99379 .99396 .99413 .99430 .99446 .99461 .99477 .99492 .99506 .99520 2.6 .99534 .99547 .99560 .99573 .99585 .99598 .99609 .99621 .99632 .99643 2.7 .99653 .99664 .99674 .99683 .99693 .99702 .99711 .99720 .99728 .99736 2.8 .99744 .99752 .99760 .99767 .99774 .99781 .99788 .99795 .99801 .99807 2.9 .99813 .99819 .99825 .99831 .99836 .99841 .99846 .99851 .99856 .99861 3.0 .99865 .99869 .99874 .99878 .99882 .99886 .99889 .99893 .99896 .99900 3.1 .99903 .99906 .99910 .99913 .99916 .99918 .99921 .99924 .99926 .99929 3.2 .99931 .99934 .99936 .99938 .99940 .99942 .99944 .99946 .99948 .99950 3.3 .99952 .99953 .99955 .99957 .99958 .99960 .99961 .99962 .99964 .99965 3.4 .99966 .99968 .99969 .99970 .99971 .99972 .99973 .99974 .99975 .99976 3.5 .99977 .99978 .99978 .99979 .99980 .99981 .99981 .99982 .99983 .99983 3.6 .99984 .99985 .99985 .99986 .99986 .99987 .99987 .99988 .99988 .99989 3.7 .99989 .99990 .99990 .99990 .99991 .99991 .99992 .99992 .99992 .99992 3.8 .99993 .99993 .99993 .99994 .99994 .99994 .99994 .99995 .99995 .99995 3.9 .99995 .99995 .99996 .99996 .99996 .99996 .99996 .99996 .99997 .99997"

neg_z_codes = ".50000 .49601 .49202 .48803 .48405 .48006 .47608 .47210 .46812 .46414 .46017 .45620 .45224 .44828 .44433 .44038 .43644 .43251 .42858 .42465 .42074 .41683 .41294 .40905 .40517 .40129 .39743 .39358 .38974 .38591 .38209 .37828 .37448 .37070 .36693 .36317 .35942 .35569 .35197 .34827 .34458 .34090 .33724 .33360 .32997 .32636 .32276 .31918 .31561 .31207 .30854 .30503 .30153 .29806 .29460 .29116 .28774 .28434 .28096 .27760 .27425 .27093 .26763 .26435 .26109 .25785 .25463 .25143 .24825 .24510 .24196 .23885 .23576 .23270 .22965 .22663 .22363 .22065 .21770 .21476 .21186 .20897 .20611 .20327 .20045 .19766 .19489 .19215 .18943 .18673 .18406 .18141 .17879 .17619 .17361 .17106 .16853 .16602 .16354 .16109 .15866 .15625 .15386 .15151 .14917 .14686 .14457 .14231 .14007 .13786 .13567 .13350 .13136 .12924 .12714 .12507 .12302 .12100 .11900 .11702 .11507 .11314 .11123 .10935 .10749 .10565 .10383 .10204 .10027 .09853 .09680 .09510 .09342 .09176 .09012 .08851 .08691 .08534 .08379 .08226 .08076 .07927 .07780 .07636 .07493 .07353 .07215 .07078 .06944 .06811 .06681 .06552 .06426 .06301 .06178 .06057 .05938 .05821 .05705 .05592 .05480 .05370 .05262 .05155 .05050 .04947 .04846 .04746 .04648 .04551 .04457 .04363 .04272 .04182 .04093 .04006 .03920 .03836 .03754 .03673 .03593 .03515 .03438 .03362 .03288 .03216 .03144 .03074 .03005 .02938 .02872 .02807 .02743 .02680 .02619 .02559 .02500 .02442 .02385 .02330 .02275 .02222 .02169 .02118 .02068 .02018 .01970 .01923 .01876 .01831 .01786 .01743 .01700 .01659 .01618 .01578 .01539 .01500 .01463 .01426 .01390 .01355 .01321 .01287 .01255 .01222 .01191 .01160 .01130 .01101 .01072 .01044 .01017 .00990 .00964 .00939 .00914 .00889 .00866 .00842 .00820 .00798 .00776 .00755 .00734 .00714 .00695 .00676 .00657 .00639 .00621 .00604 .00587 .00570 .00554 .00539 .00523 .00508 .00494 .00480 .00466 .00453 .00440 .00427 .00415 .00402 .00391 .00379 .00368 .00357 .00347 .00336 .00326 .00317 .00307 .00298 .00289 .00280 .00272 .00264 .00256 .00248 .00240 .00233 .00226 .00219 .00212 .00205 .00199 .00193 .00187 .00181 .00175 .00169 .00164 .00159 .00154 .00149 .00144 .00139 .00135 .00131 .00126 .00122 .00118 .00114 .00111 .00107 .00104 .00100 .00097 .00094 .00090 .00087 .00084 .00082 .00079 .00076 .00074 .00071 .00069 .00066 .00064 .00062 .00060 .00058 .00056 .00054 .00052 .00050 .00048 .00047 .00045 .00043 .00042 .00040 .00039 .00038 .00036 .00035 .00034 .00032 .00031 .00030 .00029 .00028 .00027 .00026 .00025 .00024 .00023 .00022 .00022 .00021 .00020 .00019 .00019 .00018 .00017 .00017 .00016 .00015 .00015 .00014 .00014 .00013 .00013 .00012 .00012 .00011 .00011 .00010 .00010 .00010 .00009 .00009 .00008 .00008 .00008 .00008 .00007 .00007 .00007 .00006 .00006 .00006 .00006 .00005 .00005 .00005 .00005 .00005 .00004 .00004 .00004 .00004 .00004 .00004 .00003 .00003"

# Create a list containing all matching floats
all_pos_z_codes = re.findall("\.\d{5}", pos_z_codes)

# Cycle through the list grabbing 10 values at a time
# and place them in each row of the multidimensional list
pos_z_code_arr = [all_pos_z_codes[i:i+10] for i in range(0, len(all_pos_z_codes), 10)]

all_neg_z_codes = re.findall("\.\d{5}", neg_z_codes)

# Do the same for negative Z codes
neg_z_code_arr = [all_neg_z_codes[i:i+10] for i in range(0, len(all_neg_z_codes), 10)]

print(f"{neg_z_code_arr[1][9]}")


# Finds area using mean, right most point and standard deviation
def pos_z_code_area(mean, right_point, standard_deviation):
    z_code = round((right_point - mean) / standard_deviation, 2)
    print(z_code)
    z_code_nums = re.findall("\d", str(z_code))
    first_z_code = int(z_code_nums[0] + z_code_nums[1])
    second_z_code = int(z_code_nums[2])
    print(f"Area : {pos_z_code_arr[first_z_code][second_z_code]}")


pos_z_code_area(40.8, 48, 3.5)

# We can also find the area to the left of the mean with a Negative
# Z Score Table. If we want to find the area the the left of 36.3
# with a mean of 40.8 perform our calculation to get -1.29. * Now
# look for -1.2 and 0.09 in the Negative Z Table * to find that the
# area is .09853


# Does the same for negative Z Code Table
def neg_z_code_area(mean, left_point, standard_deviation):
    # Take absolute value to get rid of negative value
    z_code = round(abs((left_point - mean) / standard_deviation), 2)
    print(z_code)
    z_code_nums = re.findall("\d", str(z_code))
    first_z_code = int(z_code_nums[0] + z_code_nums[1])
    second_z_code = int(z_code_nums[2])
    print(f"Area : {neg_z_code_arr[first_z_code][second_z_code]}")


neg_z_code_area(40.8, 36.3, 3.5)


def get_test_score(mean, standard_deviation, percent):
    # Get index for first closest matching value in Z Table
    # Define what I'm looking for
    regex = f"\.{percent}\d{3}"

    # Iterate the multidimensional list
    for i in range(0, len(pos_z_code_arr)):
        for j in range(0, len(pos_z_code_arr[0])):
            # If I find a match
            if re.search(regex, pos_z_code_arr[i][j]):
                # Combine column and row values into Z Code
                z_code = i * .1 + j * .01
                # Find x using formula ZC = x - mean / SD
                z_code *= standard_deviation
                z_code += mean
                return z_code


print(f"Required Score to Place in Top 1% : {get_test_score(79, 7.5, 99)}")

