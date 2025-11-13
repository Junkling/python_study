# 튜플
# 리스트와 비교
# 튜플 -> 불변 리스트(수정 삭제 x)


# 선언

t1 = ()
t2 = (1,)
t2 = (1, 2)
t3 = (10, 11, 12, 13, 14)
t4 = (100, 200, 300, 'hello', 'python')
t5 = (100, 200, 300, 'hello', 'python', ('list', 'tuple'))

print(f't4[3] = {t4[3]}')
print(f't4[-1] = {t4[-1]}')
print(f't4[0] + t4[1] = {t4[0] + t4[1]}')
print(f't5[-1][1] = {t5[-1][1]}')
print(f't5[-1] = {t5} || type(t5[-1]) = {type(t5)}')
print(f't5 = {t5} || type(list(t5)) = {type(list(t5))}')

# error (튜플의 값은 변경 불가능)
# t4[0] = 1
print(f't4[:3] = {t4[:3]}')

list_t4 = list(t4)

list_t4[0] = 1
print(f'type(list_t4) = {type(list_t4)}')

print(f't4 + t5 = {t4 + t5}')
print(f't4 *2 = {t4 * 2}')

print(f't4.index(100) = {t4.index(100)}')
print(f't4.count(200) = {t4.count(200)}')

# 패킹 언패킹
t6 = ('a', 'b', 'c', 'd')

(x1, x2, x3, x4) = t6
print(f'[value] x1 = {x1} | x2 = {x2} | x3 = {x3} | x4 = {x4}')
print(f'[type]  x1 = {type(x1)} | x2 = {type(x2)} | x3 = {type(x3)} | x4 = {type(x4)}')

t7 = 1, 2, 3
t8 = 1,

y1, y2, y3 = t7
y4, = t8

print(f'y1 = {y1} , y2 = {y2} , y3 = {y3} , y4 = {y4}')
print(f'y4 = {y4}')
