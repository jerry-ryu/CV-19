import heapq
from datetime import datetime
m = int(input())
start_time = datetime.now()  # 시작 시간 저장
for t in range(m):
    # 탐사 공간
    n = int(input())
    # 탐사 공간에 대한 비용
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 다익스트라를 위한 q
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    # 상하좌우 탐색을 위한 ds
    ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

    distance = [[1e9] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for d in ds:
            dx = x + d[0]
            dy = y + d[1]

            if 0 <= dx and dx < n and 0 <= dy and dy < n:
                cost = dist + graph[dx][dy]

                if cost < distance[dx][dy]:
                    distance[dx][dy] = cost
                    heapq.heappush(q, (cost, dx, dy))

    print(distance[n-1][n-1])
end_time = datetime.now()  # 시작 시간 저장
print(end_time - start_time)