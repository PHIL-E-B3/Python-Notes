list_a = [125, 89, 2, 6, 58, 65, 137, 11, 64, 98, 17, 35]

number = int(input("Choose a number: "))

list_b = []

for i in list_a:
    if i < number:
        list_b.append(i)

print(list_b)
