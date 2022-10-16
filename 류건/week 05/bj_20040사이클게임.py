import sys

sys.setrecursionlimit(10 ** 6)

m, n = map(int, sys.stdin.readline().split())

p = [i for i in range(m)]


def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True # 사이클 생기면 true

    # 아니면 작은 쪽으로 union
    elif x > y:
        p[x] = y
        return False
    else:
        p[y] = x
        return False


flag = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if flag != 0: # 한번이라도 사이클이 생기면 입력만 받고 바로 넘김
        continue

    if union(a, b): # 사이클이 생기면 flag 변경
        flag = i + 1

if flag == 0:  # 사이클 x => 0출력
    print(0)
else:
    print(flag) # 사이클 O => 사이클 생긴 지점 출력


### Union by Rank 는 아래와 같이 구현할 수 있습니다.
### 항상 작은 값 기준으로 혹은 항상 큰 값 기준으로 합치도록 하면, 트리의 높이가 낮아져서 시간이 빨라지는 효과가 있습니다.