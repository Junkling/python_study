# dict 타입 (json , 객체 과 유사)
# key , value 형태
# 키값에 순서 없음 (hash , hash_table)
# 키값이 고유함

# 선언

a = {'name': 'kim', 'age': 10}
b = {0: 'hello', 1: 'world'}
c = dict({'arr': [1, 2, 3, 4, 5]})
d = dict([('name', 'kim')])
e = dict(id=1, name='kim', active=True)

# print(type(a))
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)


print(a['name'])
print(a.get('name'))

# 에러
# print(a['active'])

# None (getOrDefault('None') 과 동일한 듯
print(a.get('active'))

a['address'] = 'new york'
a['name'] = 'sam'
print(a)

key_list = ['key1', 'key2', 'key3']
i = 1
for key in key_list:
    a[key] = [i , i +1 , i +2]
    i += 3

print('===========')
print(a)

print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

a.pop('key2')
print(a)

# 3.7 이후 버전부터 마지막 들어온 값을 확정적으로 꺼냄
pop_item = a.popitem()
print(pop_item)
print(a)

a.update(age = 20)
print(a)

temp = {'key1' : 'changed_value'}
a.update(temp)
print(a)