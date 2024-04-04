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

















