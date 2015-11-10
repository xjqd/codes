#!/bin/python
class Person(object):
    def __init__(self,name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def print_age(self):
        print "age=%d" %self.age
    def print_sex(self):
        print "sex=%s" %self.sex
    def set_val(self):
        x = self.age
        print x

if __name__ == "__main__":
    p = Person("sam")
    print dir(p)
    print dir(Person)
    p.set_age(30)
    p.print_age()
    p.sex = 'M'
    p.print_sex()
    p.set_val()
