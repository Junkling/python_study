# for문
# for in <collection>
#     <roof body>
import random
from re import Match

print("=====range(10)=====")
for v1 in range(10):
    print(f'v1 = {v1}')

print("=====range(1, 11)=====")
for v2 in range(1, 11):
    print(f'v2 = {v2}')

print("=====range(1, 11 ,2)=====")
# 3번째는 그 수만큼 띄워서 실행
# for v3 in range(1, 11 ,2):
for v3 in range(1, 11, 3):
    print(f'v3 = {v3}')

print("=====roof_sum=====")
roof_sum = 0
for v3 in range(1, 1001):
    roof_sum += v3
print(roof_sum)

print("=====sum(range)=====")
print(type(range(1, 10)))
print(sum(range(1, 1001)))
# 4의 배수의 합
print(sum(range(4, 1001, 4)))

print("=====Iterables=====")
# 문자열 , 리스트 , 튜플 , 셋 , 객체
# iterable 리턴 함수 : range , reversed , enumerate , filter , map , zip
str_list = ['a', 'b', 'c', 'd', 'e']

for n in str_list:
    print(n)

for index, value in enumerate(str_list):
    print(f'index({index}) = {value}')

lotto = set()
while len(lotto) < 6:
    lotto.add(random.randint(1, 45))

print(lotto)

my_dict = {
    'name': 'kim',
    'age': 20,
    'address': 'seoul'
}

print("=====dict=====")
for key in my_dict:
    print(f'{key} = {my_dict[key]}')

print("=====dict.items()=====")
for key, value in my_dict.items():
    print(f'{key} = {value}')

str1 = "FiNeApPlE"
print("=====str=====")
for n in str1:
    if n.isupper():
        print(n.lower(), end='')
    else:
        print(n, end='')
print()
print("=====break=====")
num_arr = [12, 45, 66, 88, 99, 14, 22, 100]
for n in num_arr:
    if n == 45:
        print(f'found {n}')
        break
    else:
        print(n)

print("=====continue=====")
type_arr = ['1', 45, 66, True, 9.9, complex(14), 22, 100]
for n in type_arr:
    if type(n) is bool:
        continue
    print(type(n), n)

print("=====for-else=====")

num_arr_2 = [12, 45, 66, 88, 99, 14, 22, 100]
found = 65
for index, num in enumerate(num_arr_2):
    if num == found:
        print(f'found {num}')
        break
else:
    # n은 끝까지 온다
    print(f'can not found({found}) roof-count : {index + 1} ')

print('구구단')
for i in range(2, 10):
    print(f'====={i}단=====')
    for j in range(1, 10):
        print(f' {i} * {j} = {i * j}')

# 변환 예제
name_1 = 'korea'
# 객체가 나옴
print(f'reversed : {reversed(name_1)}')
# 형변환
print(f'reversed : {list(reversed(name_1))}')
print(f'reversed : {tuple(reversed(name_1))}')
print(f'reversed : {set(reversed(name_1))}')
print(f'reversed : {''.join(reversed(name_1))}')
