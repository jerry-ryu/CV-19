# 코테 스터디 정리

## 치킨배달

크기가 NxN인 도시가 있다. 도시는 1x1크기의 칸으로 나누어져 있고 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 ‘치킨거리’라는 말을 주로 사용한다. 치킨거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지면, 각각의 집은 치킨거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의이 두 칸 (r1, c1)과 (r2, c2)간의 거리는 |r1-r2| + |c1-c2|로 구한다.

**0은 빈칸, 1은집, 2는 치킨집이다.**

example input

0 2 0 1 0

1 0 1 0 0

0 0 0 0 0

0 0 0 1 1

0 0 0 1 2

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프랜차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨 집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 N(도시의 크기), M(치킨집의 수)

다음줄부터

0 2 0 1 0

1 0 1 0 0

0 0 0 0 0

0 0 0 1 1

0 0 0 1 2

이런형식 input

### 내 풀이

1. 집이랑 치킨집 좌표 저장
2. combination(치킨집들, m)해서 각각 최소거리 구함
3. 각 combination마다 치킨거리 업데이트해줌

### min_distance함수 설명

각 집에서 가장 짧은거리에 있는 치킨집들 list에 넣어두고 합쳐줌

```python
import itertools
n, m = map(int, input().split())
chicken = []
house = []
# 
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])
        else:
            continue
def min_distance(house, chicken):
    tmp = []
    for x, y in house:
        m = 99999
        for i, j in chicken:
            m = min(m, abs(x - i) + abs(y - j))
        tmp.append(m)
    return sum(tmp)

cc = list(itertools.combinations(chicken, m))
min_num = 9999
for c in cc:
    min_num = min(min_num, min_distance(house, c))

print(min_num)
```
