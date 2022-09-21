import sys


t = int(sys.stdin.readline())
for _ in range(t) :
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))  # 통나무 높이
    l.sort()
    # 홀수번째를 기준의 왼쪽에, 짝수번째(2~)를 기준의 오른쪽에
    level = max(l[1] - l[0], l[2] - l[0])
    for i in range(3, n) :
        level = max(level, l[i] - l[i-2])
    level = max(level, abs(l[n-1] - l[n-2]))# 원형 배치이므로
    print(level)
