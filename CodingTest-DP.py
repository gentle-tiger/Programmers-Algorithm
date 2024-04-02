# 이것이 코딩테스트다. 
## Chapter.8 다이나믹 프로그래밍 (208p)   
### 8-1 피보나치 함수 소스코드 

def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))  # 결과값 : 3 


# -----------------------------------------------------

### 피보나치 수열 소스코드(재귀적)
#### 한번 계산된 결과를 memoization하기 위한 리스트 초기화
d = [0] * 100

#### Fibonacci Function를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x) :
    #### 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2 :
        return 1
    
    #### 이미 계산한 적 있는 문제라면 그대로 반환 
    if d[x] != 0 :
        return d[x]
    
    #### 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환 
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99)) # 결과값 : 218922995834555169026

# -----------------------------------------------------

### 피보나치 수열 소스코드(반복적)
#### 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0] * 100

#### 첫 번째 피보나치 수와 두 번째 피보나치 수는 1 
d[1] = 1
d[2] = 1
n = 99

#### Fibonacci Function 반복문으로 구현(보텀업 다이나믹 방식)
for i in range(3, n + 1) :
  d[i] = d[i - 1] + d[i - 2]
print(d[n])  # 결과값 : 218922995834555169026

# -----------------------------------------------------

#### 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 0(N)입니다. 
d = [0] * 100
def fibo(x) :
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6) # 결과값 : f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)

# -----------------------------------------------------

## <문제> 개미 전사 
n = 50


# 모든 식량 정보 입력 받기
array = [50, 10, 20, 30, 40, 45, 35, 25, 15, 10, 5, 45, 25, 15, 10, 50, 10, 20, 30, 40, 45, 35, 25, 15, 10, 5, 45, 25, 15, 10, 50, 10, 20, 30, 40, 45, 35, 25, 15, 10, 5, 45, 25, 15, 10, 50, 10, 20, 30]

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    print(f'd[{i}] = max({d[i-1]}, {d[i-2]} + {array[i]})' )  # 해당 위치의 DP 테이블 값을 출력하여 확인

print(f'최대 얻을 수 있는 식량의 양: {d[n-1]}')  # 마지막으로 계산된 결과 출력


# -----------------------------------------------------
# <문제> 1로 만들기 
#### 1 <= x <= 30000
x = int(input())
x = 7
d = [0] * 30001
for i in range(2, x + 1) :
    
    #### 현재의 수에서 1을 빼는 경우 
    d[i] = d[i - 1] + 1
    print(f'd[{i}] = d[{i - 1}]{d[i-1]} + 1','+1')
    if i % 2 == 0 :
        d[i] = min(d[i], d[i // 2] + 1)
        print(f'd[{i}] :{d[i]} = min({d[i], d[i // 2] + 1})','+2')
# 36 // 3 => 12 
    if i % 3 == 0 : 
        d[i] = min(d[i], d[i // 3] + 1)
        print(f'd[{i}] :{d[i]} = min({d[i], d[i // 3] + 1})','+3')
        
    if i % 5 == 0 :
        d[i] = min(d[i], d[i // 5] + 1)
        print(f'd[{i}] :{d[i]} = min({d[i], d[i // 5] + 1})','5')
print(d[7])




# -----------------------------------------------------

# <문제> 효율적인 화폐 구성 (m원을 만들기 위한 최소한의 화폐 개수)
#### 1 <= n <= 100
#### 1 <= m <= 10,000

#### 예시 설정 
#### n = 2, m = 15 
n, m = map(int, input().split())

#### N개의 화폐 단위 정보를 입력  array = [2,3]
array = []
for i in range(n) :
    array.append(int,(input()))

#### 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [10001] * (m + 1) 

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0 
for i in range(n) : 
    for j in range(array[i], m + 1) : # 2~15, 3~ 15 즉 화폐 단위가 2일 때
        if d[j-array[i]] != 10001 :  
            d[j] = min(d[j], d[j - array[i]] + 1)

# 화폐 가치에 따른 최소 계산값 출력
if d[m] == 10001 :
    print(-1)
else :
    print(d[m])



#-----------------------------------------------
# <문제>금광 


for tc in range(int(input())) :
    n, m = map(int, input().split()) #### n(가로) 4, m(세로) 3
    array = list(map(int, input().split()))
    dp = []
    index = 0
# array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for i in range(n) : #### 4 / 배열의 길이만큼 돈다. 
        dp.append(array[index : index + m]) #### array 리스트의 index부터 index + m까지의 요소가 추가
        index += m #### 4만큼 오르면서 input으로 들어오는 배열을 4개씩 끊어서 나눈다. 
        print('index :', index) #### 4 8 12
        # [1, 2, 3, 4]
        # [5, 6, 7, 8]
        # [9, 10, 11, 12]
    # 다이나믹 프로그래밍 
    for j in range(1, m) : #### 1, 2, 3
        for i in range(n) :
            # 왼쪽 위에서 오는 경우 
            if i == 0 : left_up = 0
            else : left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else : left_down = dp[i+1][j+1]
            # 왼쪽에서 오는 경우 
            left = dpp[i][j-1]
            dp[i][j] = d[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n) : 
        result = max(result, dp[i][m-1])
    print(result)            
                