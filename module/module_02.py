# 모듈 사용
from module.module_01 import add, minus, multiply, divide, power
import sys

# print(sys.path)
# sys.path.append()

a = add(1, 2)
b = minus(1, 2)
c = multiply(1, 2)
d = divide(1, 2)
e = power(1, 2)

#
print('-'*15)
print('import call')
print(a)
print(b)
print(c)
print(d)
print(e)


# __name__ 사용
