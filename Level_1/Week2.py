######## 1. 문자열 다루기 기본 ########
# 내 풀이 
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

# best 풀이 
def solution(s):
    return s.isdigit() and len(s) in (4,6) # good.. 

######## 2. 정수 내림차순으로 배치하기 ########
# 내 풀이 
def solution(n):
    a = sorted(list(str(n)),reverse=True)
    temp = ''
    for i in a:
        temp +=i
    return int(temp)

# best 풀이 
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))


######## 3. 자연수 뒤집어 배열로 만들기 ########
# 내 풀이 
def solution(n):
    ls = list(str(n))
    return list(map(lambda x : int(x), ls[::-1])) # map(함수, 입력들)

# best 풀이 
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


######## 4. 핸드폰 번호 가리기 ########
## 조건 : 전화번후 뒷 4자리 제외한 나머지 숫자 *로 가린 문자열 return 
# 내 풀이 
def solution(phone_number):
    return '*'*(len(phone_number)-4)+str(phone_number[-4:])
    

######## 5. K번째수 ########

## 조건 : 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 함

# 내 풀이 
def solution(array, commands):
    # array = [1, 5, 2, 6, 3, 7, 4]	
    # commands  = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	# command가 조건 
    result = []
    for condition in commands:
        i,j,k = condition[0]-1,condition[1], condition[2]-1
        result.append(sorted(array[i:j])[k])

# best 풀이 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



######## 6. 하샤드 수 ########
## 조건 : x의 자릿수의 합으로 x가 나누어져야 함 

# 내 풀이 
def solution(x):
    return x%sum(list(map(int,str(x))))==0

# best 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0


######## 7. 나누어 떨어지는 숫자 배열 ########
## 조건 : array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.

# 내 풀이 
def solution(arr, divisor):
    condition = [i for i in arr if not(bool(i%divisor))]
    
    # 한 줄로 줄이고 싶었는데..
    if bool(len(condition)): return sorted(condition)
    else: return [-1]
    
# best 풀이 
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1] # or을 쓰면 된다 


######## 8. 모의고사 ########
# 내 풀이 
def solution(answers):
    first = [1, 2, 3, 4, 5]*2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] *1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    cnt = [0,0,0,0]
    for i in range(len(answers)):
        if answers[i] == first[i]:
            cnt[1] +=1 
        if answers[i] == second[i]:
            cnt[2] +=1
        if answers[i] == third[i]:
            cnt[3] +=1 

    result = []
    for i in range(1,4):
        if cnt[i] == max(cnt):
            result.append(i)

    return result


# best 풀이 1
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]: # idx % len(문자열) 기억하기 
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# best 풀이 2
# https://wikidocs.net/108925 
from itertools import count, cycle # 무한 반복자 
def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

######## 9. 완주하지 못한 선수 ########
# 내 풀이 
## 정답 
def solution(participant, completion):
    completion.sort()
    participant.sort()

    for i in range(len(participant)):
        try:
            if completion[i] != participant[i]:
                return participant[i]
        except:
            return participant[i]

## try 1. Runtime Error 
def solution(participant, completion):
    for comp in completion:
        participant.remove(comp)
    return participant[0]

## best 풀이 
import collections
def solution(participant, completion):
   # 차집합 
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


## best 풀이 변형 1
from collections import Counter
def solution(participant, completion):
    answer = list(Counter(participant) - Counter(completion) )
    return answer.pop()



######## 10. 2016년 ########
## 조건 : 2016 a월 b일은 무슨 요일 return 함수 

# 내 풀이 ( %써서 하고 싶었지만, 모르겠어서 datetime import함)
import datetime
def solution(a, b):
    DAY = ["MON","TUE","WED","THU","FRI","SAT","SUN" ]
    return DAY[datetime.date(2016,a,b).weekday()]

# best 풀이 

def solution(a, b):

    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    now = 5 # 시작 날짜 (Friday)
    # a-1달 까지의 day 더하기   
    now = sum(dayLen[:a-1]) +now 
   # 1월달은 첫째 날(금요일)을 더해서 시작했으므로, day -1을 해줌 
    answer = (now + b - 1) % 7 # 
    return days[answer]


# best 풀이 practice 1
def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[(sum(dayLen[:a-1]) + b-1)%7]

# best 풀이 practice 2
def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU","FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    now = 5
    days[((sum(dayLen[:a-1])+now)+b-1)%7]
    
    return days[(sum(dayLen[:a-1]) + b-1)%7]



######## 11. 소수찾기 ########
## 조건 : 1부터 n사이에 있는 소수 개수 반환 

## 방법 1 : 단순 소수 판단  ==> runtime error 
def isPrime(x):
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True

sum(list(map(lambda x: isPrime(x), list(range(2,n+1)))))

## 방법 2: 약수 찾기 성능 향상 (제곱근까지만 파악) ==> 통과 
def isPrime(x):
    for i in range(2,int(x ** (1/2))+1):
        if (x % i == 0):
            return False
    return True

sum(list(map(lambda x: isPrime(x), list(range(2,n+1)))))

#### 번외) lambda와 for문 성능 비교 ==> lambda가 성능 Win
## 1. lambda 
import time

start_time = time.time()
sum(list(map(lambda x: isPrime(x), list(range(2,n+1)))))
print("---{}s seconds---".format(time.time()-start_time)) # ---0.02644205093383789s seconds---


## 2. for문 
start_time = time.time()
result = 0
for i in range(2,n+1):
    if(isPrime):
        result +=1
print("---{}s seconds---".format(time.time()-start_time)) # ---0.046158790588378906s seconds---


######## 12. 예산 ########
## 예산 내에 최대한 많은 부서의 물품 구매 
## max값을 뺐을 때 less_mon보다 큰지 작은지 고려 

## 내 풀이  ==> 통과 
def solution(d, budget):
    less_mon = sum(d)-budget
    d.sort()
    while True:
        if  less_mon <= 0:
            break
        d = d[:-1]
        less_mon = sum(d)-budget 
    return len(d)

## pop()과 slicing 성능 비교  ==> slicing 성능 Win
import time

d = [1,3,2,5,4]	
budget = 9
d.sort()

start_time = time.time()
while budget <= sum(d):
    d = d[:-1]
print("---{}s seconds---".format(time.time()-start_time)) 
# ---0.021351337432861328s seconds---

d = [1,3,2,5,4]	
budget = 9
d.sort()

d.sort()
start_time = time.time()
while budget <= sum(d):
    d.pop()
print("---{}s seconds---".format(time.time()-start_time))
# ---0.04585075378417969s seconds---


######## 13. 체육복 ########
''' 전체 학생 수 : n 
    체육복 도난당한 학생 번호 담긴 배열 lost 
    여벌 체육복 가져온 학생들 번호 담긴 배열 revserve 
    체육수업 들을 수 있는 학생 최댓값 return 
    여벌 체육복이 있는 학생만 다른 학생에게 체육복 빌려줄 수 있음 

    3, 5, 7 , 12 통과 안됨 => 여분 but lost인 조건 해결 
    테스트 18, 20 통과 못함  => reserve sort 해결 => 순서대로 
'''
## 내 풀이 => 통과 

def solution(n, lost, reserve):

    student = [0]*(n+2) # r-1, r+1 오류 방지 

    for l in lost:
        if l in reserve: # 체육복 도난 + 여분 = 0
            continue
        else:
            student[l] = -1

    reserve.sort()

    for r in reserve:
        if r in lost: # 체육복 도난인데 여분 ==> 자기가 씀 
            continue
        if student[r-1] == -1:
            student[r-1] = 0 

        elif student[r+1] == -1:
            student[r+1] = 0 

    return student.count(0)-2

## best 풀이 
## lost 배열에서 조건 수행 후 lost의 len을 n에서 뺌 
## 개수만 찾는 방법에서 이렇게 하면 더 낫겠다  

n = 5
lost = [1,3,5]
reserve = [2,3,6]

def solution(n, lost, reserve):

    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve)- set(lost)) ## set끼리 차집합 할 수 있다 기억 ! 
   
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

######## 14. 시저 암호 ########
## ex. "AB"는 1만큼 밀면 "BC", 3만큼 밀면 "DE"
## ex. "z"는 1만큼 밀면 "a"

## 풀이 방법 : ASCI CODE  

def solution(s, n):

    a = list(range(97,123)) # a~z
    A = list(range(65,91)) # A~Z 

    s = list(s)

    for i in range(len(s)):
        if s[i] ==" ":
            continue
        
        if s[i].isupper(): # 대문자 
            s[i] = chr(A[int(((ord(s[i])+n) - 65) % 26)])
        
        else:
            s[i] = chr(a[int(((ord(s[i])+n) - 97) % 26)])

    answer = ""
    for i in s:
        answer +=i 

    return answer   


######## [1차] 비밀지도 ########

n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]

# 내 풀이 
def solution(n, arr1, arr2):
    r1 = [[0 for col in range(n)] for row in range(n)]
    r2 = [[0 for col in range(n)] for row in range(n)]


    result = []
    for r1,r2 in zip(arr1, arr2):
        b1 = list(bin(r1))[2:]
        b2 = list(bin(r2))[2:]

        s1= [0]*(n-len(b1)) + list(map(int,b1))
        s2 = [0]*(n-len(b2)) + list(map(int,b2))

        for i,j in zip(s1,s2):
            # print(i+j)
            if i+j >0: 
                result.append("#")
            else:
                result.append(" ")

    a = list(range(n,(n*n)+1,n))
    s = 0
    l = []
    for i in a:
        l.append("".join(result[s:i]))
        s = i
    return l

# best 풀이 

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # or 
        print(a12)
        a12=a12.rjust(n,'0') #  n-len(a12)만큼 0을 붙임 # zfill도 알아둘 것 
        a12=a12.replace('1','#') # replace로 1을 #으로 대체
        a12=a12.replace('0',' ') # replace로 0을 공백으로 대체
        answer.append(a12)
    return answer
