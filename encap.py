class Person:
    def __init__(self, name, age):
        self.__name = name  # double underscore prefix makes
        self.__age = age    # these properties private.

        ## Getter and setter functions control access and editting of
        # private properties.

    #getter function
    @property
    def Name(self):
        return self.__name


    #setter function gives conditions for changing values
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Cannot be Bob"
        else:    
            self.__name = value

    @staticmethod
    def call_my_name():
        return "This is a static method"


p1 = Person('Mike', 20)
print(p1.Name)


p1.Name = "Bob"
print(p1.Name)


p1.Name = "Fush"
print(p1.Name)

##Call static method
me = Person.call_my_name()
print(me)