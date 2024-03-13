
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

# 52번

# 53번

# 54번

# 55번

# 56번

# 57번

# 58번

# 59번

# 60번

# 61번

# 62번

# 63번

# 64번

# 65번

# 66번

# 67번

# 68번

# 69번

# 70번

# 71번

# 72번

# 73번

# 74번

# 75번

# 76번

# 77번

# 78번

# 79번

# 80번

# 81번

# 82번

# 83번

# 84번

# 85번

# 86번

# 87번

# 88번

# 89번

# 90번

# 91번

# 92번

# 93번

# 94번

# 95번

# 96번

# 97번

# 98번

# 99번
# 100번

