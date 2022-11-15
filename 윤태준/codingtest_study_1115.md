![image](https://user-images.githubusercontent.com/54363784/201822370-05101fc1-cbd0-4a12-99ea-351899d18354.png)


```python
def solution(properties, location):
    queue = []
    answer = 0
		#먼저 문제 순서대로 인덱스와 중요도를 queue에다가 append를 함
    for index, importance in enumerate(properties):
        queue.append([importance, index])

    while queue:
				# 큐의 첫번째가 가장 큰 중요도를 갖고 있다면 answer += 1
        if queue[0] == max(queue, key=lambda x: x[0]):
            answer += 1
            if queue[0][1] != location:
                queue.pop(0)
						# 첫번째의 요소가 가장 크고 location과 같다면 answer
            else:
                return answer
				# 그렇지 않으면 큐의 맨 뒤에다가 다시 가져다둠
        else:
            queue.append(queue.pop(0))

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
```

### 문제 풀이

먼저 문제 순서대로 인덱스와 중요도를 queue에다가 append를 함

큐에서는 큐의 첫번째가 가장 큰 중요도를 갖고 있다면 answer += 1을 하고 큐의 첫번째 것을 pop(0)해주고 그렇지 않으면 큐의 맨 뒤에다가 다시 가져다둠

만약 첫번째의 요소가 가장 크고 location과 같다면 answer이 답이다.
