[문제 바로가기](https://www.acmicpc.net/problem/11497)

### ✏ 생각하기
문제에서 구하는 것은 주어진 통나무들로 만들 수 있는 ```최소 난이도```다.  
난이도는 인접한 두 통나무 간의 높이 차의 최댓값으로 결정되므로, 이를 최소로 만들면 된다.  
높이 차가 최대인 인접한 두 통나무를 a, b라 하자. a, b의 높이 차가 최소가 되는 경우는, 통나무들을 높이를 기준으로 정렬(오름/내림)했을 때 인접한 두 통나무가 각각 a, b일 때다. 그렇지 않을 경우 a, b의 높이 차가 최소가 되는 경우가 아니게 된다. 즉, 가능한 최소 난이도가 아니게 된다.

### 📒 알고리즘
1. 통나무 높이 ```l```을 오름(내림)차순으로 정렬한다.
2. 최소(최대)값 ```l[0]```을 기준 통나무로 설정, 좌우에 정렬된 순으로 통나무를 배치해나간다고 생각하며, 인접한 높이차를 구해 난이도 ```level```을 갱신해준다.
3. 마지막으로 좌우 끝의 통나무 ```l[n-1]```, ```l[n-2]```의 높이 차를 구해 난이도를 갱신해준다.  
⚠ 통나무들이 원형으로 배치됨에 주의!  
![](https://velog.velcdn.com/images/goodheart50/post/870b29f4-48c1-42ee-ba4a-54434554665d/image.png)


### 💻 코드
```python
import sys


t = int(sys.stdin.readline())
for _ in range(t) :
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    # 홀수idx를 기준 l[0]의 왼쪽에, 짝수idx(>=2)를 기준의 오른쪽에
    level = max(l[1] - l[0], l[2] - l[0])
    for i in range(3, n) :
        level = max(level, l[i] - l[i-2])
    level = max(level, abs(l[n-1] - l[n-2]))  # 원형 배치이므로
    print(level)
```
