a = 'harry',
b = ('harry',)
c = ()
d = 'harry', 'ron'  # packing
e = ("hermione")  # string
f = ('harry', 'ron')  # packing
g = ("hermione",)  # packing
new = f + g
print(type(a))
print(type(e))
print(f[1])
x, y = f  # unpacking
print(x, y)
print(new)

a = (7,9,11)
b = (7,9,2)

print(a == b)
print(a <= b)  # 1번째 원소부터 나아가면서 이 부등호가 성립하는 순간 값 출력(1번째에서 결과가 나오면 멈춤)
print(a < b)  # 같은 게 나오면 무시하고 다음 인덱스로 진행, 문자의 사전처럼 순서를 따지기 위해서 -> 등호일 때 안 멈춤

f = ('harry', 'ron')  # packing
g = ("hermione",)  # packing
print(id(f))
f += g  # f는 기존의 f가 아닌 새로운 id값을 갖는다.
print(id(f))