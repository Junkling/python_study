# 예외
# 컴파일 에러, 런타임 에러

# SyntaxError : 문법 오류
# print('error'))
# print('error)
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 20
# print(c)

# ZeroDivisionError
# print(100/0)

# IndexError
# x = [1, .2, 3]
# print(x[4])
# x.pop()
# x.pop()
# x.pop()
# x.pop() <- 이미 없어 애러 발생

# KeyError
dic = {'name' : 'lee' , 'age': 10 , 'city' : 'seoul'}
# 없는 키값 접근 에러
# print(dic['hobby'])

# None
print(dic.get('hobby'))

# import time
# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용
# print(time.time2())

# ValueError
x = [10 ,20 ,30]
x.remove(10)
print(x)
# 값을 찾을수 없어 에러 발생
# x.remove(200)

# FileNotFoundError
# 파일이 없어 에러 발생
# f = open('test.txt')

# TypeError
x = [1,2]
y = (1,2)
z = 'test'

# 서로 다른 타입(리스트, 튜플) 으로 인한 타입 에러
# print(x + y)
# print(x + z)
# print(z + y)

# catch
# try
# except (애러명1)
# except (애러명2)
# else : try 블록에 에러가 없을 경우
# finally : 항상 실행

name = ['kim', 'lee', 'park']
# 예시 1
try:
    # z= 'kim'
    z= 'sam'
    x = name.index(z)
    print(f'{z} found in {name} at index {x}')
except ValueError:
    print(f'{z} not in {name} [ValueError]')
else:
    print(f' ok [else]')

print('pass')

# 예시 2
try:
    # z= 'kim'
    z= 'sam'
    x = name.index(z)
    print(f'{z} found in {name} at index {x}')
except:
    print(f'{z} not in {name} [exception]')
else:
    print(f' ok [else]')

print('pass')

# 예시 3
try:
    # z= 'kim'
    z= 'sam'
    x = name.index(z)
    print(f'{z} found in {name} at index {x}')
except Exception as e:
    print(f'{z} not in {name} [{e.__class__.__name__}]')
else:
    print(f' ok [else]')
finally:
    print(f' ok [finally]')

print('pass')

# 예시 4
# raise 키워드로 직접 에러 발생
try:
    # z= 'kim'
    a= 'park'
    if(a == 'Kim') :
        print(f'OK Pass')
    else:
        raise ValueError
except Exception as e:
    print(f'\'a\' is not {a} [{e.__class__.__name__}]')
else:
    print(f' ok [else]')
finally:
    print(f' ok [finally]')

print('pass')
