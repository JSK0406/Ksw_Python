import random

# students = {'name': 'Kim inha', 'age': 23, 'eyes': [0.9, 11]}
# # for k in students.keys():
# # for k in students.values():
# for (k, v) in students.items():
#     print(f'{k} : {v}')
# print(f'''이름은 {students['name']} 나이는 {students['age']}''', end="")

# alcohol_foods = {
#     '맥주': '치킨', '소주': '골뱅이소면', '와인': '치즈', '고량주': '짬뽕'
# }
# alcohol_lst = list(alcohol_foods.keys())
# food_lst = list(alcohol_foods.values())
#
# while True:
#     alcohol = input(f'술을 선택하세요 1) {alcohol_lst[0]} 2) {alcohol_lst[1]} 3) {alcohol_lst[2]} 4) {alcohol_lst[3]} 5) 아무거나 6) 계산 : ')
#     if alcohol == '6':
#         print('다음에 또 오세요')
#         break
#     elif alcohol == '1':
#         print(f'''맥주에 어울리는 안주는 {alcohol_foods['맥주']}''')
#     elif alcohol == '2':
#         print(f'''소주에 어울리는 안주는 {alcohol_foods['소주']}''')
#     elif alcohol == '3':
#         print(f'''와인에 어울리는 안주는 {alcohol_foods['와인']}''')
#     elif alcohol == '4':
#         print(f'''고량주에 어울리는 안주는 {alcohol_foods['고량주']}''')
#     elif alcohol == '5':
#         print(f'''{random.choice(alcohol_lst)}에 어울리는 안주는 {random.choice(food_lst)}''')
#     else:
#         print('메뉴에서 골라주세요')



    # tmp = int(alcohol) - 1
    # menu = alcohol_lst[tmp] if (0 <= tmp <= 3) else 0
    # if 0 <= tmp <= 4:
    #     if tmp == 4:
    #         print('다음에 또 오세요')
    #         break
    #     else:
    #         print(f'''{menu}에 어울리는 안주는 {alcohol_foods[menu]}입니다.''')
    # else:
    #     print('메뉴에서 골라주세요')

# alcohol_foods = dict(맥주= '치킨', 소주= '골뱅이', 위스키= '치즈', 고량주= '짬뽕')
# print(alcohol_foods)


# enumerate

food = ['A', 'B', 'C', 'D']
for i in enumerate(food):
    print(i)

# ** 사용 / *만 사용하면 key값만 나옴
first = {'a': 'agnoy', 'b': 'bills'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

# update (후의 값으로 덮어쓰기)
pythons = {
    'A': 1,
    'B': 2,
    'C': 3
}
others = {
    'C': 4,
    'D': 5
}
pythons.update(others)
print(pythons)

# 딕셔너리 비교
a = {1:1, 2:2, 3:3}
b = {1:1, 3:3, 2:2}
print(a==b)  # True
# print(a<=b)  # error

# 딕셔너리 컴프리헨션 가능

