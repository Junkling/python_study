# 외장함수
# sys.argv 찾아보기!
import sys
print(sys.argv)

# 강제 종료
# sys.exit()

# 패키지 위치
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# 쓰기
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 쓰기
f = open('test.obj', 'rb')
obj = pickle.load(f)
print(obj, type(obj))
f.close()

# os : 환경변수, 디렉토리(파일) , os 명령어
import os
# print(os.environ)
print(os.environ["PYENV_ROOT"])
print(os.getcwd())

# time
import time

print(time.time())
print(time.localtime(time.time()))

print(time.ctime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# for i in range(5):
#     print(i)
#     time.sleep(1)

import random

# 0~1 실수
print(random.random())
print(random.randint(1, 45))
print(random.randrange(1, 45))

# shuffle
d = [1,2,3,5,6]
random.shuffle(d)
print(d)

# 무작위 선택
c = random.choice(d)
print(f'choice = {c}')

import webbrowser
webbrowser.open('https://www.google.com')
webbrowser.open_new('https://www.google.com')