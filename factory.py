from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def abs_method():
        # return "This is an interface method"
        pass
class Student(IPerson):

    def __init__(self):
        self.name = "Any name"

    def abs_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Any teacher name"

    def abs_method(self):
        print("I am a teacher")


# s1 = Student()
# print(s1.abs_method())
# print(s1.name)

### create objects according to type

class PersonFactory:
    @staticmethod
    def build_person(p_type):
        if p_type == "student":
            return Student()
        if p_type == "teacher":
            return Teacher()
        print("invalid type")
        return -1

if __name__ == '__main__':
    choice = input("Enter type:\n")
    person = PersonFactory.build_person(choice)
    person.abs_method()

