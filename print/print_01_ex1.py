x = 50
y = 100

text = 210565133
n = 'str'
print('----- V1 -----')
ex1 = 'n = %s , s = %s , sum = %d \n' % (n, text, x + y)
print(ex1)

print('----- V2 -----')

ex2 = 'n = {n} , s = {s} , sum = {sum} \n'.format(n=n, s=text, sum=x + y)
print(ex2)

print('----- V3 -----')

ex3 = f'n = {n} , s = {text} , sum = {x + y} \n'
print(ex3)

print('----- 구분기호 -----')

m = 100000000000
ex4 = f'm : {m:,}\n'
print(ex4)

print('----- 정렬 -----')
# ^ : 가운데 , < : 좌측 , > : 우측
t = 20
print(f't = {t:10}')
print(f'[center] t = {t:^10}')
print(f'[left] t = {t:<10}')
print(f'[right] t = {t:>10}')
print()

print('---------------')
print(f'[center] t = {t:%^10}')
print(f'[left] t = {t:-<10}')
print(f'[right] t = {t:*>10}')
