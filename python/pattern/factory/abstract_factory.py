#!/bin/python
import base
class BirdFactory(object):
    def get_pet(self):
        return base.Bird()
    def get_food(self):
        return self.get_pet().food

class PeopleFactory(object):
    def get_pet(self):
        return base.People()
    def get_food(self):
        return self.get_pet().food

class PetShop(object):
    def __init__(self, factory):
        #self.pet_factory = factory
        self.pet_factory = factory()
    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print pet
        #print "the pet food is {}".format(pet.get_food())
        print "the pet food is {}".format(self.pet_factory.get_food())

if __name__ == "__main__":
    import random
    #import pdb
    #pdb.set_trace()
    shop=PetShop(random.choice([BirdFactory,PeopleFactory]))
    shop.show_pet()

