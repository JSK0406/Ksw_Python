# 09-01

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0]*size for _ in range(size)]

store_arr = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
g = Graph(len(store_arr))

g.graph[GS25][CU] = 1; g.graph[GS25][Seven11] = 1
g.graph[CU][GS25] = 1; g.graph[CU][Seven11] = 1; g.graph[CU][MiniStop] = 1
g.graph[Seven11][GS25] = 1; g.graph[Seven11][CU] = 1; g.graph[Seven11][MiniStop] = 1
g.graph[MiniStop][Seven11] = 1; g.graph[MiniStop][CU] = 1; g.graph[MiniStop][Emart24] = 1
g.graph[Emart24][MiniStop] = 1

def print_graph(g):
    print('## 편의점 그래프 ##')
    print('%9s'%'', end='')
    for i in range(g.size):
        print("%9s"%store_arr[i][0], end=' ')
    print('')
    for row in range(g.size):
        print("%9s"%store_arr[row][0], end=' ')
        for col in range(g.size):
            print("%9d"%g.graph[row][col], end=' ')
        print('')

stack = [0]
visited_list = []
current = 0
max_value = store_arr[0][1]

while stack:
    next = None
    for vertex in range(g.size):
        if g.graph[current][vertex] == 1:
            if vertex in visited_list:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visited_list.append(current)
    else:
        current = stack.pop()
    max_value = store_arr[current][1] if max_value < store_arr[current][1] else max_value

print_graph(g)

for i in store_arr:
    if i[1] == max_value:
        print('허니버터칩 최대 보유 편의점(개수) -->', i[0], max_value)
