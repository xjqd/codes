#!/bin/python
class Person(object):
    def __init__(self, sex, logger):
        print self
        self.sex = sex
        self.logger = logger
    def print_info(self):
        print self
        print self.sex
        print self.logger.length

class Stu(Person):
    def __init__(self,sex, name):
        self.name=name
        self.sex=sex
        #print self
        #Person.__init__(self, sex)

    #def print_info(self):
        #print self.name
        #print self.sex

class Logger(object):
    length = 10

if __name__ == "__main__":
    logger = Logger()
    s = Stu('M',"sam")
    print dir(s)
    p = Person('M',logger)
    print dir(p)
    print logger.length
    #s.logger = None
    s.logger = logger
    s.print_info()
