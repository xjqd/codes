#!/bin/python
import time
# proxy has one reference for the real subject.
# it's not combine this subject, it will generate the
# object based on the condition
class SalesManager(object):
    def work(self):
        print "sales manager is working..."

    def talk(self):
        print "sales manager ready to talk..."

class proxy(object):
    def __init__(self):
        self.busy="no"
        self.sale=None

    def work(self):
        print "proxy checking for sales manager availability..."
        if self.busy == "no":
            self.sale = SalesManager()
            time.sleep(2)
            self.sale.talk()
        else:
            print "sales manager is busying..."

class NoProxy(proxy):
    def __init__(self):
        super(NoProxy, self).__init__()

    def work(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(2)
        print("This Sales Manager will not talk to you whether he/she is busy or not")

if __name__ == "__main__":
    p = proxy()
    p.work()
    p.busy = "yes"
    p.work()
    p = NoProxy()
    p.work()
    p.busy = "yes"
    p.work()
