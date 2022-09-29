import sys
from collections import deque
from datetime import datetime

test = int(input())  # 테스트 케이스의 수
start_time = datetime.now()  # 시작 시간 저장
for i in range(test):
    m = int(input())  # 맵의 한 변의 길이

    mars_map = [[0 for i in range(m)] for i in range(m)]  # 원본 비용 배열
    mars_accumulate_map = [[0 for i in range(m)] for i in range(m)]  # 누적 비용 배열
    mars_visit_map = [[0 for i in range(m)] for i in range(m)]  # 첫 방문 배열(처음으로 방문된 배열인지 아닌지 기록)

    # 이동 비용 값 넣어주기
    for i in range(m):
        tmp = list(map(int, sys.stdin.readline().split()))
        mars_map[i] = [x for x in tmp]

    # 초기설정
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start = (0, 0)  # 시작노드
    mars_visit_map[0][0] = 1  # 시작노드는 첫 방문처리
    mars_accumulate_map[0][0] = mars_map[0][0]  # 시작 노드 비용 갱신

    q = deque()
    q.append(start)

    while (q):
        x, y = q.popleft()  # 현재 좌표
        now = mars_accumulate_map[y][x]  # 현재 노드까지 도닫하는데 걸린 최소비용

        for i in range(4):
            # 이동 좌표들
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 안에 잇는 좌표인지 확인
            if (0 <= nx < m and 0 <= ny < m):
                # 첫 방문일 경우
                if (mars_visit_map[ny][nx] == 0):
                    # 이동해서 온 경로가 유일하므로, 여기까지 도닫하는데 걸리 노드비용 무조건 계산
                    mars_accumulate_map[ny][nx] = mars_map[ny][nx] + now
                    mars_visit_map[ny][nx] = 1  # 현재 노드 첫 방문처리
                    q.append((nx, ny))
                else:
                    # 이동해서 온 경로가 유일하지 않으므로 어떤 경로가 최소 값인지 계산
                    old = mars_accumulate_map[ny][nx]  # 이전 경로로의 비용값
                    new = mars_map[ny][nx] + now  # 새로운 경로로의 비용값
                    if (old > new):
                        mars_accumulate_map[ny][nx] = new
                        q.append((nx, ny))

    print(mars_accumulate_map[m - 1][m - 1])

end_time = datetime.now()  # 시작 시간 저장
print(end_time - start_time)