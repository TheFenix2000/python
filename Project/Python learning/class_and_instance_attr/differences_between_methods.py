class Pet:
    _class_info = "pet info"

    def about(self):
        print("This class is about " + self._class_info + "!")

class Dog(Pet):
    _class_info = "man's best friend"

class Cat(Pet):
    _class_info = "all kind's of cats"

if __name__ == "__main__":
    p =Pet()
    p.about()
    d = Dog()
    d.about()
    c = Cat()
    c.about()


class Pet2:
    _class_info = "pet animals"

    @classmethod  #musi byc classmetho aby metoda about 'wiedziała' przez co ją wywołujemy - 'cls'
    def about(cls):
        print("This class is about: " + cls._class_info + "!")

class Dog2(Pet2):
    _class_info = "man's best friend"

class Cat2(Pet2):
    _class_info = "all kind of cats"

if __name__ == "__main__":
    Pet2.about()
    Dog2.about()
    Cat2.about()