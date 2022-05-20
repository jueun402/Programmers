import re 

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = str(int(bin(arr1[i])[2:]) + int(bin(arr2[i])[2:]))
        tmp = tmp.zfill(n)
        tmp = re.sub('0',' ', str(tmp))
        tmp = re.sub('[1-9]','#', str(tmp))
        answer.append(tmp)
    return answer

# ---다른 사람 풀이 
# 비트 연산 쓰고싶었는데, 쓰는 방법을 몰라서 저렇게 했다.
# 이렇게 쓰면 되는구나 ~^~^~ 
a12 = str(bin(i|j)[2:])

# 풀이를 개선해보자! 

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        tmp = str(bin((a1|a2))[2:]) # 비트연산 or 
        tmp = tmp.zfill(n) # 0을 앞에 채우기 
        tmp = tmp.replace('0',' ')
        tmp = tmp.replace('1','#')
        answer.append(tmp)
    return answer
        
        
        
        
        
    return answer
