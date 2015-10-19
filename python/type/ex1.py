#!/bin/python
def hello():
    print "hello"

Foo=type('Foo',(), {"hello":hello,"name":None})

foo = Foo()
print dir(foo)
print globals()

from new import classobj
myClass = classobj("Hello",(),{"***":"boy","age":None})
# wrong f = Hello()
f = myClass()
print dir(f)
print f.age
print hasattr(f, "***")
