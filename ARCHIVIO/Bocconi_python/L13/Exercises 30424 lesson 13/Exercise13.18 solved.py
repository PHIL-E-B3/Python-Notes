def weighted_average(values, weights):
    weights_sum = 0
    for w in weights:
        weights_sum += w
        
    if weights_sum != 1:
        print('The sum of the weights is different from 1!')

    elif len(values) != len(weights):
        print('The values list and the weights list have different lengths.')
            
    else:
        average = 0
        for i in range(len(values)):
            average += values[i] * weights[i]
        return average

# main

val = [20, 25, 30]
wgt = [0.2, 0.3, 0.5]
print("Values:", val)
print("Weights:", wgt)
averageGrade = weighted_average(val, wgt)
print("Average:", averageGrade)

print()

val = [20, 25, 30]
wgt = [2,3,5]
print("Values:", val)
print("Weights:", wgt)
averageGrade = weighted_average(val, wgt)
print("Average:", averageGrade)

print()

val = [20, 25, 28, 30]
wgt = [0.2, 0.3, 0.5]
print("Values:", val)
print("Weights:", wgt)
averageGrade = weighted_average(val, wgt)
print("Average:", averageGrade)
