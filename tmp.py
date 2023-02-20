import sys
import heapq

N = int(sys.stdin.readline())

hq = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        pass
        try:
            heapq.heappop(hq)
            print(hq)
        except:
            print(0)
    else:
        heapq.heappush(hq, (abs(num), num))
    print(hq)