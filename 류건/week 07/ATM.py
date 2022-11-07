from itertools import accumulate

N = int(input())
l = list(map(int, input().split()))
l.sort() # 정렬

# 누적합 구하기
result = list(accumulate(l))
# 누적합의 합 구하기
print(sum(result))
