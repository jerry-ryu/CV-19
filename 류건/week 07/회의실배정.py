N = int(input())

# 회의 시간 받아오기
l = []
for i in range(N):
    tmp = list(map(int, input().split()))
    l.append(tmp)
# 회의시간 끝나는 시간 기준으로 정렬(끝나는 시간이 빠른게 먼저, 같을 경우 시작시간이 빠른게 먼저) (33,23,13)
l.sort(key = lambda x: (x[1], x[0]))

start = -1
cnt = 0

for i in l:
    if i[0] >= start: # 끝나는 시간이 시작하는 시간이랑 같으면 시작가능
        start = i[1]
        cnt += 1
print(cnt)