class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi I'm " + self.name)

class PhisicalRobot(Robot):
    pass

x = Robot('Marvin')
y = PhisicalRobot('Caliban')

print(x, type(x))
print(y, type(y))

y.say_hi()
