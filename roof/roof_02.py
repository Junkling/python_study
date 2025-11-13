# while 문
# while <expr>:
#     <statement(s)>

n = 5

while n > 0:
    print(n)
    n -= 1

print('-------======-------')
arr_1 = ['a', 'b', 'c']

# a 가 있으면!!
while arr_1:
    print(arr_1.pop())

print('-------======-------')
m = 10
while m > 0:
    print(m)
    m -= 1
    if m == 5:
        print('[end]')
        break

print('-------======-------')
m = 10
while m > 0:
    print(m)
    m -= 1
    if m == 5:
        print('[중간]')
        continue
    if m == 0:
        print('[end]')

i = 1
while i <= 10:
    print(f'i = {i}')
    if i == 5:
        print('[end]')
        break
    i += 1

# while-else
print('-------======-------')
k = 10
while k > 0:
    k -= 1
    print(k)
    if k == 5:
        break
else:
    #   while이 돌지 못하는 조건에 닿았을때 실행
    print('[end]')


print('-------======-------')
arr_1 = ['a', 'b', 'c']
str_1 = 'c'
# str_1 = 'z'
r = 0
while r < len(arr_1):
    if arr_1[r] == str_1:
        print(f'found \'{str_1}\' at index {r}')
        break
    r+=1
else:
    print('not exist at arr_1')


print('-------======-------')
arr_2 = ['d', 'e', 'f']

while True:
    if not arr_2:
        print('[end]')
        break
    # print(arr_2.pop())
    print(arr_2.pop(0))