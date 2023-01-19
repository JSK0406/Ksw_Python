# Class


# class Cat:
#     def __init__(self):
#
#     pass
#
#
# a_cat = Cat()
# another_cat = Cat()
#
# a_cat.age = 3
# print(a_cat.age)

class pokemon:
    def __init__(self, name, owner, skills):  # 개체 생성 시 동작
        print(f'포켓몬 {name} 생성됨')
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')


    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill)


class pikachu(pokemon):
    pass


p1 = pokemon('피카츄', '한지우', '50만 볼트/100만볼트/번개')
p2 = pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
pi1 = pikachu('피카츄', '한지우', '50만 볼트/100만볼트/번개')
pi1.info()
