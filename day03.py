# while True:
#     dan = int(input('dan : '))
#     if dan == 0:
#         break
#     if 2 <= dan <= 9:
#         for i in range(1, 10):
#             print(f'{dan} * {i} = {dan * i}')
#     else:
#         continue

num = int(input('input number : '))
cnt = 0

# k = 1
# while k <= num:
#     if num % k == 0:
#         cnt += 1
#     k += 1
# if cnt == 2:
#     print(f'{num} is prime number')
# else:
#     print(f'{num} is not prime number')

# for k in range(1, num+1):
#     if num % k == 0:
#         cnt += 1
#     k += 1
# if cnt == 2:
#     print(f'{num} is prime number')
# else:
#     print(f'{num} is not prime number')

# cnt = 0
# for k in range(2, num):
#     if num % k:
#         cnt += 1
# if cnt:
#     print(f'{num} is prime number')
# else:
#     print(f'{num} is not prime number')

for i in range(2, num):
    if num % i == 0:
        print(f'{num} is not prime number')
        break
else:
    print(f'{num} is prime number')