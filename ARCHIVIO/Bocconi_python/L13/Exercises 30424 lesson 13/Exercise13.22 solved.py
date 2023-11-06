# FUNCTION
def translate():
    # list of possible affirmative answers
    affirm_answers = ["Y", "y", "YES", "Yes", "yes", "yup", "OK", "Ok", "ok", "that's okay"]
    x = 'Y'
    while x in affirm_answers:
        x = input("Do you want to translate an Italian word into English? ")
        if x in affirm_answers:
            term = input("Which Italian word do you want to translate? ")
            try:
                print("The translation of", term, "is:", dict_ita_eng[term])
            except:
                print(term, "is not available in the dictionary")

# MAIN program
dict_ita_eng = dict()
dict_ita_eng['ciao'] = 'hello'
dict_ita_eng['gatto'] = 'cat'
dict_ita_eng['università'] = 'university'
dict_ita_eng['età'] = 'age'
dict_ita_eng['giorno'] = 'day'

translate()
