class SimpleDescriptor(object):
    """
    A simple data descriptor that can set and return values
    """

    def __init__(self, initval=None):
        print("__init__ of SimpleDecorator called with initval: ", initval)
        self.__set__(self, initval)

    def __get__(self, instance, owner):
        print(instance, owner)
        print('Getting (Retrieving) self.val: ', self.val)
        return self.val

    def __set__(self, instance, value):
        print('Setting self.val to ', value)
        self.val = value

class MyClass(object):
    x = SimpleDescriptor('green')

if __name__ == '__main__':
    m = MyClass()
    print(m.x)
    m.x = 'Yellow'
    print(m.x)