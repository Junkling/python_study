# 파이썬 함수 기초

def say_hello():
    print("hello world")

say_hello()

def say_by_arg(arg):
    print(f'hello {arg}')

say_by_arg('user')

def return_function(a, b):
    return a + b

x = return_function(3, 5.5)
print(x)

def add_string(a:str, b:str) -> str:
    return a + " " + b
y = add_string('Python' , 'good')
print(y)