class Employee:
    'Powszechna podstawowa klasa dla wszystkich pracowników'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def DisplayEmplayee(self):
        print("Name: %s, Salary: %s" % (self.name, self.salary))

#tworzenie obiektów posiadającch klasę
    #zmienna = klasa(argumenty w kolejności)
emp1 = Employee('Zara', '2000')
emp2 = Employee('John', '5500')

emp1.DisplayEmplayee()
emp2.DisplayEmplayee()
print("Total employees: %d" % Employee.empCount)