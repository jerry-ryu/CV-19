import sys

t = int(sys.stdin.readline())
for _ in range(t): 
    n, m = map(int, sys.stdin.readline().split())
    books = [1] * (n+1)
    ranges = []
    for _ in range(m): 
        a, b = map(int, sys.stdin.readline().split())
        ranges.append([a, b])
        
    ranges.sort(key=lambda x: (x[1], -x[0]))
    result = 0
    for a, b in ranges: 
        for i in range(a, b+1): 
            if books[i]: 
                books[i] = 0
                result += 1
                break
    print(result)
