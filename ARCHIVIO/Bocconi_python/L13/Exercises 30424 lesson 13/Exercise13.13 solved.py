start_list = [0] * 5  # it's the same as [0,0,0,0,0]
 
for i in range(5):
    start_list[i] = float(input('Enter a number: '))
	
square_list = []

for number in start_list:
    square_list.append(number**2)

square_list.sort()
print(square_list)
