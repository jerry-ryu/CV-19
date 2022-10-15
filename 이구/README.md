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
```
3   
0 1 0   
0 0 1   
1 0 0
```
#### [ output ]
```
1 1 1   
1 1 1   
1 1 1   
```
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

## 3주차 - BOJ 1041. 주사위
> Source: https://www.acmicpc.net/problem/1041 

### 문제
```
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+ 
``` 
주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.

A, B, C, D, E, F에 쓰여 있는 수가 주어진다.

지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.

N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.
    
### 조건
#### 입력
첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.

#### 출력
첫째 줄에 문제의 정답을 출력한다.

### 입출력 예시
#### [ input ]
```
2
1 2 3 4 5 6
```
#### [ output ]
```
36
```
### 풀이

#### 1. input 받기

```python
n = int(input())
nums = list(map(int, input().split()))
```

#### 2. Case 분류
결국, 주사위를 쌓아서 만들게 된 정육면체를 구성하고 있는 주사위들은 최소 2면, 최대 5면(n=1 인 경우)을 보이게 된다. 각각의 경우, 주사위 눈금의 합이 최소가 되는 경우는 아래와 같다.

```python
def one_side():
    return min(nums)

def two_side():
    arr = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    arr = sorted(arr)
    return sum(arr[:2])

def three_side():
    arr = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    arr = sorted(arr)
    return sum(arr[:])

def five_side():
    return sum(nums) - max(nums)    
```

#### 3. Case 별 갯수 계산하기

##### 1. 3면을 보이는 경우 (n != 1 인 경우)
정육면체의 맨 위, 꼭짓점 4개   

##### 2. 2면을 보이는 경우 (n != 1 인 경우)
맨 윗줄의 가로 모서리: (n-2) * 4 개   
옆면의 나머지 세로 모서리: (n-1) * 4 개   

##### 3. 1면을 보이는 경우 (n != 1 인 경우)
맨 윗줄의 가운데 부분: (n-2) * (n-2) 개   
옆면의 나머지 세로 모서리를 제외한 전부: (n-1) * (n-2) * 4 개   

##### 4. 0면을 보이는 경우 (n != 1 인 경우) (문제 풀이와는 관련없지만, 전부 더했을 때 n**3이 나오는 걸 확인하기 위함)

바깥 면들로 둘러싸인 부분: (n-2) * (n-2) * (n-1) 개   
==> 1, 2, 3, 4를 다 더하면 n**3 이 나오는 걸 확인할 수 있다.

##### 5. 5면을 보이는 경우 (n = 1 인 경우)   
n = 1 일때, 항상 1개    

#### 4. Case 별 answer 계산 후 출력
```python
if n > 2:
    answer = 4 * three_side() + (8 * n - 12) * two_side() + ((n-2)**2 + 4*(n-1)*(n-2)) * one_side()
elif n == 2:
    answer = 4 * three_side() + 4 * two_side()
else:
    answer = five_side()

print(answer)
```

### 전체 코드
전체 코드는 [여기](https://github.com/99sphere/Problem-Solving/blob/main/Graph%20Traversal/BOJ_1041.py)서 확인할 수 있다.

