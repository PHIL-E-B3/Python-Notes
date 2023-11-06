passed = int(input("How many modules of the Ecdl Full Standard \
certification have you already passed? "))

if passed < 0 or passed > 7:
    print("Invalid data - Run the program once again")
elif passed == 7:
    print("Great, you passed them all :-)")
elif passed == 5 or passed == 6:
    print("Go, go, go, you are almost there!")
elif passed >= 1 and passed <= 4:
    print("Come on, only ",
          str(7-passed)+' missing modules,' ,
          "finish them quickly")
elif passed == 0:
    print("What are you waiting for? You cannot do \
the second intermediate exam or the general exam \
without the prerequisite.")
