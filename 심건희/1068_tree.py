import sys

n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
remove = int(sys.stdin.readline())
tree = [[] for _ in range(n)]
root = -1
for i in range(n): 
    if i != remove and parents[i] != remove: 
        if parents[i] == -1: 
            root = i
        else: 
            tree[parents[i]].append(i)

cnt = 0
def dfs(n1): 
    global cnt
    for n2 in tree[n1]: 
        dfs(n2)
    if len(tree[n1]) == 0: 
        cnt += 1

if root != -1: 
    dfs(root)
print(cnt)
