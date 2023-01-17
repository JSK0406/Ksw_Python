import copy

a = (100,)
b = (7,9,2)

print(a == b)
print(a <= b)  # 1번째 원소부터 나아가면서 이 부등호가 성립하는 순간 값 출력(1번째에서 결과가 나오면 멈춤)
print(a < b)  # 같은 게 나오면 무시하고 다음 인덱스로 진행, 문자의 사전처럼 순서를 따지기 위해서 -> 등호일 때 안 멈춤

# 문자열을 리스트로 만들면
lst1 = list('cat')
print(lst1)

# 튜플 수정
scores = ("B+", "A+", "C+")
print(scores)
# scores[1] = "B+" (X)
# scores[2] = "A+" (X)
tmp = list(scores)
tmp[1], tmp[2] = "C+", "A+"
scores = tuple(tmp)
print(scores)

# split
day = '9/19/2019'
print(list(day.split('/')))

# list slice
marxes = ["Groucho", "Chico", "Harpo"]
# print(marxes[4]) 이거는 안됨
print(marxes[4:])  #  이거는 됨

big_bang = ["GD", "태양", "탑", "대성", "승리"]
exo = ["백현", "첸"]
# big_bang.append("인하")
big_bang.insert(1, "인하")
print(big_bang)
# print(big_bang * 2)
# exo.extend(big_bang) #  extend는 기존 exo라는 변수에 big_bang을 연장, +는 새로운 변수에 더한 리스트를 할당
print(exo)

# A = [1,2,3]
# B = [4,5,6]
# print(id(A))  같다
# A.extend(B)
# print(id(A))  같다

A = [1,2,3]
B = [4,5,6]
print(id(A))
A = A + B
print(id(A))

# A += B는 같은 id주소(A에 B를 더하기), A = A + B(A와 B를 더해서 A에 할당)는 다른 id주소

# 요소 삭제 방법
lst = ["A", "B", [1, 2, 3, 4]]
lst[-1].pop()
print(lst)  # ['A', 'B', [1, 2, 3]]
lst[-1].pop(0)  # pop에 인덱싱 번호를 추가하여 그 자리의 요소를 빼낼 수 있다.
print(lst)  # ['A', 'B', [2, 3]]
del lst[2][-1]
print(lst)  # ['A', 'B', [3]]
# lst.remove(3)  3은 리스트 안에 들어있어서 삭제 안 됨
# lst[-1].remove(3)
print(lst)

# clear
lst.clear()
print(lst)

# 정렬
lst = ['G', 'A', 'F', 'Z']
# lst.sort()  # 원본 자체가 바뀜
new = sorted(lst)  # 정렬된 리스트를 리턴
print(lst)
print(new)

primes = [2, 19, 3.0, 5, 7, 11]
primes_sorted = sorted(primes)
print(primes)
print(primes_sorted)
primes = [2, 19, 3.0, 5, 7, 11]
primes.sort()
print(primes)

# mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']  # error
# mixed.sort()

mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']  # 숫자 - 영어 대문자 - 영어 소문자 - 한글
mixed.sort(reverse=True)
print(mixed)

# shallow copy
primes = [2, 19, 3, 5, 7, 11]
primes_cp = primes
print(primes)
print(primes_cp)
primes[-1] = 'lunch time'
print(primes)
print(primes_cp)
primes_cp[0] = 'morning coffee'
print(primes)
print(primes_cp)

# immutable일 때만 shallow copy 가능
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[2] = 'sw'
print(a, b, c, d)

# mmutable인 리스트가 요소일 때 -> 완전한 deep copy가 될 수 없다. / 공간을 save하면서 copy의 효과를 낼 수 있다.
a = [1, 2, [3, 4, 5]]
b = a.copy()
c = list(a)
d = a[:]
a[-1][0] = 6
print(a, b, c, d)

# ??
a = [1, 2, [3, 4, 5]]
b = a.copy()
c = list(a)
d = a[:]
a[-1] = [6]
print(a, b, c, d)

# deepcopy
a = [1, 2, [3, 4, 5]]
b = a.copy()
c = list(a)
d = a[:]
e = copy.deepcopy(a)
a[-1][0] = 6
print(a, b, c, d, e)

# zip
lst1 = ['A', 'B', 'C']
lst2 = [1, 2, 3]
new_lst = list(zip(lst1, lst2))
new_dict = dict(zip(lst1, lst2))
print(new_lst)
print(new_dict)

# list_comprehension
num_lst = [i-1 for i in range(1,6)]
print(num_lst)
a_lst = [i for i in range(1, 6) if i % 2 == 1]
print(a_lst)

# double_comprehension
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
print(cells)
for (row, col) in cells:  # unpacking
    print(row, col)