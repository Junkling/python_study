# 람다
# 함수 -> 객체 생섬 및 리소스(메모리 할당)
# 람다 : 즉시 실행 heap 초기화 메모리 초기화
# 가독성 고려해아 써야함

def multiply(num1 , mum2):
    return num1 * mum2


mul_func = multiply(10,50)
mul_lam = lambda x, y: x * y

print(mul_func)
print(mul_lam(10,50))

def func_final(x,y,func):
    return func(x,y)

final = func_final(10, 20, lambda x, y: x - y)
print(final)

