# Errors in Python
# Error Handling
# def hoooohoo()
# 1 + Name

# hoooohoo()
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         10/age
#         # print(age)
#     except ValueError:
#         print("Please enter a number")
#     except ZeroDivisionError:
#         print('please enter age higher then 0')
#     else:
#         print("thank you!")
#         break

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'please enter numbers {err}')

# print(sum(1, '2'))

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
        
# # print(sum(1, 0))
# print(sum(1, '2'))

while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise Exception('hey cut it out')
    # except ValueError:
    #     print('please enter a number')
    #     continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you!')
        # break
    finally:
        print('ok, I am finally done')
    print('can you hear me?')