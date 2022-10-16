# import sys
#
# n = int(sys.stdin.readline())
# p = [i for i in range(n+1)] # 부모배열 만들기
# cycle = set()
#
# def find(x):
#     if(x == p[x]):
#         return x
#     p[x] = find(p[x])
#     return p[x]
#
# def union(x,y):
#     x_p = p[x]
#     y_p = p[y]
#
#     if x_p > y_p:
#         p[x_p] = y_p
#     elif x_p < y_p:
#         p[y_p] = x_p
#     else:
#         cycle.add(p[x])
#
#
# for first in range(n):
#     second = int(sys.stdin.readline())
#
#     union(first + 1,second)
#
# for i in range(n):
#     p[i] = find(i)
#
# tmp = set()
#
# for i in cycle:
#     tmp.add(find(i))
#
# print(tmp)

# dfs
import sys

n = int(sys.stdin.readline())

# 인접한 노드에 대한 리스트를 만든다
arr = {i: [] for i in range(1, n + 1)}
for i in range(1,n+1):
    m = int(sys.stdin.readline())
    arr[m].append(i)

# 사이클에 존재하는 노드를 넣을 set
s = set()

for i in range(1,n+1):
    q = []
    if i in arr[i]: # 자기자신으로 그래프가 생기면 사이클 ex. 5->5
        s.add(i)
        continue
    q.extend(arr[i]) # 인접 노드 리스트 넣어주기

    while q:
        new = q.pop()
        if i in arr[new]: # DFS를 돌다가 자기 자신이 나오면
            s.add(i) # 그 노드는 cycle의 구성요소이다.
            break
        q.extend(arr[new])

print(len(s)) # 노드개수
for i in sorted(s): # 노드
    print(i)