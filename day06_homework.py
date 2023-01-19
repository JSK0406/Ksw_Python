# 9.3

def test(func):
    def inner():
        print('start')
        func()
        print('end')
    return inner


def running():
    print('실행됨')


tmp_func = test(running)
tmp_func()

# 9.4


class OopsException(Exception):
    pass

while True:
    try:
        tmp = input('a를 입력하세요: ')
        if tmp != 'a':
            raise OopsException('OopsException 발생')
        print('Caught an oops')
        break
    except OopsException as err:
        print(err)
