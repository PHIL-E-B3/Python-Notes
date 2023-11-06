print("Give me a list of 5 numbers and you'll get their sum!")

memo = []
i = 5
while i > 0:
    x = input("\nEnter a number: ")
    memo.append(x)
    i = i - 1

print(memo) 

try:
    for j in range(5):
        memo[j] = float(memo[j])
    sum_numbers = sum(memo)
    print("\nThe sum is:", sum_numbers)

except:
    print("An error was made when entering data")
