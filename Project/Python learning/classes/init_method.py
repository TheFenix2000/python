#presence of argument - diffrent result

class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi I'm " + self.name + "!")
        else:
            print("Hi I'm a robot without a name")

x = Robot()  #brak imienia
x.say_hi()

y=Robot('Marvin')  #definiujemy imię
y.say_hi()