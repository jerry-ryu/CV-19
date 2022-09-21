# 코테스터디 (9/21 수)

오늘 공유할문제: 화성탐사(다익스트라) 

-이것이 취업을 위한 코딩테스트다(나동빈)

### 다익스트라 기본 코드

```python
import collections
import heapq

n, m = map(int, input().split())
start = int(input())
graph = collections.defaultdict(list)
dist = collections.defaultdict(int)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

Q = []
heapq.heappush(Q, (0, start))
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:  #갈 수 있는 경로를 다 찾아보기
            alt = time + w   # 다음 node에 해당하는 time을 update
            heapq.heappush(Q, (alt, v)). # Q에 (updated time, 다음 node)
print(dist)
''' 
input
6 11 (node, edge)
1 (start)
1 2 2 (start node, linked node, time)
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
```

## 다익스트라 기본풀이 개념

graph(dict)는 {한노드:[연결된노드들], 한노드:[연결된노드들]…}

dist(dict)는 {한노드:출발지로부터의 거리}

### 화성탐사

```python
import heapq
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
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
```
