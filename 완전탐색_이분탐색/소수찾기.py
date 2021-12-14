# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# 풀이
# numbers의 조합에서 가장 큰 숫자를 찾음 (maxNum)
# 1. 2~maxNum 까지 숫자들 중 numbers의 요소들을 포함한 숫자 후보1 찾기 
# 2. 숫자 후보1 중 numbers의 요소들의 개수와 동일한 숫자 후보2 찾기 
# 3. 숫자 후보2 중 prime number 찾기 


from collections import Counter

def isPrime(x):
    for i in range(2, int(x **(1/2))+1):
        if(x%i ==0):
            return False
    return True

def solution(numbers):
    maxNum = int("".join(sorted(list(numbers),reverse=True))) # numbers의 조합 중 가장 큰 수 
    cntNum = Counter(numbers)
    
     # numbers의 숫자들로 구성된 수     
    filter_candidate = list(filter(lambda i : list(set(str(i)) - set(numbers)) == [], range(2,maxNum+1)))
    # numbers의 숫자들로 구성되어 있으며, 개수가 같은 수
    candidate = list(filter(lambda i : (list(Counter(str(i)) - cntNum)) == [] , filter_candidate))  

    return len([1 for i in candidate if isPrime(i)]) # 후보들 중 소수인 수 
