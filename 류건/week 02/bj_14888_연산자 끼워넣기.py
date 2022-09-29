import sys


# 재귀 함수를 사용하여 dfs 구현
def recursive(N, l, op, total):
    # N 남은 연산 횟수, ㅣ: 숫자배열, op: 남은 연산자, total: 계산 누적값
    global max, min
    # 연산이 끝나면, max, min 갱신
    if(N == 0 ):
        if(total > max):
            max = total
        if(total < min):
            min = total
        return

    # 더하기
    if(op[0] >0):
        op[0] -= 1
        recursive(N - 1, l,op, total + l[len(l) - N])
        op[0] += 1 # 계산 끝나면 다시 연산자 복원

    # 빼기
    if (op[1] > 0):
        op[1] -= 1
        recursive(N - 1, l, op, total - l[len(l) - N])
        op[1] += 1

    #곱하기
    if (op[2] > 0):
        op[2] -= 1
        recursive(N - 1, l, op, total * l[len(l) - N])
        op[2] += 1

    # 나누기
    if (op[3] > 0):
        op[3] -= 1
        # 음수의 나눗셈
        if(total < 0 ):
            tmp = abs(total) // l[len(l) - N]
            total = -tmp
        else:
            total = total // l[len(l) - N]
        recursive(N - 1, l, op, total)
        op[3] += 1


n = int(sys.stdin.readline().rstrip())
l =  list(map(int, sys.stdin.readline().rstrip().split()))
op = list(map(int, sys.stdin.readline().rstrip().split()))


min = sys.maxsize
max = -sys.maxsize
recursive(n-1,l,op,l[0]) # 재귀 시작, 첫 누적값 = l[0]
print(max)
print(min)