class Parent:
   def myMethod(self):
       print("colling parent method")

class Child(Parent):
   def myMethod(self):
       print("Calling child method")

c = Child()
c.myMethod() #child call overrides parent method call