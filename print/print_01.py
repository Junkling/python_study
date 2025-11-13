# 기본 개행
# 4가지 문자열 표현식 통상적으로 ' 사용

print('Hello World1')
print("Hello World2")
print('''Hello World3''')
print("""Hello World4""")

# end 작성시 개행 되지 않고 해당 문자가 마지막에 붙음 , end 값 없으면 자동 개행
print('P', 'Y', 'T', 'O', 'N', sep='-', end='!')
print('P', 'Y', 'T', 'O', 'N', sep='-')
print('010', '1234', '5678', sep='-', end='')
print('010', '1234', '5678', sep='-')
print('test', 'gmail,com', sep='@', end='')
print('test', 'gmail,com', sep='@')

# file 옵션
import sys

print('Learn Python', file=sys.stderr)

# format (d : 숫자 , s : 문자열 , f : 소수)
print('%s %s' % ('one', 'two',))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 2))

# %s
print('''
  ======
//  %s  //
 ======''')

print('--------------')
print('%10s' % ('nice123'))
print('{:>10}'.format('nice123'))

print('--------------')
print('%-10s' % ('nice123'))
print('{:10}'.format('nice123'))

print('--------------')
print('{:!>10}'.format('nice123'))
print('{:^10}'.format('nice'))

print('--------------')
print('%.5s' % ('nice123'))
print('%5s' % ('nice123'))

print('--------------')
print('{:10.5}'.format('nice123'))
print('{:^10.5}'.format('nice123'))


print('''
  ======
//  %d  //
 ======''')
# %d
print('--------------')
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))


print('''
  ======
//  %f  //
 ======''')
# %d
print('--------------')
print('%f'% (3.1419132131231))
print('{:f}'.format(3.1419132131231))

# 반올림
print('%1.3f'% (3.1419132131231))
print('%06.2f'% (3.1419132131231))
print('{:06.2f}'.format(3.1419132131231))
