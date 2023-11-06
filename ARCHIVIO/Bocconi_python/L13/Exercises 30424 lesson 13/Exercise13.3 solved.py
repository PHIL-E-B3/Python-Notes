number = int(input("Enter an integer: "))

myDictionary = dict()

for x in range(1, number + 1):
    myDictionary[x] = (x / 2)**3

print()
print("Key\tValue")
for element in myDictionary:
    print(element, myDictionary[element], sep = "\t")
    #alternatively you can concatenate the keys-values in string format
    #print(str(element) + " \t" + str(myDictionary[element]))
