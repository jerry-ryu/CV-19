import heapq
import collections
from datetime import datetime

m = int(input())
start_time = datetime.now()  # 시작 시간 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(m):
    n = int(input())
		# graph에는 각각의 칸을 지나기 위한 비용을 넣어줌 {(x, y): cost}
    graph = collections.defaultdict(int)
		# dist는 (0, 0)에서 특정좌표까지 도달할 때의 cost를 넣어줌 {(x, y): cost}
    dist = collections.defaultdict(int)
    for i in range(n):
        lst = list(map(int, input().split()))
        for j in range(n):
            graph[(i, j)] = lst[j]
    q = [(graph[(0, 0)], 0, 0)] # cost, x좌표, y좌표
    while q:
        cost, x, y = heapq.heappop(q)
        if (x, y) not in dist:
            dist[(x, y)] = cost
            for i in range(4):  # 갈 수 있는 경로를 다 찾아보기
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n: # 다음 노드가 가능한 노드인지 확인
                    tmp = graph[(nx, ny)] + cost   # 다음 노드에 해당하는 cost를 update
                    heapq.heappush(q, (tmp, nx, ny)) # q에 (updated cost, x좌표, y좌표)
    print(dist[(n - 1, n - 1)])
end_time = datetime.now()  # 시작 시간 저장
print(end_time - start_time)