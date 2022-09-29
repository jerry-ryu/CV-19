import sys
a,b = map(int, sys.stdin.readline().rstrip().split()) # 세로, 가로
l = list(map(int, sys.stdin.readline().rstrip().split())) # 기둥 리스트

water = 0 # 빗물 개수

# 빗물 세기
# m은 채워지는 물높이
def water_cal(m, tmp):
    total = 0
    if tmp:
        for i in tmp:
            total = total + m - i

    return total

def solution(b, l):
    idx = 0
    stan = l[idx] # 기준 기둥
    tmp = [] # 기준 기둥보다 작은 경우 tmp에 넣는다
    water = 0 # 채워진 물의 개수


    while (idx != b):
        idx = idx + 1 # idx를 한칸씩 증가시키면서 비교


        if (idx == b):
            # 인덱스를 끝까지 갔는데, 기준 기둥보다 크거나 같은 경우가 안나온 경우
            if tmp:
                stan = max(tmp) # 나머지 배열의 최댓값을 물의 높이로 잡고
                max_idx = tmp.index(stan)
                water += water_cal(stan, tmp[:max_idx]) # 최댓값기둥 이전의 배열은 물높이를 최대값으로 하여 물을 세준다
                last = tmp[max_idx:] # 최대값 이후의 배열은 작은 문제로 정의하고 solution에 넣어준다
                water += solution(len(last), last)
            continue

        # 기준 기둥보다 작은 경우 tmp에 넣기
        if (stan > l[idx]):
            tmp.append(l[idx])
        # 기준 기둥보다 크거나 같은 경우
        else:
            water += water_cal(stan, tmp) # 여기까지 물의 개수를 세주고
            stan = l[idx] # 기준 기둥보다 크거나 같은 경우를 새로운 기준 기둥으로 삼는다
            tmp = [] # 배열 초기화

    return water

print(solution(b,l)) # 채워지는 물의 개수 세기

