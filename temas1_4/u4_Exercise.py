import datetime
now = datetime.datetime.today() # o now()
print(now)

#-----------------------------------
from statistics import mean
list = [10, 1, 7.5, 8]
list_mean = mean(list)
print (list_mean)

#-----------------------------------

import json
decode_json = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(decode_json)

#-----------------------------------

import turtle
line= turtle.forward(100)

turtle.hideturtle()
turtle.exitonclick()

#-----------------------------------

import unittest # Con run() usar clase TestCase




#-----------------------------------

from locale import getlocale
getlocale()





#-----------------------------------
