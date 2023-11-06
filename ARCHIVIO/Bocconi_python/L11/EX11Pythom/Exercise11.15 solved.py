# presentation

print("\nWHAT TYPE ARE YOU?")
print("------------------")
print("""Take part in this personality test by answering
a few simple questions about your preferences.
Thank you!\n""")


# input step

color  = input("Choose a colour between: red, yellow, green, black, blue\n--> ")
taste  = input("Choose between sweet or salty\n--> ")
number = int(input("Choose an integer number between 1 and 20\n--> "))
smell  = input("Choose a scent among: citrus fruits, honey, coffee, sandalwood\n--> ")
sound  = input("Choose between the sound of the stormy sea (S) or the sound of the drizzle (D)\n--> ")
touch  = input("Choose a tactile consistency between: silk, fur, sandpaper, steel\n--> ")


# answers processing step

if (color == "red" or color == "yellow") and \
   number%4 == 0 and \
   smell == "sandalwood" and \
   sound == 'D' :
    kind = "sensorial"

elif (color == "green" or color == "blue") and \
     taste == "sweet" and \
     (smell == "honey" or smell == "citrus fruits") and \
     not touch == "sandpaper" :
    kind = "sentimental"

elif (taste == "salty" and \
      number <10 and \
      (touch == "silk" or touch == "steel")) or \
     (color == "blue" and sound == 'S') :
    kind = "intuitive"

elif (color == "black") or \
     (number%2 != 0 and \
      smell == "coffee" and \
      touch == "steel") :
    kind = "logical-rational"

else:
    kind = ""


# output step

if kind == "":
    print("\nI'm sorry, you're really a strange guy ;-)")
else:
    print("\nThis is your psychological type:", kind)


