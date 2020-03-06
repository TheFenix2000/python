class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi I'm " + self.name)

class PhisicalRobot(Robot):

    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " takes care of you!")

#nadpisane 'say_hi
y = PhisicalRobot('Caliban')
y.say_hi()

#oryginalne
Robot.say_hi(y)