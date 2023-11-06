power = float(input("What is the maximum power signed in the contract?\n(3/4.5/6 kW) --> "))
cons = float(input("What is the total powen consumption (expressed in kW) of your \
electrical devices, assuming they are all turned on at the same time?\n --> "))

if cons > power*1.1:
    print("Don't turn everything on at the same time, otherwise the electricity supply will be disconnected")
else:
    print("Your consumption is below the limit of your",
          power, "kW meter!")
