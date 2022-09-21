#숫자가 2자리 이상일 경우 올바르지 않은 알고리즘임

n = int(input())
# 첫 수열과 다음 수열을 문자열로 바꾼다
first = "".join(input().split())
last = "".join(input().split())

# 밀기: 퍼즐 두개를 연결하여 원순열 같이 만들어주면서 처리
# 뒤집기: 뒤집기를 두번한 경우 원래의 순열과 같아지므로 뒤집기 한번한 경우만 고려
puzzle_forward = first+ first # 밀기만
puzzle_reverse = first[::-1] + first[::-1] # 뒤집기 한번 + 밀기

# 둘 다에 해당하지 않으면 bad
if(puzzle_forward.find(last) == -1 and puzzle_reverse.find(last) == -1):
    print("bad puzzle")
else: # 해당하면 good
    print("good puzzle")



n = int(input())
# 리스트로 받기
first = list(map(int, input().split()))
last = list(map(int, input().split()))


#forward
last.extend(last) # 원순열로 만들기 위해 list extend
idx = last.index(first[0]) # 첫번째 원소 위치 찾아주기

# 각 리스트의 첫번째 원소 위치부터 맞게 가는지 확인
for i in range(n):
    if(first[i] != last[idx + i]):
        break
else:
    # 모두 맞았으면 good puzzle & 종료
    print("good puzzle")
    exit()

# backward
# 리스트 뒤집어서 첫번째 원소위치 다시 찾기
last.reverse()
idx = last.index(first[0])
# 각 리스트의 첫번째 원소 위치부터 맞게 가는지 확인
for i in range(n):
    if (first[i] != last[idx + i]):
        # 둘다 틀렸으므로 bad puzzle
        print("bad puzzle")
        break
else:
    # 모두 맞았으면 good puzzle
    print("good puzzle")



