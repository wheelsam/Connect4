class Dog:

    def __init__(self, age, name):
        self._age = age
        self._name = name

    def getAge(self):
        return self._age

    def getName(self):
        return self._name

    def setAge(self, age):
        self._age = age

    def setName(self, name):
        self._name = name

    def __str__(self):
        return "dog:\nname: " + self._name + "/nage: " + str(self._age)
    #what up
