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


class PlayerCharacter:
    #Class object attribute
    membership = True
    def __init__(self, name, age):
        # self.name = name #attributes
        # self.age = age
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age
        
    def run(self):
        print('run')
        
    def shout(self):
        print(f'my name is {self.name}')
        
player1= PlayerCharacter('Cindy', 44)
player2= PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1)
print(player1.name)
print(player1.age)
print(player1.run)
print(player1.run())
print(player2)
print(player2.name)
print(player2.age)
print(player2.attack)
# help(player1)
# help(list)
print(player2.membership)
print(player1.membership)
print(player2.shout())
print(player1.shout())