class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major                   
        print("This time it's a Student object")

student = Student("Maria", 22, 6, "Computer Science")