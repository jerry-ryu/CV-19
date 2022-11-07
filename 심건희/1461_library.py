import sys

n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
left = []
right = []
for i in range(n): 
    if books[i] < 0: 
        left.append(books[i])
    else: 
        right.append(books[i])

result = 0

# 음의 방향
left.sort()
l_dist = 0
if left: 
    l_dist = abs(left[0])
i = m
while i < len(left): 
    result += abs(left[i]) * 2
    i += m

# 양의 방향
right.sort(reverse=True)
r_dist = 0
if right: 
    r_dist = abs(right[0])
i = m
while i < len(right): 
    result += abs(right[i]) * 2
    i += m


result += min(l_dist, r_dist) * 2 + max(l_dist, r_dist)
print(result)
