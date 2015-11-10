#!/bin/python
li = []
city1="qingdao"
Temperature=28
li.append("%d" %Temperature)
li.append(city1)
li.append("%s" %"hello")
li.append("%(name)s" %{'name':"hello"})
#li.append("%(name)s" %{'name'="hello"}) dictory can't use =
#li.append("%{name}s" %{'name':"hello"})
print li
Dict = {city1:"%d" %Temperature}
#Dict.add("city1":"%d" %Temperature)
print Dict
