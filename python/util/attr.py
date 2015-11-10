#!/bin/python
# how to add the attribute
class Stu(object):
    
    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print self.name
        print self.age

if __name__ == "__main__":
    stu = Stu("sam")
    #stu.print_name()
    Stu.age = 30
    stu.print_name()
    stu.sex = 'm'
    stu1 = Stu("xue")
    stu1.print_name()
    print dir(Stu)
    print dir(stu)
