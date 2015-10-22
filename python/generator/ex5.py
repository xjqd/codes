#!/bin/python
import random
def get_data():
    return random.sample(range(10),3)

def consume():
    run_sum = 0
    data_seen = 0
    while True:
        data = yield
        data_seen += len(data)
        run_sum += sum(data)
        print "The running average is {}={}/{}".format(run_sum/float(data_seen),run_sum, data_seen)

def produce(consume):
    while True:
        data = get_data()
        print "Produced {}".format(data)
        consume.send(data)
        yield

if __name__ == "__main__":
    consume = consume()
    consume.next()
    produce = produce(consume)
    for _ in range(10):
        print "producing ..."
        next(produce)


