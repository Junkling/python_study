# 함수 + 람다

# def first_func(x:str|None = ''):
# def first_func(x = ''):
def first_func(x: str = ''):
    print('hello', x)


first_func(3)
first_func()


def return_func(a: str = ''):
    return 'hello, ' + a


x = return_func('world')
print(x)


# 다중반환
def func_mul(x):
    y1 = x * 1
    y2 = x * 2
    y3 = x * 3
    return y1, y2, y3


def func_mul_tup(x) -> tuple:
    y1 = x * 1
    y2 = x * 2
    y3 = x * 3
    return y1, y2, y3


def func_mul_list(x) -> list:
    y1 = x * 1
    y2 = x * 2
    y3 = x * 3
    return [y1, y2, y3]


def func_mul_dict(x) -> dict:
    y1 = x * 1
    y2 = x * 2
    y3 = x * 3
    return {'v1': y1, 'v2': y2, 'v3': y3}


mul = func_mul(3)
print(type(mul))
print(mul)

mul_tup = func_mul_tup(4)
print(type(mul_tup))
print(mul_tup)

mul_list = func_mul_list(5)
print(type(mul_list))
print(mul_list)

mul_dict = func_mul_dict(3)
print(type(mul_dict))
print(mul_dict)

a, b, c = func_mul(3)
print(f'a: {a}, b : {b}, c: {c}')


# 튜플형
def args_func(*args):
    for i, v in enumerate(args):
        print(f'result :{i},{v}')
    print("==============")


args_func('helloworld')
args_func('hello', 'python', '!!')


# (언패킹)-> ** 딕셔너리
def keyword_func(**keyword):
    for v in keyword.keys():
        print(f'[keyword] :{v},{keyword[v]}')
    print("==============")


keyword_func(name1='kim')
keyword_func(name1='kim', name2='na', name3='park', name4='lee')


def example(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example(10, 20, 'lee', 'kim', 'park', age0=0, age1=10, age2=20, age3=30)

# 중첩함수
def nested_func(num):
    def inner_func(num):
        print(num)
    print('in func')
    inner_func(num + 100)

nested_func(10)
# 내부 함수는 호출 불가
# inner_func(10)
