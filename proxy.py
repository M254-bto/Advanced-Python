from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass= ABCMeta):

    @abstractclassmethod
    def person_method():
        """interface"""


class Person(IPerson):
    def person_method(self):
        print("I am a person")

class ProxyClass(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("This is a proxy function")
        self.person.person_method()

# p1 = Person().person_method()

p2 = ProxyClass().person_method()