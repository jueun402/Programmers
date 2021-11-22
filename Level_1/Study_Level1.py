# 1. 두 정수 사이의 합

def solution(a, b):
    return sum(range(min(a,b), max(a,b)+1))

# 2. 수박수박수박수?

def solution(n):
    answer = '수박'*10000
    return answer[:n]

# best 풀이 

def water_melon(n):
    s = "수박" * n
    return s[:n]

# 3. 서울에서 김서방 찾기

def solution(seoul):
    a = [i for i,j in enumerate(seoul) if j == "Kim"]
    answer = "김서방은 "+ str(a[0])+ "에 있다"
    return answer

# best 풀이 
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim')) # index 사용법 

# 4. 약수의 합
# 5. 문자열 내 p와 y의 개수

def solution(s):
    return s.lower().count('p') == s.lower().count('y')


# 6. 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 7. 가운데 글자 가져오기

def solution(s):
    index = len(s)//2

    if len(s)%2 !=0:
        return s[index]
    else:
        return s[index -1 : index+1]

# best 풀이 
def string_middle(str):
    # str = "abcd"	    
    # wow 
    return str[(len(str)-1)//2:len(str)//2+1]

# 9. x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    result = x
    for i in range(n):
        answer.append(result)
        result +=x
        
    return answer

# best 풀이 
def number_generator(x, n):
    # x = 2
    # n = 5
    return [i * x + x for i in range(n)]

# 10. 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for _ in range(b): 
    print("*"*a)
    
# 11. 평균 구하기 
def solution(arr):
    return sum(arr)/len(arr)

# 12. 행렬의 덧셈
## 내 풀이 
def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr1[0]))] for row in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

## best 풀이 
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 13. 짝수와 홀수 

## 내 풀이 
def solution(num):
    return "Even" if num%2 ==0 else "Odd"

## best 풀이 
def evenOrOdd(num):
    if (num%2): # 1 = True 
        return "Odd"
    else:
        return "Even"
 
# 14. 자릿수 더하기 

## 내 풀이 
def solution(n):
    return sum([int(k) for k in str(n)])

# 15. 최대공약수와 최소공배수 

### 최대공약수, 최소공배수 코드는 외우기 
## 내 풀이 

# 최대공약수 
def gcd(a,b):
    m = max(a,b)
    n = min(a,b)
    while m > 0:
        n,m  = m, n%m
    return n

# 최소공배수 
def lcm(a,b):
    return a*b // gcd(a,b)

def solution(n, m):
    return [gcd(n,m),lcm(n,m)]


# Best 풀이 
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b) # 이렇게 공부하자 
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# best 반영 코드 수정
def solution(a, b):
    c,d = max(a,b), min(a,b)
    while d>0:
        c,d = d, c%d
    return [c, a*b //c] # [최대공약수, 최소공배수]


# 16. 정수 제곱근 판별 

## 내 풀이 
# binary search로 풀어봐야겠다
def solution(n):
    start = 1
    end = n
    while start <= end:
        mid = (start+end)//2

        if mid**2 == n:
            return (mid+1)**2

        elif mid**2 > n:
            end = mid-1
            
        else:
            start = mid+1
    return -1

# best 풀이 
def nextSqure(n):
    sqrt = n ** (1/2) # n**(1/2) => 제곱근(!!)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1