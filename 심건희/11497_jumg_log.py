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
    


# 양 옆에 인접한 것들끼리 서로 가까운 것들로 위치해야함
# 원형. 마지막 idx와 두번째 건 각각 세, 두번째로 작은 거로 위치할 것
# 인접해서 높이 차가 가장 작은 건, (내림/오름)높이가 정렬되었을 때 인접한 두 높이
# 따라서 수를 정렬해서, 최소(최대도 됨, 여기선 최소)값을 기준 높이로 두고,
# 기준 높이의 양옆에 설치할 통나무 높이들을 정렬순으로 차례대로 배정