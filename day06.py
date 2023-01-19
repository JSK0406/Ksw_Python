# # generator
#
# def a():
#     yield 1
#     yield 2
#     yield 3
#
#
# def b():
#     return 1
#     return 2
#     return 3
#
# # decorator
#
# # general decorator
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('running function:', func.__name__)
#         print('positional arguments:', args)
#         print('keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return new_function
#
# def add_ints(a, b):
#     return a + b
#
# cooler_add_ints = document_it(add_ints)
# print(cooler_add_ints(3,5))
#
# # special decorator
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('running function:', func.__name__)
#         print('positional arguments:', args)
#         print('keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return new_function
#
# @document_it
# def add_ints(a, b):
#     return a + b
#
# print(add_ints(3,5))


# recursion

# def factorial_iter(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
#
#
# def factorial_recursion(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial_recursion(n-1) * n
#
#
# print(factorial_iter(5))
# print(factorial_recursion(5))

# exception

# try:
#     expression = input('분자 분모 입력: ').split()
#     print(int(expression[0]) / int(expression[1]))
# except ValueError:
#     print('숫자를 입력해주세요')
# except ZeroDivisionError as err:
#     print('분모에 0이 올 수 없습니다.')
#     print(err)
# except IndexError as err:
#     print('예외 발생')
#     print(err)
# else:
#     print('프로그램 정상', end=" ")
# finally:
#     print('종료')

