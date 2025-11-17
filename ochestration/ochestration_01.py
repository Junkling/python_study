# 파이썬 입문 통합
import time

name = input("What is your name? ")

print("Hello, " + name, " time to paly game")

print()

time.sleep(1)

print("Start Loading...")

print()

time.sleep(0.5)

# 정답
word = 'secret'

# 추측 단어
guesses = list('_' * len(word))

max_count = 10

while 0 < max_count:

    print()
    user_answer = input("What is this word ?")
    if len(user_answer) > 1:
        print("Only one letter allowed")
        continue

    if user_answer == word:
        print("Correct")
        break

    failed = True
    for index, char in enumerate(word):
        if char in user_answer:
            guesses[index] = char
            failed = False
        # print(index)

    if failed:
        max_count -= 1
        print(f'{max_count} chances left')
        failed = False

    guess = ''
    for s in guesses:
        guess += s

    for i in guess:
        print(i, end=' ')

    if list(word) == guesses:
        print("\nCorrect")
        break
