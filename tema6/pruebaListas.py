"""my_list = ["abc", 2, [5,6], 4.5, True, None]
for elem in my_list:
    print(elem)"""

"""my_list = ["abc", 2, [5,6], 4.5, True, None]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
"""

"""my_list = ["more", "than", "meets", "the", "eye"]
my_list2 = my_list.append("or ear")
my_list2 = my_list.insert(1, "or less")

print(my_list)"""


"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
for elem in fruits:
    if "a" in elem:
        new_list.append(elem)
print(new_list)"""

#Biblioteca
from datetime import datetime
my_car = {
 "manufacturer": "Ferrari",
 "model": "F40",
 "engine_cc": 2936,
 "horsepower": 478,
 "isHybrid": False,
 "revisionDates": [datetime(1990, 6, 1), datetime(1994, 7, 5)]
}

print(my_car)
print(my_car["manufacturer"])
print(my_car["model"])

my_car["country"] = "Italy"
print(my_car)

print(my_car["isHybrid"])
del my_car["isHybrid"]
print(my_car)

