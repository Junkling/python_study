# 자료형
"""
int
float
bool
str
list
tuple
set
dict
"""

# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'hello'
float1 = 1.5
int1 = 7
list1 = [str1, str2]
dict1 = {
    "name": str1,
    "version": float1
}
tuple1 = (str1, str2)
tuple2 = str1, str2
set1 = {7, 8, 9}

print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict1))
print(type(tuple1))
print(type(set1))

# 숫자형
"""
+
-
*
/ : 나누기
// : 몫
% : 나머지
abs() : 절대값
pow(x,y) : x의 y 제곱
"""

# 정수
i1 = 77
i2 = -77
big_int = 453125687656532155135165131

print(i1)
print(i2)
print(big_int)
print()

# 실수
f1 = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f1)
print(f2)
print(f3)
print(f4)
print()

# 연산

a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

#형 변환
print(int(a))
print(float(b))
print(int(c))
print(int(d))

print(complex(3))
print(complex('3'))

print(abs(-10))

x , y = divmod(100,8)
print(x, y , sep = ' || ')

print(pow(5,3))

import math

print(math.pi)
