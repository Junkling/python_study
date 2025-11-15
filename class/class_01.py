# 클래스
# 클래스 & 인스턴스

class Dog:
    name: str
    age: int
    species = 'bull'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.species = species

    def info(self):
        return f'{self.name} is {self.age} years old'
    def speak(self , sound:str):
        return f'{self.name} say {sound}!!'


dog1 = Dog('Bob', 10)
dog2 = Dog('Alice', 20)
dog3 = Dog('Bob', 10)

print(dog1, id(dog1))
print(dog2, id(dog2))
print(dog3, id(dog3))

# toString
print(dog1.__dict__)
print(dog2.__dict__)
print(dog3.__dict__)

print(f'{dog1.name} is {dog1.age} years old and {dog2.name} is {dog2.age} years old')

# 정적 필드라고 보면 됨
print(Dog.species)
# 아래 두개는 정적 필드가 아님으로 애러 (초기화 값이 없음)
# print(Dog.name)
# print(Dog.age)
print(dog1.species)

# self 의 이해
class SelfTest:
    def func1():
        print('func1')
    def func1_self(self):
        print(f'func1 id = {id(self)}')

f = SelfTest()

print(dir(f))

# 에러
# f.func1()

print(f'class id = {id(f)}')
f.func1_self()


SelfTest.func1()
# 에러
# SelfTest.func1_self()
SelfTest.func1_self(f)

class Warehouse:
    stock = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock += 1

    def delete_item(self):
        Warehouse.stock -= 1

user1= Warehouse('Bob')
user2 = Warehouse('Alice')
print(Warehouse.stock)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
user1.delete_item()
print(Warehouse.stock)

print('--------------')
july = Dog('july', 4)
print(july.info())
print(july.speak('월월'))
