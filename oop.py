class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Creating an instance of the Person class
person_instance = Person(name="Joseph", age=21, gender="male")
person_instance.introduce()
