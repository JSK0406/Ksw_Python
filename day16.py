import random


# 링크드리스트의 여러 기능 구현

class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != head:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:
        node = Node(insert_data)
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)  # 마지막 노드 삽입
    current.link = node
    node.link = head


def delete_node(delete_data):
    global pre, current, head

    if head.data == delete_data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return

    return


def find_node(find_data):
    global pre, head, current

    current = head

    if current.data == find_data:
        return current

    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            return current
    return Node(None)


def is_find(find_data):
    global pre, head, current

    current = head

    if current.data == find_data:
        return True

    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            return True
    return False

def count_odd_even():
    global head, current, pre

    # if head == None:
    #     return False

    current = head
    even, odd = 0, 0
    while True:
        if current.data % 2 == 0:
            even += 1
        else:
            odd += 1
        if current.link == head:
            break
        current = current.link
    return odd, even

def make_minus_number(odd, even):
    if odd > even:
        remainder = 1
    else:
        remainder = 0

    current = head
    while True:
        if current.data % 2 == remainder:
            current.data = current.data * -1

        if current.link == head:
            break
        current = current.link

# head, current, pre = None, None, None
# data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]
data_array = [random.randint(1, 100) for _ in range(7)]

if __name__ == "__main__":

    node = Node(data_array[0])  # 첫 번째 노드
    head = node
    head.link = head

    for data in data_array[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)

o, e = count_odd_even()
make_minus_number(o, e)
print("odd number : ", o, "even number", e)
print_nodes(head)


    # print_nodes(head)
    # delete_node("피카츄")
    # print_nodes(head)
    # print(find_node("꼬부기").data)
    # print(is_find("꼬부기"))
    # print(is_find("잠만보"))

    # insert_node("피카츄", "잠만보")
    #
    # print_nodes(head)
    # delete_node("잠만보")
    # print_nodes(head)
    # delete_node("이상해씨")
    # print_nodes(head)
    # delete_node("강찬석")
    # print_nodes(head)
    # print(find_node("피카츄").data)
    # print(find_node("피카츄"))
    # print(find_node("abc").data)
    #
    #
