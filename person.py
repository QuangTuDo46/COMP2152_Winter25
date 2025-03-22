class Person:
    def __init__(self, name, age, height):
        self.__name = name 
        self.__age = age  
        self.__height = height     
        print("Constructing the Person object")
        self.public_prop = "I'm public"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

person = Person("Mark", 20, 6)

print(person.public_prop)

try:
    print(person.__name)
except AttributeError:
    print("Error: Cannot access private attribute directly.")

print("Initial Name:", person.get_name())
person.set_name("Anna")
print("Updated Name:", person.get_name())

class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        print("Constructing the Person object")
        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")


person = Person("Mark", 20, 6)
print("Initial Name (magic getter):", person.name)
person.name = "Anna"
print("Updated Name (magic setter):", person.name)

