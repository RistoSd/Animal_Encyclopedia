from animalencyclopedia import AnimalEncyclopedia
from animal_info import *


def set_animal_info(dictionary, animal):
    output = AnimalEncyclopedia(
        dictionary[animal]['1'],
        dictionary[animal]['2'],
        dictionary[animal]['3'],
        dictionary[animal]['4'],)
    return output


cow = set_animal_info(animals, 'cow')
text_output = AnimalEncyclopedia.description(cow)
print(AnimalEncyclopedia.get_output_template(cow))
