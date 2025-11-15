# 형변환 애러


# def parse_input():
#     num = 0
#     try:
#         num = int(input('Enter a number: '))
#     except ValueError:
#         print('Please enter a number')
#         parse_input()
#     return num
#
# parsed = parse_input()
#
# print(type(parsed), parsed)


def parse_float(prompt, on_error=None):
    try:
        return float(input(prompt))
    except ValueError as e:
        if on_error:
            return on_error(e)  # 콜백 실행
        else:
            print("입력 오류:", e)
            return None


# f = parse_float(
#     "Enter float number: ",
#     lambda e: print("타입 오류!")  # return None 자동
# )
# print(type(f),f)

f2 = parse_float(
    "Enter float number: ",
    lambda e: parse_float("is not float Enter again: ")
)

print(type(f2), f2)
