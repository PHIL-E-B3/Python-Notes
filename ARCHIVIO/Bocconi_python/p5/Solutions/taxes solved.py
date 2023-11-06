

income = float(input('Enter your income: '))


if income <= 10000:
    taxes = income * 0
elif income <= 29000:
    taxes = income * 0.2
elif income <= 65000:
    taxes = income * 0.3
elif income <= 110000:
    taxes = income * 0.4
else:
    taxes = income * 0.45


avail_income = income - taxes

print('Taxes to be paid amount to', format(taxes, '.2f'), 'euros.')
print('The available income is:', format(avail_income, '.2f'),'euros.')

while True:
    savings = float(input('How much of your available income do you want to save? '))
    if savings <= avail_income * 0.50:
        break
    else:
        print('You cannot save more than 50% of the available income!')













