# ---------------
# 스택 구현 예제
stack = [] #### stack은 list형태를 사용한다. 
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #### 7
stack.append(1)
stack.append(4)
stack.pop() #### 4

print(stack[::-1]) #### 최상단 원소부터 출력 : [1, 3, 2, 5]
print(stack) #### 최하단 원소부터 출력 : [5, 2, 3, 1]


# ---------------
# 큐 구현 예제
from collections import deque

# 큐(queue) 구현을 위해 덱(deque) 라이브러리 사용 
queue = deque()
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #### 5
queue.append(1)
queue.append(4)
queue.popleft() #### 2

print(queue) # a먼저 들어온 순서대로 출력 : deque([3, 7, 1, 4])
queue.reverse() # 역순을 바꾸기 
print(queue) # 나중에 들어온 원소부터 출력 : deque([4, 1, 7, 3])


# -----------------------
# 재귀함수 

def recursive_function(i):
    if i == 100 :
        return
    print(f'{i}번째 재귀함수에서 {i + 1}번째 재귀함수를 호출합니다.')
    
    recursive_function(i+1)
    print(f'{i}번째 재귀함수를 종료합니다.')
    
recursive_function(1)


# -----------------------
# 팩토리얼 구현 예제

# 반복적으로 구현한 n! 
def factorial_iterative(n):
    result = 1
    
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1) : 
        result = result * i
    return result    
    
print('반복적으로 구현',factorial_iterative(5))
    
# 재귀적으로 구현한 n! 
def factorial_iterativee(n):
    if n <= 1 : # n이 1이하인 경우 1을 반환 
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기 
    return n * factorial_iterativee(n-1)


print('재귀적으로 구현',factorial_iterativee(5))



# -----------------------
# 유클리드 호제법

def gcd(a,b) :
    if a % b == 0 :
      print(b)
      return b #### 해당 b는 else의 return 값인 gcd()의 b로 다시 들어가게 된다. 
    else :
        print(f'{b}, a{a}%b{b} = {a % b}')
        # 162, a:192 % b:162 = 30
        #  30, a:162 % b:30 = 12
        #  12,  a:30 % b:12 = 6
        return gcd(b, a % b)

print(gcd(192,162))  


# -----------------------
# DFS 소스코드 예제 

# DFS 메서드 정의 
def dfs(graph, v, visited) :
    
    # 현재 노드를 방문 처리 
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출 
dfs(graph, 1, visited) #### 1 2 7 6 8 3 4 5


# -----------------------
# BFS 소스코드 예제 

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited) :
    
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용 
    queue = deque([start])
    # 현재 노드를 방문처리 
    visited[start] = True
    # 큐가 빌 때까지 반복 
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기 
        v = queue.popleft() #### popleft 메서드는 큐의 맨 앞에 있는 원소를 추출
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입 / graph[v]는 노드 v와 연결된 노드들을 담은 리스트 / 따라서 for i in graph[v]는 현재 노드 v와 연결된 노드들을 탐색하게 됩니다.
        for i in graph[v] :
            if not visited[i] : #### not은 부정연산자로 false를 만나야 참(true)이 됨. 즉  visited[i]가 false라면 참이 됨으로 다음 코드가 실행됨. 
                                #### 즉 해당 노드 i가 이미 방문된 상태라면 if not visited[i]는 거짓이 되어 해당 노드를 큐에 추가하지 않고 다음 인접한 노드를 탐색하게 됩니다.
                queue.append(i) #### append 메서드는 큐의 맨 뒤에 원소를 추가하는 것
                visited[i] = True
                
                


# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출 
dfs(graph, 1, visited) #### 시작 노드가 1이라는 뜻. 



# -----------------------
# 음료수 얼려먹기 

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문 

def dfs(x,y) :
    # 주어진 범위를 벗어지는 경우에는 즉시 종료 
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리 
        graph[x][y] = 1
        # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 왼쪽
        dfs(x + 1, y)  # 오른쪽
        dfs(x, y - 1)  # 아래
        dfs(x, y + 1)  # 위
        return True  # 현재 노드가 음료수인 경우 True 반환. 만약 여기서 x or y 가 범위를 넘어가더라도 해당 값이 다시 dfs를 실행할 때 조건식에서 걸려 false를 반환하게 된다. 
    return False  # 현재 노드가 이미 방문한 경우 False 반환



n,m = map(int,'4 5'.split()) 
print(f'n :{n}, m :{m}')
s = list('00110 00011 11111 00000'.split())
s
graph = []
#### 2차원 배열 만들기 
for i in s :
    row = []
    for j in i :
        row.append(int(j))
    graph.append(row)
    
#### 2차원 배열 출력해보기
for i in range(n) : 
    print(graph[i])

graph[1][1]

# 모든 노드(위치)에 대하여 음료수 채우기 
result = 0
for i in range(n) :
    for j in range(m) :
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True :
            result += 1
            
print(result)


# -----------------
# 미로 탈출
from collections import deque

# BFS 소스코드 구현 
def bfs(x,y) : 
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    print('queue :', queue)
    # 큐가 빌 때까지 반복하기 
    while queue :
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인 
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > n or ny < 0 or ny > m :
                continue
            
            # 괴물이 있는 부분 무시  
            if graph[nx][ny] == 0 :
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 
            if graph[nx][ny] == 1 :
                graph[nx][ny] == graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환 
    return graph[n-1][m-1]

                






# N, M을 공백기준으로 구분하여 입력 받기 
# n, m = map(int, input().split())
n, m = map(int, '4 5'.split())
print(f'n :{n},  m :{m}')

# 2차원 리스트의 맵 정보 입력 받기 
test = list('101010 111111 000001 111111 111111'.split())
test

graph = []

# for i in range(n) :
#     graph.append(list(map(int,input())))
print('graph :', graph)
for i in test :
    arr = []
    for j in i : 
        arr.append(int(j))
    graph.append(arr)

print('graph :', graph) 

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0] # (-1,0) 상 ~ (0,1) 우
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(1,0))



