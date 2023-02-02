
# class_inheritance
#
# class_method_override
class Pokemon:
    def __init__(self, owner, skills):
        print(f"포켓몬 생성 :", end='')
        self.hidden_owner = owner
        self.skills = skills.split('/')

    def get_owner(self):
        return self.hidden_owner

    def set_owner(self, owner):
        self.hidden_owner = owner

    def info(self):
        print(f"{self.owner()}의 포켓몬이 사용가능한 스킬은{self.skills}입니다.")
        for skill in self.skills:
            print(skill)

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전')

    owner = property(get_owner, set_owner)


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(전기) 시전')


class Ggo(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(물) 시전')


pk1 = Pikachu('한지우','몸톧박치기/번개')
pk1.attack(1)

ggo1 = Ggo('덴트', '몸통박치기/물대포')
ggo1.attack(0)


# multiple_inheritance

class Animal:
    def says(self):
        return 'I speak!'


# example

class Pokemon:
    def __init__(self, owner, skills):
        print(f"포켓몬 생성 :", end='')
        self.owner = owner
        self.skills = skills.split('/')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용가능한 스킬은{self.skills}입니다.")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전')


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(전기) 시전')

class Ggo(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(물) 시전')

class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}의 {self.skills[idx]} 공격(불) 시전')

while True:
    menu = input('1) 포켓몬 생성  2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리 : ')
        if pokemon == '1':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
            p = Pikachu(n, s)
        if pokemon == '2':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
            p = Pikachu(n, s)
        if pokemon == '3':
            n = input('플레이어 이름 입력 : ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력)')
            p = Pikachu(n, s)
        else:
            print('메뉴에서 골라 주세요.')
        info_attack = input('1) 정보 조회  2) 공격 : ')
        if info_attack == '1':
            p.info()
        elif info_attack == '2':
            p.info()
            attack_menu = input('공격 번호 선택 : ')
            p.attack(int(attack_menu) - 1)
        else:
            print('메뉴에서 골라주세요')
    else:
        print('메뉴에서 골라 주세요.')