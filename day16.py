# 링크드리스트의 여러 기능 구현

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.link = None
#
#
# def print_nodes(start):
#     current = start
#     if current == None:
#         return
#     print(current.data, end=' ')
#     while current.link != None:
#         current = current.link
#         print(current.data, end=' ')
#     print()
#
# def insert_node(find_data, insert_data):
#     global head, current, pre
#
#     if head.data == find_data:
#         node = Node(insert_data)
#         node.link = head
#         head = node
#         return
#
#     current = head
#     while current.link != None:  # 중간 노드 삽입
#         pre = current
#         current = current.link
#         if current.data == find_data:
#             node = Node(insert_data)
#             node.link = current
#             pre.link = node
#             return
#
#     node = Node(insert_data)  # 마지막 노드 삽입
#     current.link = node
#
# def delete_node(delete_data):
#     global pre, current, head
#
#     if head.data == delete_data:
#         current = head
#         head = head.link
#         del current
#         print("첫 노드가 삭제됨")
#         return
#
#     current = head
#     while current.link != None:
#         pre = current
#         current = current.link
#         if current.data == delete_data:
#             pre.link = current.link
#             del current
#             print("중간 노드가 삭제됨")
#             return
#
#     print("삭제된 노드 없음")
#     return
#
# def find_node(find_data):
#     global pre, head, current
#
#     current = head
#
#     if current.data == find_data:
#         return current
#
#     while current.link != None:
#         pre = current
#         current = current.link
#         if current.data == find_data:
#             return current
#     return Node(None)
#
# # head, current, pre = None, None, None
# data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]
# if __name__ == "__main__":
#
#     node = Node(data_array[0])  # 첫 번째 노드
#     head = node
#
#     for data in data_array[1:]:  # 두 번째 이후 노드
#         pre = node
#         node = Node(data)
#         pre.link = node
#
#     insert_node("피카츄", "잠만보")
#
#     print_nodes(head)
#     delete_node("잠만보")
#     print_nodes(head)
#     delete_node("이상해씨")
#     print_nodes(head)
#     delete_node("강찬석")
#     print_nodes(head)
#     print(find_node("피카츄").data)
#     print(find_node("피카츄"))
#     print(find_node("abc").data)

