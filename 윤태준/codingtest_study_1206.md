# 베스트앨범

[코딩테스트 연습 - 베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

## 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

## 제한사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예

```
# 입력
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 출력
return = [4, 1, 3, 0]
```

### 입출력 예 설명

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

- 고유 번호 3: 800회 재생
- 고유 번호 0: 500회 재생
- 고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

- 고유 번호 4: 2,500회 재생
- 고유 번호 1: 600회 재생

따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

- 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

### 풀이

```python
import collections

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = [] # 답을 저장하는 리스트
    counter = collections.Counter() # 장르별로 얼마나 많은 play를 기록(기준1: 속한 노래가 많이 재생된 장르를 먼저 수록)
    dic = collections.defaultdict(list) # 각 장르에서 [노래, 고유번호]를 기록(기준2, 3: 장르 내에서 많이 play, 고유번호 순)
		
		# counter와 dic 기록
    for i, (g, p) in enumerate(list(zip(genres, plays))): # i는 노래 고유번호, g는 노래의 장르 p는 노래의 play수
        counter[g] += p
        dic[g].append([p, i])
		# 기준 2, 3을 위해 dic내의 장르 안에서 노래별 정렬
    for d in dic:
        dic[d].sort(key=lambda x: (x[0], -x[1])) # play 오름차순, 고유번호 내림차순 정렬
		# 기준 1을 위해 poplst만들고 많이 플레이 된 순으로 리스트에 넣어줌
    poplst = [] # 많이 플레이 된 장르 순으로 list만들기 위해 만들어줌
    for a, b in counter.most_common():
        poplst.append(a)

		
    for genre in poplst:
				# 장르별로 노래가 2개 이상이면
        if len(dic[genre]) >= 2:  # 두개만 하는 이유는 제한조건에 있음(장르별 재생된 노래 최대 두개모음)
            answer.append(dic[genre].pop()[1])
            answer.append(dic[genre].pop()[1])
				# 장르별로 노래가 한개면
        else:
            answer.append(dic[genre].pop()[1])
    return answer

print(solution(genres, plays))
```
