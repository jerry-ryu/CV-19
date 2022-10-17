# 편집 거리
문제유형: 다이나믹 프로그래밍, 기존 1차원이 아닌 2차원에서 차이점

## 편집거리 알고리즘?
어떠한 문자열을 삽입, 삭제, 변경을 몇번이나 해서 바꿀 수 있는지 계산하여 유사도 판단의 척도로 다룸
만약 두 문자열이 비슷하면 편집거리가 작고, 그렇지 않다면 편집거리가 큼




### 점화식
* 두 문자가 같은 경우: dp[i][j] = dp[i-1][j-1]

* 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j - 1] **삽입** , dp[i - 1][j] **삭제** , dp[i - 1][j - 1] **교체**)



```python
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(n + 1):
        dp[0][i] = i
    for j in range(m + 1):
        dp[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]

str1 = input()
str2 = input()
print(edit_dist(str1, str2))
```
