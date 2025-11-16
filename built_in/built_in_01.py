# 파이썬 빌트인 함수

# 절대값
print(f'{abs(-3)}')

# 이터레이터 요소 검사(참, 거짓)

# all -> 모두 참
print('=' * 5, 'all', '=' * 5)
print(all([1, 2, '3']))
print(all([1, 2, '']))

# any -> 하나라도
print('=' * 5, 'any', '=' * 5)
print(any([1, 2, 0]))
print(any([1, 2, '']))

print('=' * 5, 'chr', '=' * 5)
# chr : 아스키 -> 문자 , ord : 문자 -> 아스키
print(chr(67))
print('=' * 5, 'ord', '=' * 5)
print(ord('a'))

# enumerate : 인덱스 + Iterable 객체
print('=' * 5, 'enumerate', '=' * 5)
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)


# filter
def conv_pos(x):
    return abs(x) > 2


print('=' * 5, 'filter', '=' * 5)
print(list(filter(conv_pos, [1, 2, 3])))
print(list(filter(lambda x: abs(x) > 2, [1, 2, 3])))

# id : 객체 레퍼런스
print('=' * 5, 'id', '=' * 5)
print(id(int(5)))

# len : 길이
print('=' * 5, 'len', '=' * 5)
print(len('asdfasdfsadf'))
print(len([1, 2, 3, 4, 6, 6]))

# min max
print('=' * 5, 'max', '=' * 5)
print(max(1, 2, 3, 5, 6, 7))
print(max('python'))
print('=' * 5, 'min', '=' * 5)
print(min(1, 2, 3, 5, 6, 7))
print(min('python'))

# map
print('=' * 5, 'map', '=' * 5)
print(list(map(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])))

# pow
print('=' * 5, 'pow', '=' * 5)
print(pow(2,10))

# range
print('=' * 5, 'range', '=' * 5)
print(range(1,10,2))
print(list(range(0,10,2)))
print(list(range(0,-20,-3)))

# round
print('=' * 5, 'round', '=' * 5)
print(round(3.14123123123,4))
print(round(9.2))
print(round(8.7))

# sorted
print('=' * 5, 'sorted , reversed', '=' * 5)
l = [6,8,3,4,12]
print(sorted(l))
print(list(reversed(l)))

print('=' * 5, 'sum', '=' * 5)
print(sum(l))
print(sum(range(1,101)))

# type
print('=' * 5, 'type', '=' * 5)
print(type(range(1,101)))
print(type([1,2]))
print(type((1,2)))
print(type('str'))
print(type(True))
print(type(5))

# zip : Iterable의 요소를 묶어 반환
list1 = list(zip([1, 2, 3, 4], [6, 7, 8, 9, 3]))

print(list1)
print(list(zip(list1, [1,2,3,5,5])))



