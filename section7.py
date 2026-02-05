#Pure Fucntions
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3])) 

# new_list=[]
# def multiply_by2(li):
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# # new_list=''
# print(multiply_by2([1,2,3]))

# map, filter, zip, and reduce
# map(action, iterable)
# def multiply_by2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list

# def multiply_by2(li):
#     return li*2

# # print(map(multiply_by2, [1,2,3]))
# print(list(map(multiply_by2, [1,2,3])))

# my_list = [1,2,3]
# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, my_list)))
# print(my_list)

#filter
# my_list = [1,2,3]
# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))
# print(my_list)

# # zip
# my_list = [1,2,3]
# your_list = [10, 20, 30]
# their_list = (5,4,3)
# def only_odd(item):
#     return item % 2 != 0

# print(list(zip(my_list, your_list)))
# print(list(zip(my_list, your_list, their_list)))
# print(my_list)


# reduce
# from functools import reduce 
# my_list = [1,2,3]

# def multiply_by2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 != 0

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list, 0))
# # 0 1
# # 1 2
# # 3 3
# # 6
# # print(reduce(accumulator, my_list, 10))
# # 10 1
# # 11 2
# # 13 3 
# # 16
# print(my_list)

# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize(item):
#     return item.capitalize()

# print(list(map(capitalize, my_pets)))

# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# def sort(item):
#     return sorted(item)

# print(list(zip(my_strings, sorted(my_numbers))))

# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def over_50(item):
#     return item > 50

# print(list(filter(over_50, scores)))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def accumulator(acc, item):
#     return acc  + item

# print(reduce(accumulator, my_numbers + scores, 0))

# lambda expressions
# lambda param: action(param)

# from functools import reduce


# my_list = [1,2,3]

# def multuply_by2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 != 0

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item%2!=0, my_list)))
# print(reduce(lambda acc, item: acc+item, my_list))

# exercises lambda expressions
#Square
# my_list = [5,4,3]

# new_list = list(map(lambda num: num**2, my_list))
# print(new_list)

# #List Sorting
# a = [(0,2), (4,3), (10, -1), (9,9)]
# a.sort(key = lambda x: x[1])
# print(a)

# Comprehensions
# list, set, dictionary
# my_list = []
# for char in 'hello':
#     my_list.append(char)
    
# print(my_list)
# my_list = [param for param in iterable]
my_list = [char for char in 'hello']
print(my_list)