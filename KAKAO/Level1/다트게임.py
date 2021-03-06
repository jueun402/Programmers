'''
1. 3번의 기회
2. 0~10점 
3. 점수 S, D, T 영역 존재  
    1제곱, 2제곱, 3제곱 
4. 스타상* 아차상# 
    스타상 * => 해당 점수,  바로전에 얻은 점수 => 각 2배 
    아차상 # => 해당 점수 마이너스 
5. 스타상 * => 첫번째 기회에도 나올 수 있음
    첫번째 스타상 점수만 두배 
    
6. 스타상 * 효과 = 다른 스타상*과 중첨 O 
    중첩된 스타상의 점수는 4배가 된다 
    EX. 
    상1   상2     상3 
    2배   스타상  스타상 
          2배      2배
          2배
          = 4배 
7. 스타상의 효과는 아차상의 효과와 중첩될 수 있음 
   중첩된 아차상의 점수는 -2배가 된다.            

8. S, D, T 점수마다 하나씩 ㄱ존재 
9. *, # 점숨다 둘 중 하나만 존재 OR 존재하지 않을 수 있음 

0~10의 정수, 문자 SDT, *#로 구성된 문자열이 입력될 시 총 점수 반환 함수 작성 
'''

##-----------------------------------내 풀이 -----------------------
# 1. S, D, T 마다 점수를 분리한다. 
# 2. 만약 *(스타상)이나  #(아차상)이 나오면, 앞에 나왔던 S,D,T에 연산을 수행해준다. 

# 예시로 설명해보면
# 1S2D*3T이 존재할 때 

# 1. 문자 하나하나마다 check하면서 s, d, t가 나오면 리스트에 저장해준다 	

# 2-1. [1S, 2D] 이렇게 될 텐데, * 문자가 나오면 *2 연산을 진행해준다.
#    - 여기서 *2 연산을 하기 전에 리스트의 길이가 2 이상인지 CHECK해준다.
#    - 만약 2 이상이라면, *문자가 나오기 전, 나오기 전전의 문자에 *2를 해준다.
#    - 만약 리스트 길이가 1 미만이라면, * 문자가 나오기 전에만 *2를 해준다.
# [1S, 2D] 이 경우 리스트는 [(1**1)*2, (2**2)*2] 이렇게 된다. 

# 2-2. #이 나오는 경우는 위와 같이 #문자가 나오기 전 문자에 *-1을 해주면 된다

 
def solution(dartResult):
    str = []
    dart = ''
    for i,d in enumerate(dartResult):
        dart += d

        if 'S' in dart :
            str.append(int(dart[:-1])) # 'S'앞의 숫자 리스트에 추가 **1
            dart =''
            
        if 'D' in dart:
            str.append(int(dart[:-1])**2) # 'D'앞의 숫자 리스트에 추가 **2
            dart = ''
            
        if 'T' in dart:
            str.append(int(dart[:-1])**3) # 'T'앞의 숫자 리스트에 추가 **3
            dart= '' 

        if '*' in dart:
            dart = ''
            # 리스트의 길이가 1이 넘으면 2개 계산 
            if len(str) > 1:
                str[-1] = str[-1]*2
                str[-2] = str[-2]*2
                
            # 리스트의 길이가 1이 넘지 않으면 1개 계산 
            else:
                str[-1] = str[-1]*2  
                     
        if '#' in dart:
            # '#'이 나오면 *-1 계산 
            dart = ''
            str[-1] = str[-1]*-1

    return sum(str)
