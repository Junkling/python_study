# if 문
# True -> 0이 아닌 수, 길이가 0이 아닌 모든 데이터
# False -> 0인 수 , 길이가 0인 데이터

if True:
    print('good')

if False:
    print('bad')

if 'a':
    print('a')

if '':
    print('empty')

if False:
    print('bad')
else:
    print('good!')

#  관계 연사자 관련
x = 15
y = 10
if x == y:
    print('x equals y')

if x < y:
    print('x less than y')

if x > y:
    print('x greater than y')
if x <= y:
    print('x less than or equal to y')

if x >= y:
    print('x greater than or equal to y')
print('================')

str = ''
if str:
    print(f'str = {str}')
else:
    print(f'str is empty')
print('================')
str = 'hello'
if str:
    print(f'str = {str}')
else:
    print(f'str is empty')

# 논리 연산자

a = 70
b = 30
c = 10
print('================')
print(f'and = {a > b and c > a}')
print(f'and = {a > b and c < a}')

print('================')
print(f'or = {a > b or c > a}')
print(f'or = {a > b or c < a}')

print('================')
print(f'not = {not b > a}')
print(not True)
print(not False)

print('========else-if 문========')
num = 90
if num > 90:
    print('Grade : A')
elif num > 70:
    print('Grade : B')
elif num > 60:
    print('Grade : C')
elif num > 50:
    print('Grade : D')
else:
    print('Grade : F')

print('========중첩 if문========')
grade = 'A'
total = 95
if grade == 'A':
    if total >= 90:
        print('장학금 100')
    elif total >= 80:
        print('장학금 80')
    else:
        print('장학금 50')
else:
    print('장학금 대상 아님')

# in , not in

arr_1 = [10, 20, 30]
arr_2 = [50, 60, 70, 80]
dict_1 = {"name": "kim", 'city': 'seoul', 'grade': 'A'}
arr_3 = (10, 12, 14)

print(f'10 in arr_1 = {10 in arr_1}')
print(f'10 not in arr_1 = {10 not in arr_1}')
print(f'\"name\" in dict_1 = {"name" in dict_1}')
print(f'\"seoul\" in dict_1 = {"seoul" in dict_1}')
print(f'\'seoul\' in dict_1.values() = {'seoul' in dict_1.values()}')
print(f'dict_1[\"name\"] == \"kim\" = {dict_1["name"] == "kim"}')
