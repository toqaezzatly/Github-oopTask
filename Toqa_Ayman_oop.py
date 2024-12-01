class Animal:

    def __init__(self, name ):
        self.name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("I NEED A NAAAAME!!")
        
        elif not isinstance(value, str):
            raise ValueError('The name has to be String value')
        
        else:
            self.__name = value

    

    def eat(self):
        return f'{self.__name} from class {self.__class__.__name__} is eating'
    
    def sleep(self):
        return f'{self.__class__.__name__} is sleeping'
    


class Dog(Animal):
    
    def bark(self):
        return 'Dog is barking.'


class Cat(Animal):

    def meowing(self):
        return 'Cat is Meowing'


kitten = Animal('kitty')
print(kitten.eat())

kitten2 = Cat('lolo')
print(kitten2.eat())

puppy = Dog('H')
print(puppy.bark())
