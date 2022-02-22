class AnimalEncyclopedia:
    def __init__(self,
                 animal_name: str,
                 avr_lifespan: str,
                 avr_size: str,
                 habitable_region: str,
                 ):
        self.animal_name = animal_name
        self.avr_lifespan = avr_lifespan
        self.avr_size = avr_size
        self.habitable_region = habitable_region

    def get_output_template(self):
        return f"""\nThe animals name/names are {self.animal_name},
Its average lifespan is {self.avr_lifespan},
Their usual size is {self.avr_size},
and its habitats are {self.habitable_region}.\n"""

    def description(self):
        file_output = self.get_output_template()
        with open("animal_information.txt", "w", encoding='utf-8') as f:
            f.write(file_output)

    @staticmethod
    def set_animal_info(dictionary, animal):
        output = AnimalEncyclopedia(
            dictionary[animal]['1'],
            dictionary[animal]['2'],
            dictionary[animal]['3'],
            dictionary[animal]['4'], )
        return output
