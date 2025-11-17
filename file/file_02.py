# 쓰기

with open('../resource/test2.txt' , 'w' , encoding='utf-8') as f3:
    f3.write('hello world\n')

with open('../resource/test2.txt' , 'wt' , encoding='utf-8') as f4:
    f4.write('hello world2\n')

with open('../resource/test2.txt' , 'a' , encoding='utf-8') as f5:
    f5.write('hello world3\n')

# writelines
with open('../resource/test2.txt' , 'a' , encoding='utf-8') as f6:
    f6.writelines(['hello world4\n', 'hello world5\n' , 'hello world6\n'])


with open('../resource/test3.txt' , 'a' , encoding='utf-8') as f7:
    print('Test Print File 1' , file=f7)
    print('Test Print File 2' , file=f7)
    print('Test Print File 3' , file=f7)
