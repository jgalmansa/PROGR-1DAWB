def print_odd_or_even(my_number):
    if my_number % 2 == 0:
        print("Even number")
    elif my_number % 2 == 1:
        print("Odd number")
    else:
        print("Not a valid integer")

print_odd_or_even (4)

def fn(a, b):
    a += 1
    b.append(9)
    print(a)
x = 1
y = [7, 8]
fn(x, y)
print(x, y)


def f1(*args):
    for arg in args:
        print(arg)

f1(1, True, 50, "Hello, world!")