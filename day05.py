import random
from typing import Dict


# function

# def isprime(n):
#     """
#     매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
#     :param n: integer number
#     :return: value, type of bollean
#     """
#     if n <= 1:
#         return False
#     for k in range(2, n):
#         if n % k == 0:
#             return False
#     else:
#         return True
#
#
# start = int(input("input start number: "))
# end = int(input("input end number: "))
#
# if end < start:
#     start, end = end, start
#
# for i in range(start, end + 1):
#     if isprime(i):
#         print(i, end=' ')
#
# help(isprime)

# def do_nothing():
#     pass
#
#
# do_nothing()
# print(do_nothing())

# mamamoo = ['화사', '솔라', '휘인', '문별']
# print(mamamoo.pop())  # 삭제하면서 그 값 리턴
# print(mamamoo.remove('문별'))  # 삭제만 하고 리턴값 없음
# print(mamamoo)
#
# A = None
#
# if A is None:
#     print('O')
# print(type(A))


# def menu(wine, entree, dessert):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
#
# # 위치 인수
# print(menu('chardonnay', 'chicken,', 'cake'))
#
# # 키워드 인수
# print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# 기본 매개변수 값 지정하기
# def menu(wine, entree, dessert='pudding'):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
#
#
# print(menu('chardonnay', 'chicken'))  # 기본값 지정 상태에서 변수를 안 주면 기본값
# print(menu('dunckelfelder', 'duck', 'doughnut'))  # 기본값 지정 상태에서 변수를 주면 입력한 값
# dessert='ABC'
# print(menu('chardonnay', 'chicken'))

# 위치 인수(애스터리스크)
# def print_args(*args):
#     print("Positional tuple:", args)
#
#
# print_args()
# print_args(1, 2, 3)


# def calculate_fee(args) -> list:
#     """
#     놀이공원 요금 계산
#     :param args: 나이의 리스트
#     :return: 아이 수, 어른 수, 금액
#     """
#     total = 0
#     adults = 0
#     kids = 0
#     for age in args:
#         if 19 <= age:
#             total += 10000
#             adults += 1
#         else:
#             total += 3000
#             kids += 1
#     return kids, adults, total
#
#
# answer = calculate_fee(lst := [random.randint(1, 50) for _ in range(int(input("인원을 입력해주세요: ")))])  # (kids, adults, total)
# print(f'전체 {answer[0]+answer[1]}명 중 아이: {answer[0]}명, 어른: {answer[1]}명, 금액: {answer[2]}원입니다.')
# print(lst)

# def calculate_fee(args) -> dict[str, int]:
#     """
#     놀이공원 요금 계산
#     :param args: 나이의 리스트
#     :return: 아이 수, 어른 수, 금액
#     """
#     total = 0
#     adults = 0
#     kids = 0
#     for age in args:
#         if 19 <= age:
#             total += 10000
#             adults += 1
#         else:
#             total += 3000
#             kids += 1
#     return {'아이': kids, '어른': adults, '금액': total}
#
#
# answer = calculate_fee(lst := [random.randint(1, 50) for _ in range(int(input("인원을 입력해주세요: ")))])  # (kids, adults, total)
# print(f'''전체 {len(lst)}명 중 아이: {answer['아이']}명, 어른: {answer['어른']}명, 금액: {answer['금액']}원입니다.''')
# print(lst)

# def answer():
#     print(42)
#
#
# def call_func(f):
#     """
#     매개변수로 함수를 넘겨 받아 실행
#     :param f: 함수
#     :return: None
#     """
#     f()
#
#
# call_func(answer)

# def add_args(arg1, arg2):
#     print(arg1 + arg2)
#
#
# def run_something_with_args(func, arg1, arg2):
#     func(arg1, arg2)
#
#
# run_something_with_args(add_args, 1, 2)

# def subtract(n1, n2):
#     print(n1 - n2)
#
#
# def run_func(func, arg1, arg2):
#     """
#     함수를 매개변수로 받아 함수 안에서 해당 함수를 실행
#     :param func: 첫 번째 변수는 함수
#     :param arg1: 정수 값
#     :param arg2: 정수 값
#     :return:
#     """
#     func(arg1, arg2)
#
#
# run_func(subtract, 99, 88)


# inner func
# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)
#
#
# print(outer(4, 7))

# def knights2(saying):
#     def inner():
#         return "we are the %s" % saying
#     return inner

# closure

# def calculate(n):  # n??
#     x = 1
#     y = 2
#     tmp = 0
#     def add_sub():
#         nonlocal tmp
#         tmp = tmp + x + n + y
#         return tmp
#     return add_sub
#
#
# c1 = calculate(5)
# print(c1)

# lambda

num_lst = [random.randint(1, 100) for _ in range(5)]
def process(numbers, f):
    for num in numbers:
        print(f(num))

process(num_lst, lambda x: x * x)



# def process(num_lst, f):
#     for num in num_lst:
#         print(f(num))
# def squares(n):
#     """
#     제곱 함수
#     :param n: integer
#     :return: integer
#     """
#     return n * n
#
#
# print(numbers)
# process(numbers, squares)
