# 선언
print('==========선언==========')
n = 700
print(n * 3)
print(f'type : {type(n)}')
print()

# 동시 선언
print('==========동시 선언==========')
x = y = z = 100
print(f'x : {x}, y : {y}, z: {z}')
print()

# 재선언
print('==========재선언==========')
var = 70
print(f'var(bf) : {var}')
print(f'type(var(bf)) : {type(var)}')
var = 'changed'
print(f'var(af) : {var}')
print(f'type(var(af)) : {type(var)}')
print()

print('==========객체 참조==========')
# Object Reference (객체 참조)
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 출력
# 4. 재할당시 1~3 그대로 반보
print('인트타입 객체 생성 -> 700 할당 -> print() 함수 실행')
print(700)  # -> 인트타입 객체 생성 -> 700 할당 -> print() 함수 실행
print()

print('==========객체 참조==========')
# 예시
var2 = 7777
print(f'var2 : {var2}', f'var2 type : {type(var2)}', sep='\n')  # -> 인트타입 객체 생성 -> 700 할당 -> print() 함수 실행
print()

var3 = var2
print(f'var3 : {var3} , var2 : {var2}')

var2 = 'changed var2'
print(f'var3 : {var3} , var2 : {var2}')

print('==========id(identity)==========')
# id(identity) 객체 고유값
m = 800
n = 600

print(id(m))
print(id(n))


print('==========재할당 시 당연히 똑같음==========')
m = n
print(id(m))
print(id(n))
print(f'equals = {id(m) == id(n)}')

print('==========같은 값을 할당하면 똑같음==========')
a = 800
b = 800
print(id(a))
print(id(b))
print(f'equals = {id(a) == id(b)}')
print()
n = 600
print(id(m))
print(id(n))
print(f'equals = {id(m) == id(n)}')


print('==========문자열도 같은가?==========')
str1 = 'str1'
str2 = 'str2'

print(f'str1 : {str1}')
print(f'str2 : {str2}')
print(f'equals = {str1 == str2}')

print()

str2 = str1
print('str2 = str1')
print(f'str1 : {str1}')
print(f'str2 : {str2}')
print(f'equals = {str1 == str2}')
print()

str3 = 'str1'

print('str3 = "str1"')
print(f'str3 : {str3}')
print(f'str2 : {str2}')
print(f'equals = {str3 == str2}')

# 파이썬 규칙
# 메서드 : 카멜케이스
# 클레스 : 파스칼 (대문자 시작 카멜)
# 변수 : 스네이크 케이스(자바와 차이) -> 변수는 숫자로 시작하지만 않으면 됨(자바와 동일)


"""
# 🐍 Python 예약어 정리 (Python 3.11 기준)

False      : 불리언 거짓값
None       : '값이 없음'을 나타내는 상수
True       : 불리언 참값

and        : 논리 AND
or         : 논리 OR
not        : 논리 부정(NOT)

as         : import나 예외 처리 시 별칭(alias) 지정
assert     : 조건이 거짓이면 AssertionError 발생
break      : 반복문 강제 종료
class      : 클래스 정의
continue   : 반복문 다음 반복으로 건너뜀
def        : 함수 정의
del        : 객체(변수, 원소 등) 삭제
elif       : if ~ elif ~ else 조건 분기
else       : 조건문, 반복문 등에서 '그 외' 처리
except     : 예외 발생 시 처리 블록
finally    : try 블록 종료 후 반드시 실행되는 블록
for        : 반복문
from       : import 시 특정 모듈에서 일부만 가져오기
global     : 전역 변수 선언
if         : 조건문
import     : 외부 모듈 불러오기
in         : 포함 여부 검사 (예: x in list)
is         : 객체 동일성 비교 (==과 다름)
lambda     : 익명 함수 생성
nonlocal   : 중첩 함수 안에서 바깥 함수의 변수 참조
pass       : 아무 동작도 하지 않음 (placeholder)
raise      : 예외 발생
return     : 함수에서 값 반환
try        : 예외 처리 블록 시작
while      : 조건이 참일 동안 반복
with       : 컨텍스트 관리자 사용 (리소스 자동 해제)
yield      : 제너레이터에서 값 반환 (상태 유지)
async      : 비동기 함수 정의 (await와 함께 사용)
await      : 비동기 작업 완료를 기다림
"""
