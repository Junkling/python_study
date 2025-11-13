# set
# 중복x, 순서x

a = set()
print(type(a))

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

a_b = a&b
print(type(a_b), a_b)