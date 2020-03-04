class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi I'm " + self.name + '!')
        else:
            print("Hi I'm a robot without a name")
        if self.build_year:
            print('I was built in ', self.build_year, '.')
        else:
            print("I don't know when i was built")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_built_year(self, built_year):
        self.build_year = built_year

    def get_built_year(self):
        return self.build_year
x = Robot('Marvin', 1990)
y = Robot()
y.set_name('Gotfryd')
x.say_hi()
y.say_hi()

