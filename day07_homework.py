# 10.1
class Thing:
    pass

example = Thing()
print(Thing == example)

# 10.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)

# 10.3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


example = Thing3()
print(example.letters)

# 10.4

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        return (self.name, self.symbol, self.number)

    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'
Hydrogen1 = Element('Hydrogen', 'H', 1)
print(Hydrogen1.name, Hydrogen1.symbol, Hydrogen1.number)

# 10.5

el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
Hydrogen2 = Element(**el_dict)
print(Hydrogen2.name, Hydrogen2.symbol, Hydrogen2.number)

# 10.6

Hydrogen3 = Element('Hydrogen', 'H', 1)
print(*Hydrogen3.dump())

# 10.7

Hydrogen4 = Element('Hydrogen', 'H', 1)
print(Hydrogen4)

# 10.8

class Element:
    def __init__(self, na, sy, nu):
        self.__name = na
        self.__symbol = sy
        self.__number = nu

    @property
    def dump(self):
        print('inside the getter')
        return f'{self.__name} {self.__symbol} {self.__number}'

    @dump.setter
    def dump(self, na, sy, nu):
        print('inside the setter')
        self.__name = na
        self.__symbol = sy
        self.__number = nu


example = Element('네임', '심볼', '넘버')
print(example.dump)

# 10.9

class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

ex_be = Bear()
ex_ra = Rabbit()
ex_oc = Octothorpe()
print(ex_be.eats(), ex_ra.eats(), ex_oc.eats())

# 10.10

class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'


# class Robot(Laser, Claw, SmartPhone):
#     def __init__(self):
#         self.laser_dose = Laser.does()
#         self.claw_dose = Claw.does()
#         self.smart_does = SmartPhone.does()
#
#     def does(self):
#         return f'{self.laser_does} {self.claw_does} {self.smart_does}'



ex_la = Laser()
ex_cl = Claw()
ex_sm = SmartPhone()

class Robot():
    def __init__(self, ex_la, ex_cl, ex_sm):
        self.laser_dose = _ex_la.does()
        self.claw_dose = _ex_cl.does()
        self.smart_does = _ex_sm.does()

    def does(self):
        return f'{self.laser_dose} {self.claw_dose} {self.smart_does}'

ex_ro = Robot(ex_la, ex_cl, ex_sm)
print(ex_ro.does())

