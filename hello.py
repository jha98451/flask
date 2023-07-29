import os
path = "Jha"
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)
print('Hello Jha')
