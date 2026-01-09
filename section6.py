#OOP
# class Bigobject: #Class
#     #code
#     pass

# obj1=Bigobject() #instanciate
# obj2=Bigobject() #instanciate
# obj3=Bigobject() #instanciate
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))

# print(type(Bigobject))
# print(type(obj1))


# class PlayerCharacter:
    #Class object attribute
    # membership = True
    # def __init__(self, name, age):
        # self.name = name #attributes
        # self.age = age
        # if (PlayerCharacter.membership):
        #     self.name = name
        #     self.age = age
    # def __init__(self, name='anonymous', age=0):
    #     if (age > 18):
    #         self.name = name
    #         self.age = age
    
    # def __init__(self, name='anonymous', age=0):
    #     self.name = name
    #     self.age = age
        
    # def run(self):
    #     print('run')
        
    # def shout(self):
    #     print(f'my name is {self.name}')
        
    # @classmethod
    # def adding_things(cls,num1,num2):
    #     # return num1 + num2
    #     return cls('Teddy', num1 + num2)
    
    # @staticmethod
    # def adding_things2(num1, num2):
    #     return num1 + num2
        
# player1= PlayerCharacter('Cindy', 44)
# player2= PlayerCharacter('Tom', 21)
# player2.attack = 50

# player3 = PlayerCharacter.adding_things(2,3)
# print(player3.age)


# print(player1.adding_things(2,3))
# print(player1)
# print(player1.name)
# print(player1.age)
# print(player1.run)
# print(player1.run())
# print(player2)
# print(player2.name)
# print(player2.age)
# print(player2.attack)
# # help(player1)
# # help(list)
# print(player2.membership)
# print(player1.membership)
# print(player2.shout())
# print(player1.shout())

# class Cat:
#     species = 'mammal'
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# cat1 = Cat('cat1', 5)
# cat2 = Cat('cat2',7)
# cat3 = Cat('cat3', 3)

# def oldest_cat(*args):
#     return max(args)

# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

# class NameOfClass():
#     class_attribute = 'value'
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
        
#     def method(self):
#         #code
        
#     @classmethod
#     def cls_method(cls, param1, param2):
#         return cls(param1, param2)
    
#     @staticmethod
#     def stc_method(param1, param2):
#         return param1 + param2

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        return self

player1 = PlayerCharacter('andrei', 100)

print(player1.run())