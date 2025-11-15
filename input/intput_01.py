# 인풋 -> 기본 타입 str

# name = input("Enter your name: ")
#
# grade = input("Enter your grade: ")
#
# company_name = input("Enter your company name: ")
#
# print(f'name : {name}, grade : {grade}, company_name : {company_name}')
#

# num = input('Enter a number: ')
# name = input('Enter a name: ')
# print(type(num) , num , num*3)
# print(type(name) , name)

# # 형변환
# first_num = int(input('First number: '))
# second_num = int(input('Second number: '))
#
# func_mul_num = lambda x, y: x * y
#
# print ('func mul result = ',func_mul_num(first_num, second_num))
# 형변환
first_num = float(input('First number: '))
second_num = float(input('Second number: '))
print(type(first_num))
print(type(second_num))
func_mul_num = lambda x, y: x * y

print ('func mul result = ',func_mul_num(first_num, second_num))
