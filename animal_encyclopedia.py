from animalencyclopedia import AnimalEncyclopedia
from animal_info import animals, animal_list


while True:
    print("""Choose an animal you wish to learn about:\n 
    press nr corresponding to the animal or
    press x to exit""")
    for i in animal_list:
        print(i, animal_list[i])

    user_input = str(input())

    if user_input == 'x':
        break

    elif user_input == '1':
        cow = AnimalEncyclopedia.set_animal_info(animals, 'cow')
        AnimalEncyclopedia.description(cow)
        print(AnimalEncyclopedia.get_output_template(cow))

    elif user_input == '2':
        polar_bear = AnimalEncyclopedia.set_animal_info(animals, 'polar_bear')
        AnimalEncyclopedia.description(polar_bear)
        print(AnimalEncyclopedia.get_output_template(polar_bear))

    elif user_input == '3':
        giraffe = AnimalEncyclopedia.set_animal_info(animals, 'giraffe')
        AnimalEncyclopedia.description(giraffe)
        print(AnimalEncyclopedia.get_output_template(giraffe))

    else:
        print("input wrong")


