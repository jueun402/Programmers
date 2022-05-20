'''
왼쪽 3개 숫자 [1,4,7] => 왼
오른쪽 3개 숫자 [3,6,9] => 오
가운데 4개 숫자 [2,5,8,0]  => 가까운 손가락 
    => 거리 같으면, 오른손잡이는 오 / 왼손잡이 왼
'''
#------------------ 코드 --------------------------

# 가운데 키패드 거리 계산
def pad_dist(l,r, c): # 왼손, 오른손, 가운데 키패드
    keypad = ['123','456','789','*0#']

    # 왼쪽, 오른쪽, 가운데 좌표 
    lx, ly, rx, ry, cx, cy   = 0,0,0,0,0,0
    
    # left, right, center 좌표 구해서 거리 구하자 
    for i,pad in enumerate(keypad):

        # left 
        if pad.find(str(l)) > -1:  ly, lx = i, pad.find(str(l))
        
        # right 
        if pad.find(str(r)) > -1:  ry, rx = i, pad.find(str(r))
            
        # center
        if pad.find(str(c)) > -1:  cy, cx = i, pad.find(str(c))
        
    right, left = (abs(cy-ry) + abs(cx-rx)) , (abs(cy-ly) + abs(cx-lx)) 
    
    if right == left: return 'h'
    elif right < left: return 'r'
    elif  right > left: return 'l'

def solution(numbers, hand):
    result = ''
    L, R = '*','#'

    for i in numbers:
        # 왼손 
        if i in [1,4,7]:
            result += 'L'
            L = i

        # 오른손 
        elif i in [3,6,9]:
            result += 'R'
            R = i

        # 가운데 
        else:
            res = pad_dist(L,R,i) 

            if res == 'r':
                R = i
                result += 'R'

            elif res== 'l':
                L = i
                result += 'L'

            elif res == 'h':
                if hand == 'right':
                    R = i
                    result += 'R'
                else:
                    L = i
                    result += 'L'
    
    return result
#----------------- 풀이 회고  -------------------

# 채점 중 8번 15번에서 오류나서 검색해봤더니 L,R을 0,0으로 초기화 한 것이 오류였다!! 
# L,R을 0,0으로 초기화하면, 0부터 거리를 재야하기 때문에 오류가 발생한다. 
# L, R = 0,0 
L, R = '*','#'

#----------------- 다른 풀이 참고 -------------------

# 나는 키패드의 거리를 아래처럼 복잡하게 계산했는데

def pad_dist(l,r, c): # 왼손, 오른손, 가운데 키패드
    keypad = ['123','456','789','*0#']

    # 왼쪽, 오른쪽, 가운데 좌표 
    lx, ly, rx, ry, cx, cy   = 0,0,0,0,0,0
    
    # left, right, center 좌표 구해서 거리 구하자 
    for i,pad in enumerate(keypad):

        # left 
        if pad.find(str(l)) > -1:  ly, lx = i, pad.find(str(l))
        
        # right 
        if pad.find(str(r)) > -1:  ry, rx = i, pad.find(str(r))
            
        # center
        if pad.find(str(c)) > -1:  cy, cx = i, pad.find(str(c))
        
    right, left = (abs(cy-ry) + abs(cx-rx)) , (abs(cy-ly) + abs(cx-lx)) 
    
    if right == left: return 'h'
    elif right < left: return 'r'
    elif  right > left: return 'l'
    
# 이 방법을 바로 DICTIONARY로 변형한 분이 있었다! 
key_pad = {1:(0,0),2:(0,1),3:(0,2),
            4:(1,0),5:(1,1),6:(1,2),
            7:(2,0),8:(2,1),9:(2,2),
            '*':(3,0),0:(3,1),'#':(3,2)}


# 이걸 참고해서 코드를 더 간단하게 만들어보자 
# 엄청 간단하다!! + 이게 시간복잡도 측면에서 훨씬 효율적이다! 
# 딕셔너리를 잘 다루도록 공부해야겠다. 

def pad_dist(l,r, c): # 왼손, 오른손, 가운데 키패드, 손
    key_pad = {
        1: (0,0), 2 : (0,1), 3 : (0,2),
        4: (1,0), 5 : (1,1), 6 : (1,2),
        7 : (2,0), 8: (2,1), 9 : (2,2),
        '*' : (3,0), 0 : (3,1), '#' : (3,2) }

    ly, lx = key_pad[l] # 왼쪽 좌표  
    ry, rx = key_pad[r] # 오른쪽 좌표
    cy, cx = key_pad[c] # 가운데 좌표 
    
    right, left = (abs(cy-ry) + abs(cx-rx)) , (abs(cy-ly) + abs(cx-lx)) 

    # 거리 가까운 손 return 
    if right == left: return 'h'
    elif right < left: return 'r'
    elif  right > left: return 'l'
    
def solution(numbers, hand):
    result = ''
    L, R = '*','#' # 초기값 0,0으로 두지 않도록 조심 ! 

    for i in numbers:
        # 왼손 
        if i in [1,4,7]:
            result += 'L'
            L = i

        # 오른손 
        elif i in [3,6,9]:
            result += 'R'
            R = i

        # 가운데 
        else:
            res = pad_dist(L,R,i) 

            if res == 'r':
                R = i
                result += 'R'

            elif res== 'l':
                L = i
                result += 'L'

            elif res == 'h':
                if hand == 'right':
                    R = i
                    result += 'R'
                else:
                    L = i
                    result += 'L'
    
    return result