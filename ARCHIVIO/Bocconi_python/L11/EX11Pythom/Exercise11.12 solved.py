tag_list = ""
t = "Start"   # t variable must be different from "" to enter into the loop
while t != "":
    t = input("Next tag: ")
    if t != "":
        tag_list = tag_list + t + ", "
print("Tag list:", tag_list)
