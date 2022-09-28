# 코테 스터디
## 1주차

### 문제 (https://www.acmicpc.net/problem/11055)
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

### 풀이
```python
n = int(input())
a = list(map(int, input().split()))
       
dp = a[:]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))
```

### 해설
dp 테이블은 a를 deepcopy해서 초기화
-> 자기보다 앞에 있는 모든 수가 자기보다 큰 경우로 시작

이후, 아래 과정 반복
 | a | 1 | 100 | 2 | 50 | 60 | 3 | 5 | 6 | 7 | 8 |
 |---|---|----|----|----|----|---|---|---|---|---|
|1| i  |     |   |    |    |   |   |   |   |   |
|2| j   |  i   |   |    |    |   |   |   |   |   |
|3| j  |     | i  |    |    |   |   |   |   |   | 
|4|     |  j   | i  |    |    |   |   |   |   |   |
|5| j    |     |   | i   |    |   |   |   |   |   |
|6|     |    j |   |  i  |    |   |   |   |   |   |
|7|     |     | j  |   i |    |   |   |   |   |   |


 | dp | 1 | 100 | 2 | 50 | 60 | 3 | 5 | 6 | 7 | 8 |
 |---|---|----|----|----|----|---|---|---|---|---|
|1| 1 | 100 | 2 | 50 | 60 | 3 | 5 | 6 | 7 | 8 |
|2|  1  |  101   | 2 | 50 | 60 | 3 | 5 | 6 | 7 | 8 |
|3| 1  |  101   | 3  | 50 | 60 | 3 | 5 | 6 | 7 | 8 | 
|4| 1  |  101   | 3  | 50 | 60 | 3 | 5 | 6 | 7 | 8 |
|5| 1  |  101   | 3  |  53  | 60 | 3 | 5 | 6 | 7 | 8 |
|6|     |    j |   |  i  |    |   |   |   |   |   |
|7|     |     | j  |   i |    |   |   |   |   |   |

## 2주차 - BOJ 11403. 경로찾기
> Source: https://www.acmicpc.net/problem/11403 

### 문제
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

### 조건
#### 입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

#### 출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

### 입출력 예시
#### [ input ]
3   
0 1 0   
0 0 1   
1 0 0    
#### [ output ]
1 1 1   
1 1 1   
1 1 1   

### 풀이
전형적인 그래프 탐색 문제이고, 나는 BFS를 이용하여 해결했다. 문제를 보면, adjacency matrix 형식의 그래프를 input으로 받는다. 

#### 1. input 받기

```python
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

```

#### 2. 문제 해결
시작 노드와 종료 노드를 선택한 후, bfs를 통해 시작 노드에서 종료 노드까지 경로가 존재하는지를 확인한다. 조금 특별한 점이 있다면, cycle이 생기는 경우(시작 노드와 종료 노드가 같은 경우)도 판단해야 하기에 bfs를 시작하는 노드에는 visitd를 체크하지 않는다.

```python
def bfs(start, end):
    visited = [False] * n
    queue = deque()
    queue.append(start)
    #visited[start] = True

    while queue:
        current = queue.popleft()
        for idx, val in enumerate(graph[current]):
            if val and visited[idx]==False:
                queue.append(idx)
                visited[idx] = True

                if idx == end:
                    return "1"

    return "0"

for i in range(n):
    for j in range(n):
        answer[i][j] = bfs(i, j)
```

#### 3. 출력 형식 맞추기
```python
for ans in answer:
    print(" ".join(ans))
```

### 전체 코드
전체 코드는 [여기](https://github.com/99sphere/Problem-Solving/blob/main/Graph%20Traversal/BOJ_11403.py)서 확인할 수 있다.

