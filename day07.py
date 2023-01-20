import math

# class_inheritance

# class_method_override
# class Pokemon:
#     def __init__(self, owner, skills):
#         print(f"포켓몬 생성 :", end='')
#         self.owner = owner
#         self.skills = skills.split('/')
#
#     def info(self):
#         print(f"{self.owner}의 포켓몬이 사용가능한 스킬은{self.skills}입니다.")
#         for skill in self.skills:
#             print(skill)
#
#     def attack(self, idx):
#         print(f'{self.skills[idx]} 공격 시전')
#
#
#
# class Pikachu(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(전기) 시전')
#
# class Ggo(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(물) 시전')
#
# pk1 = Pikachu('한지우','몸톧박치기/번개')
# pk1.attack(1)
#
# ggo1 = Ggo('덴트', '몸통박치기/물대포')
# ggo1.attack(0)


# multiple_inheritance

# class Animal:
#     def says(self):
#         return 'I speak!'
#
# class Horse(Animal):
#     def says(self):
#         return 'Neigh!'
#
# class Donkey(Animal):
#     def says(self):
#         return 'Hee-haw'
#
# class Mule(Horse, Donkey):
#     pass
#
# m1 = Mule()
# print(m1.says())


# example

# class Pokemon:
#     def __init__(self, owner, skills):
#         print(f"포켓몬 생성 :", end='')
#         self.owner = owner
#         self.skills = skills.split('/')
#
#     def info(self):
#         print(f"{self.owner}의 포켓몬이 사용가능한 스킬은{self.skills}입니다.")
#         for i in range(len(self.skills)):
#             print(f'{i+1} : {self.skills[i]}')
#
#     def attack(self, idx):
#         print(f'{self.skills[idx]} 공격 시전')
#
#
#
# class Pikachu(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(전기) 시전')
#
# class Ggo(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(물) 시전')
#
# class Pairi(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "파이리"
#         print(f"{self.name}")
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(불) 시전')
#
# while True:
#     menu = input('1) 포켓몬 생성  2) 프로그램 종료 : ')
#     if menu == '2':
#         print('프로그램을 종료합니다.')
#         break
#     elif menu == '1':
#         pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리 : ')
#         if pokemon == '1':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
#             p = Pikachu(n, s)
#         if pokemon == '2':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
#             p = Pikachu(n, s)
#         if pokemon == '3':
#             n = input('플레이어 이름 입력 : ')
#             s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
#             p = Pikachu(n, s)
#         else:
#             print('메뉴에서 골라 주세요.')
#         info_attack = input('1) 정보 조회  2) 공격 : ')
#         if info_attack == '1':
#             p.info()
#         elif info_attack == '2':
#             p.info()
#             attack_menu = input('공격 번호 선택 : ')
#             p.attack(int(attack_menu) - 1)
#         else:
#             print('메뉴에서 골라주세요')
#     else:
#         print('메뉴에서 골라 주세요.')

# class PrettyMixin():
#     def time_print(self):
#         import datetime
#         print(datetime.date.today())
#     def dump(self):
#         import pprint
#         pprint.pprint(vars(self))
#
#
# class Thing(PrettyMixin):
#     pass
#
# t = Thing()
# t.name = "Nyarlathotep"
# t.feature = "ichor"
# t.age = "eldritch"
# t.gender = 'female'
# t.gender = 'male'
# t.dump()
# t.time_print()


# property

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('insdie the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
#
#
# don = Duck('Donald')
# don.name = 'donna'
# print(don.name)

# class Circle():
#     def __init__(self), radius:
#         self.radius = radius


# class Duck():
#     def __init__(self, input_name):
#         self.__name = input_name
#     def get_name(self):
#         print('insdie the getter')
#         return self.__name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.__name = input_name
#     name = property(get_name, set_name)
#
#
# don = Duck('Donald')
# print(don.name)
# don.name = '김인하'
# print(don.name)

# attribute of class
# class Fruit:
#     color = 'red'
#
# blueberry = Fruit()

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    def get_name(self):
        print('insdie the getter')
        return self.__name
    def set_name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    name = property(get_name, set_name)
    color = 'white'

don = Duck('Donald')
print(don.color)
don.color = 'blue'
print(don.color)
print(Duck.color)

# class method / 클래스의 객체들이 공유하고 있는 변수를 class method에

# class A():
#     count = 0
#     def __init__(self):
#         A.count += 1
#     def exclaim(self):
#         print("I'm an A!")
#     @classmethod
#     def kids(cls):
#         print(cls.count, "objects")

# polymorphism

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다.')

    def __add__(self, other, the_other):
        return self.get_area() + other.get_area() + the_other.get_area()

    def __repr__(self):
        return f'{self.__class__.__name__}의 좌표는 {self.x}, {self.y} 넓이는 {self.get_area()}입니다.'

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    # def __add__(self, other ):
    #     return (self.width + other.width) * (self.height + other.height)

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self.height = h

    def get_volume(self):
        return super().get_area()*self.height

c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(0, 0, 20, 50)
cy1 = Cylinder(0, 0, 5.0, 5.0)

print(r1 + r2 + c1)
