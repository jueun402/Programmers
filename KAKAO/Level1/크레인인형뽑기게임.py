#------------------ 코드 --------------------------
import numpy as np
from collections import deque

def solution(board, moves):
     
    t_board = np.transpose(board) 
    # array([[0, 0, 0, 4, 3],
    #    [0, 0, 2, 2, 5],
    #    [0, 1, 5, 4, 1],
    #    [0, 0, 0, 4, 3],
    #    [0, 3, 1, 2, 1]])

    # 0 제거 
    boards = []
    for i, b in enumerate(t_board):
        boards.append(deque(list(filter(lambda x : x!=0, b))))

    # moves에 따라서 차곡차곡 쌓기 
    move_stack = []
    for m in moves:
        try: move_stack.append(boards[m-1].popleft()) 
        except: continue 

    # moves의 stack의 길이가 2가 안되면 => 터트릴 수 없음  
    if len(move_stack) > 1:
        res_stack = [move_stack[0]] # 겹치는 숫자 제거하기 위한 stack 
        cnt = 0 # 제거한 수 count

        for i in range(1,len(move_stack)):

            # 스택이 비었는데 검색해야할건 남아있으면
            if not res_stack and len(move_stack):
                # 다음 move_stack 넣고 비교 
                res_stack.append(move_stack[i]) 
                continue      

            # res_stack의 top 숫자와 다음 숫자가 같으면 pop 
            if res_stack[-1] == move_stack[i]:
                res_stack.pop()
                # res_stack의 숫자 pop + move_stack[i]을 제거한 것 (여기서는 stack에 append하지 않음 == 제거)
                cnt +=2 
            else:
            # res_stack의 top 숫자와 다음 숫자가 다르면 stack에 넣어주기 
                res_stack.append(move_stack[i])
    else:       
        cnt = 0 
    return cnt
#-----------------  문제 후기  -------------------

# 01. 문제 이해를 제대로 못해서(feat. 카카오,,, 그냥 숫자로 줘요 이상한 어피치 얼굴 말고 -_-) 진짜 한~참 헤맸다.

# 질문하기에서 https://programmers.co.kr/questions/24766 이 분의 문제 보충 설명을 보고 이해했다
# board	= [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
# board가 한 줄씩 열 단위로  쌓이는줄 알았는데 

# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 3],
#  [0 ,2, 5, 0, 1],
#  [4 ,2, 4, 4, 2],
#  [3 ,5, 1, 3, 1]]

# 이렇게 행 단위로 쌓이는 거였다. 이런이런... 

# 별 생각 없이 이젠 그냥 풀기에 집중해서 numpy를 써서 코드를 짰는데, 
# 비효율적인 것 같아서 다른분들의 코드를 참고해서 다시 풀어보도록 하겠다. 


#----------------- 다른 풀이 참고 -------------------

# 이거 보고 기억해야 할 내용!! 
# 1. 인형이 들어올 때 마다 stack을 비교! 
#   => 이렇게 하면 굳이 나중에 for문 돌려서 머리아프게 비교하지 않아도 된다! 
#   => + 지금 들어온 인형, 직전에 들어온 인형을 bucket[:-2]로 슬라이싱 

# 2. 2중 for문이 꼭 비효율적인게 아니라는 것! 
#   => 0이 아닌 수를 board line마다 탐색해야한다는 생각에 미리 제거해버리고 했었는데
#   => for문을 한번 돌면서 여러 과정을 처리하는게 더 효율적이라는걸 알았따. 
#   => ex. 나는 0제거하는 for문 한번, stack 쌓는 for문 한번, 이런식으로 했다.
#   => 2중for문 너무 두려워하지 말자! 

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	

def solution(board, moves):
    answer = 0 # cnt 
    bucket = [] # stack 

    for move in moves:
        for line in board:
            # 0이 아니면 stack에 추가하기 
            if line[move-1]:
                bucket.append(line[move-1])
                # 추가했으면 0으로 바꾸기 
                line[move-1] = 0
                # 하나만 추가해야 하므로 board line 탐색 break 
                break 
    
        # 인형 뽑을 때 마다 stack에 겹치는 인형 확인 (인형이 들어올 때 마다 비교... 대단하다)
        # 현재 넣은 인형과 그 전에 있던 인형 비교 
        # 만약 현재 넣은 인형과 그 전에 있던 인형이 똑같다면 
        if len(bucket) >=2 and bucket[-1] == bucket[-2]:
            answer +=2 # cnt +=2 
            bucket = bucket[:-2] # bucket에 방금 넣은 인형, 그 전에 있던 인형 제거 
    
    return answer