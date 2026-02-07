# Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. They are often used to add functionality to existing code without changing its structure.
# @classmethod
# @staticmethod

# def hello():
#     print('hellllllooooooo')
    
# greet = hello
# # hello()
# del hello

# print(greet())

# def hello(func):
#     func()
    
# def greet():
#     print('still here!')
    
# a = hello(greet)

# print(a)

# @decorator
# def hello():
#     pass

# Higher Order Function HOC
# def greet(func):
#     func()
# # filter()
# def greet2():
#     def func():
#         return 5
#     return func

# a = greet2()
# print(a())

# Decorator 2
# def my_decorator(func):
#     def wrap_func():
#         print('**********')
#         func()
#         print('**********')
#     return wrap_func

# @my_decorator
# def hello():
#     print('hellloooo')
    
# @my_decorator
# def bye():
#     print('see ya later')    
    
# hello()
# bye()
# hello2 = my_decorator(hello)
# hello2()
# hello2 = my_decorator(hello)()

# Decorator 3
# def my_decorator(func):
#     def wrap_func(x, y):
#         print('**********')
#         func(x, y)
#         print('**********')
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)
    
# # hello('hiii')
# a = my_decorator(hello)
# a('hiiii', ':)')

# Decorator Patter
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('**********')
#         func(*args, **kwargs)
#         print('**********')
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)
    
# hello('hiiii')

# Why do we need decorators?
# from time import time 

# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1= time() # what time it is now
#         result = fn(*args, **kwargs)
#         t2 = time() # what time it is after function run
#         print(f'it took {t2-t1}ms')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(1000000):
#         i*5
        
# long_time()

# Exercise
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user['valid']==True and user['name']=='Sorna':
            return fn(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)