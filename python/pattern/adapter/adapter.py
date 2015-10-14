#!/bin/python
class Cat(object):
    def __init__(self):
        self.name = "cat"
    def meow(self):
        return "meow"

class Dog(object):
    def __init__(self):
        self.name="dog"
    def bark(self):
        return "bark"

class Human(object):
    def __init__(self):
        self.name="human"
    def speak(self):
        return "speak"

class Car(object):
    def __init__(self):
        self.name="car"
    def make_noise(self):
        return "vroom"

class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
        #k=adapted_methods.keys()
        #v=adapted_methods.values()
        #for k, v in adapted_methods.items():
        #    print k ,v
        #    self.obj.__dict__[k]=v

if __name__=="__main__":
    objects=[]
    cat=Cat()
    t=Adapter(cat,make_noise=cat.meow)
    objects.append(t)
    #print dir(t)
    #print t.obj.make_noise()
    dog=Dog()
    objects.append(Adapter(dog,make_noise=dog.bark))
    human = Human()
    objects.append(Adapter(human,make_noise=human.speak))
    car=Car()
    objects.append(Adapter(car,make_noise=car.make_noise))

    for obj in objects:
        print obj.make_noise()
