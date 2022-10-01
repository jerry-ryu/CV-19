import sys

string = sys.stdin.readline() # 괄호 문자열 받아오기

stack = [] # stack
l = [[] for i in range(16)] # 깊이에 따른 리스트
# 문자열의 길이가 1이상 30이하이므로 15개 + layer +1 연산의 OutofIndex 방지를 위해 1 = 16개
flag = 0 # 0: 올바른 괄호열, 1: 올바르지 않은 괄호열ㄹ

# 현재 layer까지 더해준다
def calculate_stack():
    tmp = stack.pop()
    layer = len(stack) # stack의 높이 == tmp가 들어가야 할 깊이
    if l[layer + 1]: # 들어가야할 깊이보다 깊은 리스트에 값이 있으면
        l[layer].append(tmp * sum(l[layer + 1])) # 모두 더해서 *
        l[layer + 1] = [] # 깊은 리스트 초기화
    else:
        l[layer].append(tmp) # 없으면, 그냥 넣기


for i in string:
    if i == '(': # 2추가
        stack.append(2)
    elif i == '[': # 3추기
        stack.append(3)
    elif i == ')': # stack에 값이 존재하고 2라면 올바른 괄호열이므로
        if stack and stack[len(stack) - 1] == 2:
            calculate_stack() # 깊이에 따라 적절한 list에 추기
        else:
            flag = 1 # 올바른 괄호열이 아니므로 break
            break

    elif i == ']':# stack에 값이 존재하고 3라면 올바른 괄호열이므로
        if stack and stack[len(stack) - 1] == 3:
            calculate_stack() # 깊이에 따라 적절한 list에 추기
        else:
            flag = 1
            break

# stack에 값이 남았거나 올바른 괄호열이 아니라면 0
if flag or stack:
    print(0)
else: # 올바른 괄호열이었다면, 1층 값 전체 더하기
    print(sum(l[0]))
