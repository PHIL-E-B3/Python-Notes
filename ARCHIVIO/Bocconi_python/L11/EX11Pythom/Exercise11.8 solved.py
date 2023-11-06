n = 0
while True:
    x = input("""\nWhat's your favourite food?
(Write ENOUGH to finish): """)
    if x == "ENOUGH":
        break
    n += 1
print("\nYou like", n,"dishes")
