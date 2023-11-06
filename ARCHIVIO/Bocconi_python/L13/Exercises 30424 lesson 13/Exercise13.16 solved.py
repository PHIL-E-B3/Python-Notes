# FUNCTION
def char_frequency(myString):
    dict_freq = {}
    for character in myString:
        if character in dict_freq:
            dict_freq[character] = dict_freq[character] + 1
        else:
            dict_freq[character] = 1
    return dict_freq


# MAIN Program
sentence = input("Enter a text string: ")
print(char_frequency(sentence))
