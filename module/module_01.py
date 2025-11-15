# 모듈
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b


#
# print('-'*15)
# print('inner call')
# print(add(1, 2))
# print(minus(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))
# print(power(1, 2))

if __name__ == "__main__":
    print('-'*15)
    print('main call')
    print(add(1, 2))
    print(minus(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))
    print(power(1, 2))
