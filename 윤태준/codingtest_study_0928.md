# 플로이드 워셜 알고리즘

다익스트라 알고리즘은 ‘한 지점에서 다른 특정 지점까지의 최단 경로를 구행 하는 경우’에 사용할 수 있는 최단 경로 알고리즘이다. 이번에 설명하는 **플로이드 워셜 알고리즘**은 ‘모든 지점에서 다른 모든 지점까지의 최단 경로를 모든 구해야 하는 경우’에 사용할 수 있는 알고리즘이다.

```python
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
```

```python
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
```

# 미래도시 
[문제]
미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.

 

방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.

 

미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.

 

또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어

 

있다면, 정확히 1만큼의 시간으로 이동할 수 있다.

 

또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다.

 

방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정이다.

 

따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다.

 

이때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다. 

 

방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.




```python
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range (n + 1)]

for k in range(1, n + 1):
    graph[k][k] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

x, k = map(int, input().split())
distance = graph[1][k] + graph[k][x]
print(distance)

'''
<입력 예시 1>
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
<출력 예시 1>
3

<입력 예시 2>
4 2
1 3
2 4
3 4
<출력 예시 2>
-1
'''

```
