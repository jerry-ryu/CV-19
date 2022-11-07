N, K = map(int, input().split())
# 동전 가져오기
l = []
for i in range(N):
    l.append(int(input()))
l.sort(reverse = True) # 정렬
total = 0

# 큰거부터 나누기
for i in l:
    if i <= K:
        total += (K // i)
        K -= (K // i) * i

print(total)