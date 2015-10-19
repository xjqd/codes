#!/bin/python
# -*- coding: UTF-8 -*-
def get_localizer(langue="english"):
    languages = dict(english=EnglishTexter,
                     chinese=ChineseTexter
                  )
    return languages[langue]()

class EnglishTexter(object):
    def output(self, val):
        return val

class ChineseTexter(object):
    def __init__(self):
        self.trans = dict(dog=u"狗",cat=u"猫")
        # SyntaxError: keyword can't be an expression
        # if we add dict('dog'=xxx) report error
        # for this style, this method think the left should be one parameter
    def output(self, val):
        try:
            return self.trans[val]
        except:
            return str(val)


e,c = get_localizer("english"),get_localizer("chinese")
for msg in "dog cat bird".split():
    print e.output(msg), c.output(msg)
