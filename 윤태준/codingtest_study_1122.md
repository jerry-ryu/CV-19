# 코테 스터디

백준

[https://www.acmicpc.net/problem/18428](https://www.acmicpc.net/problem/18428)

## 감시피하기

*N*x*N* 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.

각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.

다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자. 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다. 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다. 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다.

![image](https://user-images.githubusercontent.com/54363784/203216966-ecd6225e-7e13-4aae-b753-908784b4ca1d.png)

이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.

학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다. *N*x*N* 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.

예를 들어 *N*=5일 때, 다음과 같이 선생님 및 학생의 위치 정보가 주어졌다고 가정하자.

### 입력

첫째 줄에 자연수 *N*이 주어진다. (3 ≤ *N* ≤ 6) 둘째 줄에 *N*개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 *N*개의 원소가 공백을 기준으로 구분되어 주어진다. 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.

단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.

### 출력

첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다. 모든 학생들을 감시로부터 피하도록 할 수 있다면 `YES`, 그렇지 않다면 `NO`를 출력한다.

![image](https://user-images.githubusercontent.com/54363784/203217022-6a136915-1889-44ae-bc70-9b68ae2d7ce1.png)

### 문제 요약

선생님, 학생, 빈 공간의 좌표를 구할 수 있다.

선생님은 직선방향으로만 동서남북을 볼 수 있다.(십자가..?)

그런데 빈 공간 중 3개에 벽을 설치한다.

그러면 학생들 모두가 딴짓할 수 있는가?

### 풀이 전략

1. 빈공간 좌표 리스트를 만들고 combination 3개로 만들어서 다시 리스트에 넣어야겠다.→ combination
2. dfs써서 선생님 좌표로부터 동서남북 보는 함수를 만들어야겠다.→Dfs
3. 각 조합마다 학생들이 다 살아있는지..? 확인 →numofstudent

```python
import copy
import itertools

n = int(input())
graph = []
teacher = []
student = []
zero = []
for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append([i, j])
        if graph[i][j] == 'S':
            student.append([i, j])
        if graph[i][j] == 'X':
            zero.append([i, j])

numOfStudent = len(student)
cc = list(itertools.combinations(zero, 3))

# 학생수세는 함수
def countStudent(lst):
    count = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 'S':
                count += 1
    return count

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 선생님이 레이저 쏘는 함수
# d는 방향임 0이면 동 1이면 서.. 이런느낌
# 한 직선방향으로 graph_에서 'T'로 바꿔줌, 'O'면 멈춤
def dfs(i, j, d):
    graph_[i][j] = 'T'

    nx = i + dx[d]
    ny = j + dy[d]

    if 0 <= nx < n and 0 <= ny < n and graph_[nx][ny] != 'O':
        dfs(nx, ny, d)

    return

check = False
for c in cc:
		# deepcopy 유의하기
    graph_ = copy.deepcopy(graph)
		# 세군데다 벽쳐줌
    graph_[c[0][0]][c[0][1]] = 'O'
    graph_[c[1][0]][c[1][1]] = 'O'
    graph_[c[2][0]][c[2][1]] = 'O'
		
		# 선생님 좌표마다 dfs씀 
    for tx, ty in teacher:
        for direction in range(4):
            dfs(tx, ty, direction)
		# 레이저 쏘고 난 다음 학생수가 원래 학생수와 같으면 check true
    if countStudent(graph_) == numOfStudent:
        check = True

if check:
    print('YES')
else:
    print('NO')
```
