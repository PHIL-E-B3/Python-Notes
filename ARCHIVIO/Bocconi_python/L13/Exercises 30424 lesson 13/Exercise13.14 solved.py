name_list = ['Jack', 'Daniel']

joinTheParty = input("Would you like to invite someone else (Y/N)? ")

affirmative_answers = ['Y', 'y', 'YES', 'Yes', 'yes',
                       'yup', 'OK', 'ok', 'Sure', 'Of course']

while joinTheParty in affirmative_answers:
    name = input("What's the name of the person you want to invite? ")
    name_list.append(name)
    joinTheParty = input("Would you like to invite another guest (Y/N)? ")

print("\nHere is the guest list:")
for name in name_list:
    print(name)




