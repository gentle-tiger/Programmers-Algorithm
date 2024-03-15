
# 1번 

print("Hello")

# 2번 

print("Hello World")


# 3번

print("Hello")

print("World")


# 4번

print("'Hello'")


# 5번

print('"Hello World"')


# 6번

print("\"!@#$%^&*()\'")


# 7번

print('"C:\Download\\\'hello\'.py"')   # "C:\Download\'hello'.py"


# 8번

print('print("Hello\\nWorld")')


# 9번

c = input()

print(c)

# 10번
n = input()

print(int(n))  # input()을 사용하면 키보드로 입력(input)한 값을 가져온다.
 
# 11번
n = input()

print(float(n)) # 실수값 출력 

# 12번
a = input()
b = input()
print(int(a))
print(int(b))


# 13번
a = input()
b = input()
print(b)
print(a)


# 14번
n = input()
print(n)
print(n)
print(n)


# 15번

a,b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)


# 16번

a, b = input().split()

print(b,a)


# 17번
s = input()

print(s,s,s)


# 18번

a,b = input().split(':')

print(a,b,sep=":")      # sep=':' 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.



# 19번

y,m,d = input().split('.')  # 2020.3.4

print(d,m,y ,sep="-")       # 4-3-2020

# 20번

a,b = input().split('-')    # 000907-1121112

print(a+b)                  # 0009071121112

# 21번
s = input()

print(s[0])

print(s[1])

print(s[2])

print(s[3])

print(s[4])

# 22번
s = input()

print(s[0:2], s[2:4], s[4:6])


# 23번

h,m,s = input().split(':') # 17:23:57

print(m) # 23


# 24번

a,b = input().split() # hello world

print(a+b)


# 25번

a, b = input().split()

print(int(a)+int(b))


# 26번
a = input()
b = input()

print(float(a)+float(b))


# 27번  10진수를 입력받아 16진수(hexadecimal)로 출력
a = input()

n = int(a) # 내장함수 int()는 a를 10진수 값으로 변환

print('%x'%n) # %x를 통해 n을 16진수로 변환


# 28번

n = int(input(), 16)

print('%X'%n)  #  %X로 출력하면 16진수 대문자로 출력된다. 


# 29번

n = int(input(),16)

print('%o' %n) # 8진수(octal) 형태 문자열로 출력 


# 30번

n = ord(input())

print(n)   # 입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.


# 31번
n = int(input())

print(chr(n))  # n에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 


# 32번
n = int(input())

print(-n)


# 33번

s = ord(input())  # 아스키문자표에서 'A'는 10진수 65로 저장되고 'B'는 10진수 66으로 저장된다.

print(chr(s+1))


# 34번

a,b = input().split() # 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성

print(int(a) - int(b))

# 35번

a,b = input().split() # 실수 2개(f1, f2)를 입력받아 곱을 출력 0.5 2.0 => 1.0

print(float(a) * float(b))


# 36번

s, n = input().split() # love 3 

print(s*int(n)) # s를 n번 반복. 


# 37번
n = input()
s = input()

print(s*int(n))


# 38번

a,b = input().split() # a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성

print(int(a)**int(b))


# 39번

a,b = input().split() # 거듭제곱(exponentiation)을 계산하는 연산자(**)를 제공

print(float(a)** float(b))


# 40번

a,b = input().split()  # 나눈 몫을 계산하는 연산자(//, floor division)를 제공

print(int(a) // int(b))

# 41번
a,b = input().split()  # 나머지를 계산하는 연산자(%, remainder)를 제공

print(int(a) % int(b))

# 42번
a = input()    #  원하는 자리까지의 정확도로 반올림 된 실수 값
a = float(a)
print(format(a,".2f")) 

# 43번
a,b = input().split()
c = (float(a) / float(b)) # int()는 소수점을 받으면 에러를 발생시킴. 
print((format(c, ".3f")))


# 44번
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))

# 45번 정수 3개 입력받아 합과 평균 출력하기
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
f = format((sum/3),".2f")
print(sum , f )

# 46번 정수 1개 입력받아 2배 곱해 출력하기
n = input()
print(int(n)<<1)

# 47번 2의 거듭제곱 배로 곱해 출력하기
a,b = input().split()
print(int(a)<<int(b))

# 48번 정수 2개 입력받아 비교하기1
a, b = input().split()
print(int(a) < int(b))

# 49번 정수 2개 입력받아 비교하기2
a, b = input().split()
print(int(a) == int(b))

# 50번 정수 2개 입력받아 비교하기3
a,b = input().split()
print(int(a) <= int(b))

# 51번 정수 2개 입력받아 비교하기4
a,b = input().split()
print(int(a) != int(b))

# 52번 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

# 53번 참 거짓 바꾸기
n = int(input())
print(not bool(n))

# 54번 둘 다 참일 경우만 참 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) and bool(b))
# 55번 하나라도 참이면 참 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) or bool(b))

# 56번 참/거짓이 서로 다를 때에만 참 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) != bool(b))

# 57번 참/거짓이 서로 같을 때에만 참 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) == bool(b))

# 58번 둘 다 거짓일 경우만 참 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print( not bool(a) and not bool(b) ) # and는 모두 True일 때 True, not은 논리값을 뒤집습니다.

# 59번 비트단위로 NOT 하여 출력하기
a = input()
a = int(a) 
print(~a) # ~1 = -2

# 60번 비트단위로 AND 하여 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(a & b) # 3 & 5 = 1 

# 61번 비트단위로 OR 하여 출력하기
a,b = input().split()
a = int(a)
b = int(b)  
print(a | b) # 3 | 5 = 7

# 62번 비트단위로 XOR 하여 출력하기
a,b = input().split()
a = int(a)
b = int(b)
print(a ^ b) # 3 ^ 5 = 6

# 63번 정수 2개 입력받아 큰 값 출력하기
a, b = input().split()
a = int(a)
b = int(b)
a if a > b else b

# 64번
# input().split()으로 입력된 값을 공백을 기준으로 분할한 후 
# map()함수를 사용하여 각 요소를 int로 변환하고 map의 결과를 다시 풀어서 각 변수에 할당합니다. 
a,b,c = map(int, input().split()) 
print(min(a,b,c))

# 65번 정수 3개 입력받아 짝수만 출력하기 "1 2 3 4 5 6"
# 1
numbers = list(map(int ,input().split())) # [1, 2, 3, 4, 5, 6] 
result = filter(lambda x : x % 2 == 0 ,numbers)      
for num in result : 
    print(num)
# 2
a,b,c = input().split() 
a = int(a)
b = int(b)
c = int(c)
if a % 2 == 0 : print(a) 
if b % 2 == 0 : print(b) 
if c % 2 == 0 : print(c) 

# 66번 정수 3개 입력받아 짝/홀 출력하기
# 1
numbers = list(map(int, input().split()))
for num in numbers  :
    print("even") if num % 2 == 0 else print("odd")
# 2
a,b,c = map(int,input().split())
print("even") if a % 2 == 0 else print("odd")
print("even") if b % 2 == 0 else print("odd")
print("even") if c % 2 == 0 else print("odd")

# 67번 정수 1개 입력받아 분류하기
n = int(input())
if n < 0 :
    print("A") if n % 2 == 0 else print("B")
else :
    print("C") if n % 2 == 0 else print("D")

# 68번 점수 입력받아 평가 출력하기
# 1
n = int(input())
if n >= 90 :
    print("A")
elif 70 <= n < 90 :
    print("B")
elif 40 <= n < 70 :
    print("C")
elif 0 <= n < 40 :
    print("D")
else :
    print("")
    
# 2 
n = int(input())
grade = "A" if n >= 90 else "B" if n >= 70 else "C" if n >= 40 else "D"
print(grade) if grade else None   

 
# 69번 평가 입력받아 다르게 출력하기
s = input()
grade = "best!!!" if s == "A" else "good!!" if s == "B" else "run!" if s == "C" else "slowly~" if s == "D" else "what?"
print(grade)

# 70번 월 입력받아 계절 출력하기

    
s = int(input())
if (s == 12 or s ==  1 or s ==  2) : 
    print("winter")
elif (s == 3 or s ==  4 or s ==  5) :
    print("spring")
elif (s == 6 or s ==  7 or s ==  8) :
    print("summer")
else  :
    print("fall")
    
# 2
n = int(input())
if n // 3 == 1 : 
    print("spring")
elif n // 3 == 2 :
    print("summer")
elif n // 3 == 3 :
    print("fall")
else : print("winter") 


# 71번 0 입력될 때까지 무한 출력하기
n = 1
while n != 0 :  # n이 0이 아니면 반복문은 계속 실행되며 해당 숫자가 출력된다. 만약 0이라면 반복문은 종료된다.
    n = int(input())
    if n != 0 :
        print(n)  # 입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)
# 72번 정수 1개 입력받아 카운트다운 출력하기1
# 1
n = int(input())
while n != 0 :
    print(n)
    n = n - 1
# 2 
n = int(input())
while True :
    print(n)
    n = n - 1
    if(a == 0) : 
        break


# 73번 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())

while n != 0 :
    n = n - 1 # 위치만 변경
    print(n)

# 74번 문자 1개 입력받아 알파벳 출력하기
s = ord(input())
t = ord('a')

while t <= s:
    print(chr(t), end="") # end=' '는 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
    t += 1                # end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.

# 75번 정수 1개 입력받아 그 수까지 출력하기1
n = int(input())
t = int(0)
while s >= t : 
    print(t)
    t += 1
# 76번 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())
for i in range(n+1) :
    print(i)

    
# 77번 짝수 합 구하기 ★ 
n = int(input())
sum = 0
for i in range(n+1) : # 시작값(1)부터 끝값(n+1) 직전까지의 범위를 생성
    if i % 2 == 0 :
        sum += i
print(sum)

# 78번 원하는 문자가 입력될 때까지 반복 출력하기
while True : 
    n = input()
    print(n)
    if n == 'q' : break   # 무한루프를 생성하고 그 안에서 입력을 받습니다. 입력값을 출력한 뒤 입력값이 q라면 break로 무한루프를 탈출합니다.  
    
# 79번 언제까지 더해야 할까? ★★
n = int(input())
sum = 0
count = 0
while sum < n : # <=를 하게 되면 while문이 한 번더 돌아간다.
    count += 1
    sum += count
print(count)
    


# 80번 주사위 2개 던지기
n,m = map(int, input().split()) # 면의 개수
for i in range(1, n +1) :# 1 2 3 4 5 6
    for j in range(1, m+1):
        print(i, j)
        
# 81번 16진수 구구단 출력하기 ★★★
n = int(input(),16) # input으로 들어온 값이 16진수로 변환됨. int('A',16)-> 10
for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
    # '%X'는 변수를 대문자 16진수로 변환한다
    # '%X' % i 는 %X는 i 변수값을 대문자 16진수로 변환하여 문자열에 삽입한다. 
    # '=%X' % (n * i) 는 '%X' 는 n * i 의 값을 대문자 16진수로 변환하여 문자열에 삽입한다. 
    
# 82번 3 6 9 게임의 왕이 되자 ★★
n = int(input())
for i in range(1,n+1) :
    if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):  #  if i % 3 == 0  이렇게 할 경우 두자리수의 값은 해결이 되지 않는다.
        print('X', end=' ')
    else :
        print(i, end=' ')
     
# 83번 빛 섞어 색 만들기
a,b,c = map(int, input().split())

for i in range(0,a) :
  for j in range(0,b) :
    for k in range(0,c) :
    #  print(i, j, k)
    #  print('%d %d %d' %(i,j,k))
            
print(a*b*c)

# h44100 b16 c2 s10
# 84번 소리 파일 저장용량 계산하기 ★★★
# 1
h,b,c,s = map(int,input().split())
total_byte = h * b * c * s / 8 # 176400.0
total_kb = total_byte / 1024 # 172.265625
total_mb = total_kb / 1024 # 0.16822814...
print('%0.1f MB' % total_mb) # 1.7MB

# 2
h,b,c,s = map(int, input().split())
total = h*b*c*s/8/1024/1024
print(round(total, 1),'MB')
 
 
# 85번 그림 파일 저장용량 계산하기
r,g,b = map(int, input().split())
total = r*g*b/8/1024/1024  # 2.25
# print(round(total,2), 'MB') # round는 공백을 주는 메서드
print('%.2f' %total, 'MB') # %는 해당 자릿수까지 자르는 연산자

# 86번 거기까지! 이제 그만~ ★
n = int(input())
sum = 0
c = 1
while True :
    sum += c
    c += 1
    if n <= sum :
        break
print(sum)        
        
# 87번 3의 배수는 통과
n = int(input())
for i in range(1, n+1) :
    if i % 3 == 0 :
     continue
    print(i , end=' ')

# 88번 수 나열하기1 # 1 3 5   ★
# 1
a,d,n = map(int, input().split())
print(a +d * (n-1)) # 3 * (n-1) + 1

# 2 
a,d,n = map(int, input().split())
s = a 
for i in range(2,n+1)
    s += d
print(s)

# 89번 수 나열하기2 ★
a,r,n = map(int, input().split())
print(a * r **(n-1)) 

    
# 90번 수 나열하기3
## n번 반복하며, 반복할 때 answer 값이 할당된다. answer는 이전 값에 m을 곱하고 + 1을 해준 값이다.
# 1 메모리 사용량: 상수의 메모리 공간이 사용됨
a,m,d,n = map(int, input().split()) # 1 -2 1 8
count = 1
answer = a
while count < n  :
    # print(count)
    answer = (answer * m) + d  # answer는 누적이 아닌 계속 값이 재할당 된다. 
    count += 1
print(answer)

# 2 메모리 사용량: 추가 메모리가 사용되지 않음
a,m,d,n = map(int, input().split()) # 정해진 구간이 있는 반복은 for문이 더 낫나  
for i in range(1,n) :
    a = a * m + d
print(a)

# 91번 함께 문제 푸는 날


a,b,c = map(int, input().split())
a,b,c = map(int, "3 7 9".split())
d = 1
while True :
    if (a * d) == (b * d) == (c * d) :
        print(d)
        break
    d += 1
    




# 92번

# 93번

# 94번

# 95번

# 96번

# 97번

# 98번

# 99번
# 100번

