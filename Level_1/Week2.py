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
    # commands  = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	# command가 조건이다 
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
from itertools import cycle # 무한 반복자 
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
