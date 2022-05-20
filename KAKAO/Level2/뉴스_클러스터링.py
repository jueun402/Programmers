'''
# 문제 설명 

자카드 유사도 = a,b 집합 사이 자카드 유사도

ex 1)---------------------------------------

a = {1,2,3}
b = {2,3,4}

a n b = {2,3}
a u b = {1,2,3,4}

a,b 자카드 유사도 = 2/4  

ex 2)---------------------------------------
if a n b = {} 
a,b 지카드 유사도 = 1 

ex 3)---------------------------------------
a = {1,1,1}
b = {1,1,1,1,1}

a n b = {1,1,1}
a u b = {1,1,1,1,1}

a,b 자카드 유사도 = 3/5 

ex 4)---------------------------------------
a = {1,1,2,2,3}
b = {1,2,2,4,5}

a n b = {1,2,2}
=> 교집합 {1,2}
=> min(a에서 1 ,b에서 1)

a u b = {1,1,2,2,3,4,5}
=> 합집합 = {1,2,3,4,5}
=> 교집합 = {1,2}
=> max(a에서 1, b에서 1), max(a에서 2, b에서 2 )
=> {1,1}, {2,2}

a,b 자카드 유사도 = 3/7  

ex 5)---------------------------------------
a = 'franch'
b = 'french'

다중집합 = {fr, ra, an, nc, ce }, {fr, re, en, nc, ch}
교집합 = {fr, nc}
합집합 = {fr, ra, an, nc, ce, re, en, ch }

a,b 자카드 유사도 = 2/8 


> 입력으로 str1, str2 두 문자열이 들어온다. 
> 각 문자열 길이 = 2이상 1000이하 
> 두 글자씩 끊어서 다중집합의 원소로 만든다
> 공백, 숫자, 특수문자가 들어있는 경우 글자쌍 버린다.
> ab+로 들어오면 ab, b+ (x)

ex 6)---------------------------------------

[7, 9, 10, 11번 반례]

str1 = ' abc'
str2 = 'abbb'
인 경우 출력 값이 16384가 나와야 합니다.

만약 21845값이 나온다면 합집합 로직의 문제 입니다.
합집합 = ['ab', 'bc', 'bb', 'bb'] (o)
합집합 = ['ab', 'bc', 'bb'] (x)

'''

str1 = ' abc'
str2 = 'abbb'
def solution(str1, str2):

    # 문자열 2개씩 split  
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    inter = set(str1) & set(str2) # 교집합
    numerator = len(str1)+len(str2)  # 분모 = str1과 str2의 문자열 길이 - (str1과 str2의 교집합 요소 중 가장 적은 수 cnt )
    denominator = 0 # 분자 = str1과 str2의 교집합 요소 중 가장 적은 수 cnt 

    # 교집합 요소 중 str1과 str2에서 가장 적은 수 count 
    for i in inter:
        inter_min = min(str1.count(i), str2.count(i)) 
        denominator += inter_min # 분자에는 더해주고 
        numerator -= inter_min # 분모에는 빼주기 (str1+str2하면서 개수를 다 cnt했으니까)
    
    # 분모가 0일 경우 예외처리 
    try:
        return int((denominator/numerator) * 65536)
    except:
        return 65536