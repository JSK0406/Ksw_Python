class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


lst = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]

if __name__ == "__main__":
    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    lst.append(node)

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        lst.append(node)

    print_nodes(head)
    print_nodes(lst[2])
    print(lst)