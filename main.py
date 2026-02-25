class Dog:
    def __init__(self, name, height = 5):
        self.name = name
        self.height = height

    def __ge__(self, dog):
        return self.height == dog.height


my_dog = Dog("Nelson", 2)
street_dog = Dog("Nelson", 2)

print(dir(int))



