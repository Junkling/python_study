# set
# 중복x, 순서x

a = set()
print(type(a))

# 아래 방식 권장되지 않나봄..
b = set([1, 2, 3, 4, 5])
c = set([3, '4', '6', 2, 1])
d = set([1, 1, 1, 1, 2])
# 리스트는 안되는듯
# e = {'a', 'b', (1,2) , ['hello', 'world']}
e = {'a', 'b', (1, 2)}

print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)

print(2 in b)

t_b = tuple(b)
l_c = list(c)
print(type(t_b), t_b)
print(type(l_c), l_c)

f = {1, 2, 3, 4, 5, 6, 7}
g = {4, 5, 6, 7, 8, 9, 10}

# 교집합
f_g = f & g
print(type(f_g), f_g)
print(f.intersection(g))

# 합집합
f_or_g = f | g
print(type(f_or_g), f_or_g)
print(f.union(g))

# 차집합
f_without_g = f - g
print(type(f_without_g), f_without_g)
print(f.difference(g))

# 중복 원소가 존재하지 않은 집합인가? -> f, g 는 중복 원소가 있기 때문에 False
print('==========')
print('서로 중복 원소가 존재하지 않는가')
print(f.isdisjoint(g))

# 부분 집합 확인 (앞은 뒤의 부분)
h = {1, 2, 3}
print('==========')
print('부분 집합 확인 (앞은 뒤의 부분)')
print(f.issubset(h))
print(h.issubset(f))

# 부분 집합 확인 (뒤는 앞의)
print('==========')
print('부분 집합 확인 (뒤는 앞의)')
print(f.issuperset(h))
print(h.issuperset(f))

# 데이터 추가 제거
set_1 = {1, 2, 3, 4}
set_1.add(5)
print(set_1)

set_1.remove(2)
# 예외 발생
# set_1.remove(10)
print(set_1)

set_1.discard(1)
# 예외 발생하지 않음
set_1.discard(10)
print(set_1)

set_1.clear()
print(set_1)