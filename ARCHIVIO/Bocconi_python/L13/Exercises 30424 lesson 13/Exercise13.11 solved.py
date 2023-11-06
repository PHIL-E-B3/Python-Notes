while True:
    line = input('Enter a string\n--> ')
    if line == 'end' or line == 'exit':
        break
    print("It is composed of", len(line), "characters")
