# myfile = open('1.txt')

# print(myfile.read())
# myfile.seek(0)
# print(myfile.read())

# myfile= open('test.txt')
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# myfile= open('test.txt')

# print(myfile.readlines())

# myfile.close()

# with open('test.txt') as myfile:
#     print(myfile.readlines())
    
# with open('tests.txt', mode='a') as myfile:
#     text = myfile.write('hey it\' me!')
#     print(text)
    
    
# with open('tests.txt', mode='w') as myfile:
#     text = myfile.write('hey it\' me!')
#     print(text)
    
# with open('tests.txt', mode='_r+_') as myfile:
#     text = myfile.write('hey it\' me!')
#     print(text)
    

with open('sad.txt', mode='w') as myfile:
    text = myfile.write('hey it\' me!')
    print(text)