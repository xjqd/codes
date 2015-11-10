#!/bin/python
def outer_f(f=None):
    print "out_f"
    def inner(f=None):
        print 'inner_f'
        f()
    return inner

def study():
    print "need to study"

if __name__ == "__main__":
    f1 = outer_f(study)
    print "f1=", f1
    #f2 = outer_f(study)()
    f2 = outer_f()(study)
    print "f2=",f2
