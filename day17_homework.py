import random

# 07-01

print('------ 07-01 ------')


class Que:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = -1
        self.rear = -1

    def is_que_empty(self):
        return True if self.front == self.rear else False

    def is_que_full(self):
        return True if self.front == -1 and self.rear == self.size - 1 else False

    def en_que(self, data):
        if not self.is_que_full():
            self.rear += 1
            self.q[self.rear] = data
        else:
            print('que is full')

    def de_que(self):
        if not self.is_que_empty():
            self.front += 1
            print(self.q[self.front], "님 식당에 들어감")
            self.q[self.front] = None
            for i in range(self.front, self.rear):
                self.q[i] = self.q[i + 1]
            self.q[self.rear] = None
            self.front -= 1
            self.rear -= 1

    def check_que(self):
        print("대기 줄 상태 : ", que.q)
        return None


que = Que(5)

que.en_que('정국')
que.en_que('뷔')
que.en_que('지민')
que.en_que('진')
que.en_que('슈가')

for _ in range(5):
    que.check_que()
    que.de_que()
if que.is_que_empty():
    que.check_que()
    print('식당 영업 종료!')

# 07-02

print('------ 07-02 ------')


class CirQue:
    def __init__(self, size):
        self.q = [None] * size
        self.front = 0
        self.rear = 0
        self.waiting_time = 0
        self.size = size

    def is_que_empty(self):
        return True if self.front == self.rear else False

    def is_que_full(self):
        return True if (self.rear + 1) % self.size == self.front else False

    def en_que(self, why_call, time):
        if not self.is_que_full():
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = (why_call, time)
            self.waiting_time += time
            return
        print('que is full')

    def de_que(self):
        if not self.is_que_empty():
            self.front = (self.front + 1) % n
            self.q[self.front] = None
            return
        print('que is empty')

    def check_status(self):
        print(f'귀하의 대기 예상시간은 {self.waiting_time} 분입니다.')
        print('현재 대기 콜 -->', self.q)
        print('')
        return


que = CirQue(6)
que.check_status()
que.en_que('사용', 9)
que.check_status()
que.en_que('고장', 3)
que.check_status()
que.en_que('환불', 4)
que.check_status()
que.en_que('환불', 4)
que.check_status()
que.en_que('고장', 3)
print('최종 대기 콜 -->', que.q, '\n프로그램 종료!')

# 08-01

print('------ 08-01 ------')


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        current = self.root

        while True:
            if node.data == current.data:
                return
            if node.data < current.data:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
                continue

            if node.data > current.data:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
                continue

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)


test = BinaryTree()
data_arr = ['바나나맛우유', '레쓰비캔커피', '추파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_arr = []

for _ in range(20):
    sell_arr.append(tmp := random.choice(data_arr))
    test.add_node(tmp)

print('오늘 판매된 물건(중복O) -->', *sell_arr)

print('\n이진 탐색 트리 구성 완료!\n')
print('판매된 종류(중복X)-->', end=' ')
test.preorder(test.root)
