class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return print("Hello, I am {}!".format(self.name))
      
newby = Person(input())
newby.greet()
