# 문자열

str1 = '안녕'
str2 = "파이썬"
str3 = '''누구세요'''
str4 = """감사합니다."""

print(type(str1), type(str2), type(str3), type(str4))

print(len(str1), len(str2), len(str3), len(str4))

str5 = ''
str6 = str()

print(type(str5), type(str6))
print(len(str5), len(str6))

print('I\'m boy')
print('I\\m boy')
print('Empty String : \"\"')

# tab 만큼

print('a \t b')

# Row String
raw_str1 = r'D:\python\test'
print(raw_str1)

# 멀티 라인
ml_str = """afsajnflanslfnlksadfnlksadnflkn
sadlkfnladskfnlkasdnflkasnlkfnlaskdfnlksalfnsdlfnlaksdnfls
adnflkansdflksnflksanflksnflasnflkanflasnflkansflnasdklfnalksdnflksdnflksdnflksnfks
anfklnsldkfnsdlkfnsladnflsdnflsaknflskdnf"""

# 멀티 라인
ml_str2 = \
"""afsajnflanslfnlksadfnlksadnflkn
sadlkfnladskfnlkasdnflkasnlkfnlaskdfnlksalfnsdlfnlaksdnfls
adnflkansdflksnflksanflksnflasnflkanflasnflkansflnasdklfnalksdnflksdnflksdnflksnfks
anfklnsldkfnsdlkfnsladnflsdnflsaknflskdnf"""

# 멀티 라인
ml_str3 = \
"afsajnflanslfnlksadfnlksadnflkn" \
"sadlkfnladskfnlkasdnflkasnlkfnlaskdfnlksalfnsdlfnlaksdnfls" \
"adnflkansdflksnflksanflksnflasnflkanflasnflkansflnasdklfnalksdnflksdnflksdnflksnfks" \
'anfklnsldkfnsdlkfnsladnflsdnflsaknflskdnf'

print(ml_str)
print()
print(ml_str2)
print()
print(ml_str3)

# 문자열 연산
str_o1 = "Python"
str_o2 = 'Apple'
str_o3 = 'hello world!'
str_o4 = 'thanks'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1 , 't' not in str_o4 , sep= ' || ')
print()

# 문자열 형변환
print(type(str(66)))
print(type(str(10.1)) == float)

# 첫글자만 대문자로
print("Capitalize: ", str_o4.capitalize())
print('endswith : ' , str3.endswith('!'))
print('replace : ' , str_o2.replace('pple', 'BC'))
print('sorted : ' , sorted(str_o1))
print('split : ', str_o3.split(' '))

# 반복(시퀀스)
in_str = 'good boy and pretty girl'

for i in in_str:
    print(i, end='|')

print()
# 슬라이싱
str_s1 = "Good Game Well Played"
print(str_s1[0:len(str_s1)-10])
print(len(str_s1))
# 0~ 뒤에서부터 9번째까지
print(str_s1[0:-9])
print(str_s1[0:max(len(str_s1)-30 , 1)])
print(str_s1[0:len(str_s1):2])
print(str_s1[0:10:2])
print(str_s1[::2])
print(str_s1[::-1])
print(str_s1[::-2])

# 아스키코드
a = 'z'
print(ord(a))
print(chr(ord(a) -1))
