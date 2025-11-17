# 읽기

# 읽기모드 : r , 쓰기모드 : w , 추가모드 : a , 텍스트모드 : t , 바이너리모드 : b

f = open('../resource/test1.txt' , 'r' , encoding='utf-8')

print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
print(f.read())

f.close()


print('\n==== with문 ====\n')

# with (자동으로 닫기까지함)
with open('../resource/test1.txt' , 'r' , encoding='utf-8') as f1:
    c1 = f1.read()
    print(iter(c1))
    print(list(c1))

print()

# read(10) <- 바이트 수

print('\n==== byte ====\n')
with open('../resource/test1.txt' , 'r' , encoding='utf-8') as f2:
    c2 = f2.read(5)
    print(c2)
    c2 = f2.read(5)
    print(c2)
    f2.seek(0)
    c2 = f2.read(5)
    print(c2)


print()

print('\n==== readline ====\n')

with open('../resource/test1.txt' , 'r' , encoding='utf-8') as f3:
    line = f3.readline()
    print(line)
    line = f3.readline()
    print(line)
    line = f3.readline()
    print(line)

print('\n==== readlines ====\n')
# 배열로 받아서 줄바꾸해서 들어옴
with open('../resource/test1.txt' , 'r' , encoding='utf-8') as f3:
    lines = f3.readlines()
    print(lines)
    print()
    for k,v in enumerate(lines):
        print(f'[{k}] : {v}')