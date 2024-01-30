import sys

print(sys.argv)
print(type(sys.argv))


if len(sys.argv) == 1:
    print("Debe introducir algún parámetro")
else:
    for elem in sys.argv:
        print(elem, type(elem))