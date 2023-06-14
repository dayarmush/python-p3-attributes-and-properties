#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='dog', breed = None ):
            if type(name) == str and (0 < len(name) < 26):
                self.name = name
            else:
                return print('Name must be string between 1 and 25 characters.')

            if breed in APPROVED_BREEDS:
                self.breed = breed
            else:
                print("Breed must be in list of approved breeds.")


    # def set_name(self, name):
    #     if type(name) == str and (0 < len(name) < 26):
    #             self.name = name
    #     else:
    #         return print('Name must be string between 1 and 25 characters.')

    # def get_name(self):
    #     return self._name

    # name = property(set_name, get_name)

    # def set_breed(self, breed):
    #     if breed in APPROVED_BREEDS:
    #             self.breed = breed
    #     else:
    #         print("Breed must be in list of approved breeds.")
         

    
    # def get_breed(self):
        # return self._breed
    
    # breed = property(set_breed, get_breed)
    
