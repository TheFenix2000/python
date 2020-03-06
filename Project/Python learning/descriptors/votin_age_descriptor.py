from weakref import WeakKeyDictionary

class Voter:
    required_age = 18 #in Germany

    def __init__(self):
        self.age = WeakKeyDictionary()

    def __get__(self, instance_object, object_type):
        return self.age.get(instance_object)

    def __set__(self, instance, new_age):
        if new_age < Voter.required_age:
            msg = '{name} is not old enough to vote in Germany'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print('{name} can vote in Germany'.format(name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]

class Person:
    voter_age = Voter()

    def __init__(self, name, age):
        self.name = name
        self.voter_age = age

p1 = Person('Marian', 22)
p2 = Person('Ola', 170) #jeżeliby nie maiała to wystąpiłby error
print(p2.voter_age)