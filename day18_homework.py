from operator import itemgetter

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0]*size for _ in range(size)]

city_arr = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5

g = Graph(len(city_arr))

g.graph[서울][뉴욕] = 80; g.graph[서울][북경] = 10
g.graph[뉴욕][서울] = 80; g.graph[뉴욕][북경] = 40; g.graph[뉴욕][방콕] = 70
g.graph[런던][방콕] = 30; g.graph[런던][파리] = 60
g.graph[북경][서울] = 10; g.graph[북경][뉴욕] = 40; g.graph[북경][방콕] = 50
g.graph[방콕][뉴욕] = 70; g.graph[방콕][북경] = 50; g.graph[방콕][런던] = 30; g.graph[방콕][파리] = 20;
g.graph[파리][방콕] = 20; g.graph[파리][런던] = 60;

def print_graph(g):
    for i in range(g.size):
        print("%9s"%city_arr[i], end=' ')
    print('')
    for row in range(g.size):
        print(city_arr[row], end='')
        for col in range(g.size):
            print("%9d"%g.graph[row][col], end=' ')
        print('')

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
print_graph(g)

def find_vertex(g, findvtx):
    stack = [0]
    visited_list = [0]
    current = 0

    while stack:
        next = None
        for vertex in range(g.size):
            if g.graph[current][vertex] != 0:
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

    return True if findvtx in visited_list else False

edge_arr = []
for start in range(g.size):
    for end in range(g.size):
        if g.graph[start][end] != 0:
            edge_arr.append([g.graph[start][end], start, end])


edge_arr = sorted(edge_arr, key=itemgetter(0), reverse=False)

new_arr = []
for i in range(0, len(edge_arr), 2):
    new_arr.append(edge_arr[i])


idx = 0
while len(new_arr) > g.size-1:
    start = new_arr[idx][1]
    end = new_arr[idx][2]
    cost = new_arr[idx][0]

    g.graph[start][end] = 0
    g.graph[end][start] = 0

    if find_vertex(g, start) and find_vertex(g, end):
        del(new_arr[idx])
    else:
        g.graph[start][end] = cost
        g.graph[end][start] = cost
        idx += 1

print('')
print('## 가장 효율적인 해저 케이블 연결도 ##')
print_graph(g)