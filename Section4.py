'''
my_list=[1,2,3]
for item in my_list:
    print(item)

i=0
while i<len(my_list):
    print(my_list[i])
    i +=1
'''
'''
for item in [1,2,3]:
    print(item)

i=0
while i<len([1,2,3]):
    print(i)
    i +=1
'''
'''
while True:
    print('say something: ')
    break
'''
'''
while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
'''
'''
my_list=[1,2,3]
for item in my_list:
    continue
    print(item)

i=0
while i < len(my_list):
    print(my_list[i])
    continue
    i += 1
'''
'''
my_list=[1,2,3]
for item in my_list:
    print(item)
    continue

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
'''
'''
my_list=[1,2,3]
for item in my_list:
    pass
    print(item)

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass
'''
'''
my_list=[1,2,3]
for item in my_list:
    # thinking about it
    pass

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass
'''
from os import name


picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
''''''

#iterate over picture
# if 0 -> print ''
# if 1 -> print '*'
'''
for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
'''
'''
fill='*'
empty=''
for row in picture:
    for pixel in row:
        if (pixel):
            print(fill,end='')
        else:
            print(empty,end='')
    print('')
'''
'''
#Exercise: Check for duplicates in list:
some_list=['a','b','c','b','d','m','n','n']

duplicates=[]
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
'''

# DRY
#parameters
#def say_hello():
#    print('Hello!')
# def say_hello(name,emoji):
    # print(f'Hello! {name} {emoji}')
#arguments
# #positional arguments
# def say_hello(name='Darth Vader',emoji=':)'):
#     print(f'Hello! {name} {emoji}')
# say_hello('Andrei',':)')
# say_hello('dan',':)')
# say_hello('emily',':)')
# # '''
# def show_tree():
#     for image in picture:
#         for pixel in image:
#             if pixel:
#                 print('*',end='')
#             else:
#                 print(' ',end='')
#         print('')

# show_tree()
# '''
# #keyword arguments
# say_hello(emoji=':)',name='Bibi')
# say_hello()
# say_hello('Timmy')

# def sum(num1,num2):
#     return num1+num2
    # print('hi')

#Should do one thing really well
#Should return something
# print(sum(4,5))

# total=sum(10,5)
# total=15
# print(sum(10,total))

# def sum(num1,num2):
#     def another_func(n1,n2):
#         return n1+n2
#     return another_func(num1,num2)
#     #return 5
#     #print('hi')

# total=sum(10,20)
# print(total)


#method vs function
# list()
# print()
# max()
# min()
# input()

'''
def some_random_stuff():
    pass

some_random_stuff()

'hello'.index()
'''

# is_old = True
# is_licensed = True

# Truthy and Falsy
# is_old = bool('hello)
# is_licensed = bool(5)
# is_licensed = bool(None)

# if is_old and is_licensed:
#     print("you are old enough to drive and you have a licence!")
# else:
#     print("you are not of age!")

# print('okoko')


# Ternary Operator

# condition_if_true if condition else condition_if_false

# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)
'''
# Logical Operators
# Short Circuiting
is_Friend = True
# is_Friend = False
is_User = True
# is_User = False

if is_Friend and is_User:
    print(is_Friend and is_User)

if is_Friend or is_User:
    print(is_Friend and is_User)

print(4>5)
print(4==5)
print(4<5)
print('a' > 'A')
print(1<2>3<4)
print(1 <=0)
'''

'''
is_magician = True
is_expert = False

# Check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")
# Check if magician BUT NOT expert: "at least you are getting there"
elif is_magician and not is_expert:
    print("at least you are getting there")
# Check if NOT magician: "you need magic powers"
elif not is_magician:
    print("you need magic powers")
'''



# print(True == 1) # print(True == bool(1))
# print('' == 1)
# print(10 == 10.0)
# print([] == [])
# print([1,2,3] == [1,2,3])


# print(True is 1)
# print('1' is '1' )
# print(10 is 10.0)
# print([] is [])
# print([1,2,3] is [1,2,3])

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# print(a == b)

# for item in 'Zero to Mastery':
#     print(item)

# for item1 in [1,2,3,4,5]:
#     print(item1)

# for item2 in (1,2,3,4,5):
#     print(item2)
# print(item2)

# for item3 in {1,2,3,4,5}:
#     print(item3)
# print("hi")

# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
        # print(item, x)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
'''
for item in user.items():    # for item in user:
    print(item)

# for item in user.values():
    # print(item)
for item in user.values():
    key,value = item;
    print(key, value)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)
'''

# iterable - list, dictionary, tuple, set, string
# iterate - one by one check each item in the collection

# counter
'''
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item
print(counter)
'''
'''
for number in range(0,100):
    print(number)
'''

# for _ in range(0,10,2):
#     print(_)
# for _ in range(10,0,-1):
#     print(_)
# for _ in range(10,0,-2):
#     print(_)
# for _ in range(2):
#     print(list(range(10)))

# for i,char in enumerate("Helllo"):
#     print(i,char)
# for i,char in enumerate((1,2,3)):
#     print(i,char)

# for i, char in enumerate(list(range(100))):
#     print(i, char)
#     if char == 50:
#         print(f'index of 50 is: {i}')

# i = 0
# while i < 50:
#     print(i)
#     i +=1 # break
#     break
# else:
#     print('done with all the work')

# my_list = [1,2,3]
# for item in my_list:
#     print(item)

# i=0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
# while True:
#     response =input('say something: ')
#     if (response == 'bye'):
#         break

# my_list=[1,2,3]
# for item in my_list:
    # thinking about it
    # break
    # pass
    # continue
    # print(item)
'''
i=0
while i< len(my_list):
    print(my_list[i])
    i+=1
    # continue
    # break
    pass
'''
'''
# clean
# DRY
# Readability
# predictability
# Exercise!
# A 2D list whhere 0 is the background and 1 is the shape
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
# itersate over picture
# if 0 -> print ''
# if 1 -> print '*'
# Step 1: Loop through each horizontal line (the rows)
for row in picture:
    # Step 2: Loop through each individual number in that row (the columns)
    for pixel in row:
    # Step 3: Check the value of the pixel
        if (pixel==1):
        # Print a star for '1', use end='' to stay on the same line
            print('*', end='')
        else:
        # Print a space for '0', use end='' to stay on the same line
            print(' ',end ='')
    # Step 4: After finishing a row, print a newline to move to the next line
    print('')
'''

# Exercise: Check for duplicates in list:
'''
some_list = ['a','b','c','b','d','m','n','n']

duplicates =[]

for value in some_list:
    if some_list.count(value) >1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
'''

# DRY
# def say_hello():
#     print("hello")
    
# say_hello()

# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# def show_tree():
#     for image in picture:
#         for pixel in image:
#             if pixel:
#                 print('*', end='')
#             else:
#                 print(" ", end='')
#         print('')
        
# show_tree()

# parameters
# def say_hello(name='Darth Vader', emoji=':)'):
#     print(f'hello {name} {emoji}')
# def say_hello(name, emoji):
    
# positional arguments
# say_hello('Kitark', ':)')

# keyword arguments
# say_hello(emoji=':D', name='bibi')
# say_hello()

# def sum(num1, num2):
#     print('hii')
#     return num1 + num2

# should do one thing really well.
# should return something

# total = sum(10, 5)
# print(sum(4,total))

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2 
#     return another_func(num1, num2)

# total = sum(10,20)
# print(total)

# def checkDriverAge(age):
#     if age < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif age > 18:
#         print("Powering On. Enjoy the ride!")
#     elif age == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
        
# checkDriverAge(age=20)

# def some_random_stuff():
#     pass

# some_random_stuff()

# 'hello'.capitalize()

# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)
    
# help(test)
# print(test.__doc__)

# clean code
# def is_odd_or_even(num):
# def is_even(num):
#     return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # return False
    # elif num % 2 != 0:
    #     return False
    
# print(is_odd_or_even(4))  # True
# print(is_odd_or_even(7))  # False

# print(is_even(50))

# *args **kwargs

# def super_func(*args):
# def super_func(*args, **kwargs):
'''
def super_func(name, *args, i='hi', **kwargs):
    # print(args)
    # print(kwargs)
    total =0
    for items in kwargs.values():
        total += items
    # return sum(args)
    return sum(args) + total

print(super_func('Andy',1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
'''
'''
def highest_even(li):
    even = []
    for num in li:
        if num % 2 ==0:
            even.append(num)
    return max(even)


print(highest_even([10,2,3,4,8,11]))
''' 
# := walrus operator
'''

a = 'helllooooooo'

# if (len(a) > 10):
#     print(f"too long {len(a)} elements")
if ((n:=len(a)) > 10):
    print(f"too long {len(a)} elements")
    
while ((n:= len(a)) > 1):
    print(n)
    a = a[:-1]
    
print(a)
'''
# Scope - what variables do I have access to?\
'''
if True:
    x=10
def some_func():
    total =100
    
    
print(x)
'''

# a = 1

# def parent():
#     # a = 10
#     def confusion():
#         # return a
#         return sum
#     return confusion()

# print(a)
# print(parent())

# 1 - start with local
# 2 - parent local
# 3 - global
# 4 - built-in python functions

# total = 0

# def count():
#     # total = 0
#     global total 
#     total += 1
#     return total

# count()
# count()
# print(count())

# def count(total):
#     total += 1
#     return total 

# print(count(count(count(total))))


# Scope - what variables do I have access to?

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
    
outer()

#1 - start with local
#2 - parent local
#3 - global