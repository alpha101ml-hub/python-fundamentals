try: 
    with open('sad.txt', mode='r') as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print("File not found")
    raise err
except IOError as err:
    print('IO error')
    raise err