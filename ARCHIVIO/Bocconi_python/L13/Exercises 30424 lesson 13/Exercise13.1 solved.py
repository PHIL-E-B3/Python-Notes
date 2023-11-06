animals = 'dogcatgiraffejaguarlion'

anim1 = animals[:3]
anim2 = animals[3:6]
anim3 = animals[6:13]
anim4 = animals[13:19]
anim5 = animals[-4:]   # or anim5 = animals[19:]

animals_list = []
animals_list.append(anim1)
animals_list.append(anim2)
animals_list.append(anim3)
animals_list.append(anim4)
animals_list.append(anim5)

animals_list.sort()

for animal in animals_list:
    print(animal)
