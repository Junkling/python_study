# 리스트

# 선언
arr1 = []
arr2 = list()
arr3 = [10, 20, 30, 40]
arr4 = [10, 20.0, '30']
arr5 = [10, 20.0, ['30', '40', '50'], True]

print('arr4 = ', type(arr4), arr4)
print('arr4[2] = ', arr4[2])
print('arr3[1] + arr3[1] + arr3[0] = ', arr3[1] + arr3[1] + arr3[0])
print('arr5[-1]', arr5[-1])
print('arr5[-2][1]', arr5[-2][1])
print('list(arr4[2])', list(arr4[2]))

# 슬라이싱
print('arr5 slice = ', arr5[0:3])
print('arr5 slice = ', arr5[2][0:2])

# 리스트 연산
print('arr4 + arr5 = ', arr4 + arr5)
print('arr4 * 2 = ', arr4 * 2)
# print('\"Test\" + arr3[0] = ', 'Test' + arr3[0]) # ->error
print('\"Test\" + arr3[0] = ', 'Test' + str(arr3[0]))  # ->error
print('\"Test\" * arr4[2] = ', 'Test' * int(arr4[2]))

print(arr5 == arr5[:2] + arr5[2:])
print(arr5)
print(arr5[:2])
print(arr5[2:])
print(arr5[:2] + arr5[2:])

temp = arr5

print(f'id(temp) = {id(temp)} , id(arr5) = {id(arr5)})')

# 리스트 수정 삭제
arr5[0] = 1
print(arr5)
arr5[0:1] = ['a', 'b', 'c']
print(arr5)

arr5[1] = ['a', 'b', 'c']
print(arr5)

arr5[0:2] = []
print(arr5)

del arr5[0]
print(arr5)

list1 = [5,1,3,4,2]
list1.append(6)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

print(list1.index(3))

list1.insert(2, 10)
print(list1)

list1.remove(10)
print(list1)
print(list1.pop())
print(list1)

list1.append(3)
print(list1)
print(list1.count(3))

list1.extend([10,20])
print(list1)

while list1:
    data = list1.pop()
    print(data)

print(list1)