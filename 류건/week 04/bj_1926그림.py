import sys
from collections import deque
from collections import Counter
n, m = map(int,sys.stdin.readline().split())

l = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)] # 지도 그리기

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
level = 2 # 그림 번호

# 맵을 돌면서
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            l[i][j] = level
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                for r in range(4):
                    nx = x + dx[r]
                    ny = y + dy[r]
                    if 0 <= nx < m and 0 <= ny < n and l[ny][nx] == 1:
                        l[ny][nx] = level # 그림 라벨링
                        q.append((ny, nx))
            level += 1 # 그림 라벨링이 끝나면 그림번호 +1

# Counter로 단지 개수 세기
C = Counter([])
for i in range(n):
    C += Counter(l[i])

# 0번 단지가 있다면
if(0 in C):
    C.pop(0) # 0번 단지는 아파트가 없는곳이므로 삭제
print(len(C)) # 그림 개수 출력

# 그림이 있으면 가장 넓은 그림 넓이 출력
if C:
    # Counter에는 sort가 없어서 리스트로 만들어서 정렬 출력
    tmp = []
    for i in C.values():
        tmp.append(i)

    print(sorted(tmp, reverse = True)[0])

# 그림이 없으면 0출력
else:
    print(0)