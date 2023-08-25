
class Person:
    def __init__(self, name, dob, age, height):
        self.name = name
        self.dob = dob
        self.age = age
        self.height = height

    def getDob(self):
        return self.dob

    def getSummery(self):
        return f'Name: {self.name} \nAge: {self.age} \nDate of Birth: {self.dob} \nHeight: {self.height}\n'

    def changeName(self, newName):
        self.name = newName


# personLst = [
#     Person("Fazlul", '14 April', 23, 5.11),
#     Person("Karim", '14 April', 37, 5.11),
#     Person("Shahed", '14 April', 20, 5.11),
#     Person("Joy", '14 April', 40, 5.11),
#     Person("Shumon", '14 April', 15, 5.11),
# ]

# for person in personLst:
#     if person.age >= 30:
#         print(person.getSummery())


class Student(Person):
    def __init__(self, name, dob, age, height, id, email):
        super().__init__(name, dob, age, height)
        self.id = id
        self.email = email

    def getSummery(self):
        return f'Name: {self.name} \nDOB: {self.getDob()} \nId: {self.id} \nEmail: {self.email}\n'


student_1 = Student('Uma', '23 November', 25, 5.3, 1936345, 'uma@gmail.com')
print(student_1.getSummery())
student_1.changeName('Israt Jahan')
print(student_1.getSummery())
