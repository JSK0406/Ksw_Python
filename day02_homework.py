import random
#
# secret = random.randint(1, 10)
# guess = int(input('정답은 ? : '))
#
# if secret > guess:
#     print(f'too low, 정답은 :{secret}')
# elif secret < guess:
#     print(f'too high, 정답은 :{secret}')
# else:
#     print('just right')

small = random.choice([True, False])
green = random.choice([True, False])

print(small, green)
if green:
    if small:
        print('강낭콩')
    else:
        print('수박')
else:
    if small:
        print('체리')
    else:
        print('호박')