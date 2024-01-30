class DuplicatedValuesError(ValueError):
    """Indicates that the value cant be introduced because is duplicated/is previously on the list
    Attributes:
        item: duplicated element
        message: informative text for the end user
    """
    def __init__(self, item, message="adding duplicated values is not allowed =>"):
        self.item = item
        self.message = 'DuplicatedValuesError: ' + message + ' [' + item +']'
        super().__init__(self.message)



def add_once(my_list, my_elem):
    """ Adds an element to a list, providing that it is no repeated.
        my_list (list): collection of elements
        my_elem: a value to be introduced in my_list
        Throws RepeatedValuesError when my-elem i already in my_list
    """
    if my_elem in my_list:
        raise DuplicatedValuesError(my_elem)
    my_list.append(my_elem)



value_list = []

while True:
    value = input("Enter a number: ")
    if value == "0":
        break
    try:
        add_once(value_list, value)
    except DuplicatedValuesError as e:
        print(e.message)

print("Values entered: ", value_list)

