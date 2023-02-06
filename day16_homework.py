import random
import math

# ex) 05-01

class Node:
    def __init__(self, data):
        self.data = data
        self.name = data[0]
        self.next = None


if __name__ == "__main__":
    data_list = []
    for i in range(10):
        x, y = random.randint(1, 100), random.randint(1, 100)
        data_list.append((chr(i+65), x, y, math.sqrt(x*x+y*y)))

    head = None
    for i in range(10):
        if not head:
            node = Node(data_list[i])
            head = node
            node.next = head
            continue
        node = Node(data_list[i])
        pre = head
        current = head.next
        if node.data[3] < head.data[3]:
            node.next = head
            while current.next != head:
                current = current.next
            current.next = node
            head = node
            continue
        while current.data[3] <= node.data[3]:
            if current.next == head:
                pre = current
                current = current.next
                break
            pre = current
            current = current.next
        node.next = current
        pre.next = node


start = head
print('///// 1번 문제 /////')
for _ in range(10):
    print(start.name, "편의점, ", "거리: ", start.data[3])
    start = start.next

# ex) 05-02


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.pre = None


if __name__ == "__main__":
    data_lst = ['다현', '정연', '쯔위', '사나', '지효']
    node = Node(data_lst[0])
    head = node
    current = head
    for i in data_lst[1:]:
        node = Node(i)
        current.next = node
        node.pre = current
        current = node

    start = head
    print('///// 2번 문제 /////')
    print('정방향 --> ', end='')
    for _ in range(5):
        print(start.name, end=' ')
        if not start.next:
            break
        start = start.next

    print('')
    print('역방향 --> ', end='')
    for _ in range(5):
        print(start.name, end=' ')
        if start.pre == None:
            break
        start = start.pre
    print('')
# ex) 06-01

def is_stack_full():
    if top >= len(lst)-1:
        return True
    return False

def is_stack_empty():
    global stack, top
    if top <= -1:
        return True
    return False

def push(data):
    global stack, top
    top += 1
    stack[top] = data
    return data

def pop():
    global stack, top
    tmp = stack[top]
    stack[top] = None
    top -= 1
    return tmp

def peek():
    global stack, top
    if is_stack_empty():
        return None
    return stack[top]

if __name__ == "__main__":
    stack = [None] * 6
    top = -1
    lst = ['빨강', '파랑', '초록', '노랑', '보라', '주황']
    random.shuffle(lst)

    print('///// 3번 문제 /////')

    print("과자집에 가는길 : ", end='')
    for i in lst:
        print(push(i), "->", end=' ')
    print("과자집")

    print("우리집에 오는길 : ", end='')
    for _ in range(len(lst)):
        print(pop(), "->", end=' ')
    print("우리집")

# ex) 06-02


def is_stack_full():
    if top >= len(lst)-1:
        return True
    return False

def is_stack_empty():
    global stack, top
    if top <= -1:
        return True
    return False

def push(data):
    global stack, top
    top += 1
    stack[top] = data
    return data

def pop():
    global stack, top
    tmp = stack[top]
    stack[top] = None
    top -= 1
    return tmp

def peek():
    global stack, top
    if is_stack_empty():
        return None
    return stack[top]

if __name__ == "__main__":
    top = -1
    text_lst = "진달래꽃\n나 보기가 역겨워\n가실 때에는\n말없이 고이 보내드리오리다."
    stack = [None]*len(text_lst)
    print('///// 4번 문제 /////')
    print('----- 원본 -----')
    for i in text_lst:
        print(push(i), end='')
    print('')
    print('----- 거꾸로 처리된 결과 -----')
    for _ in range(len(text_lst)):
        print(pop(), end ='')