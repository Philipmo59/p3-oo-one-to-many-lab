class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner=""):
        if pet_type not in self.PET_TYPES:
            raise Exception
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self,name):
        self.name = name
    def pets(self):
        return Pet.all
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet: pet.name)